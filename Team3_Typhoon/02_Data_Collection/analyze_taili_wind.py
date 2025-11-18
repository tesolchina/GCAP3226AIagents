#!/usr/bin/env python3
"""Analyze 10-minute wind data for Taili typhoon period and plot 8 reference stations vs HKO No.8 threshold.

Output files are written to `Output Taili` folder inside this data directory.
"""
import os
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


DATA_DIR = Path(__file__).resolve().parent / '泰利 20230717'
OUTPUT_DIR = Path(__file__).resolve().parent / 'Output Taili'
OUTPUT_DIR.mkdir(exist_ok=True)

# Reference stations (as listed in 8stations.md)
REF_STATIONS = [
    'Ta Kwu Ling',
    'Lau Fau Shan',
    'Sha Tin',
    'Tsing Yi',
    'Kai Tak',
    'Cheung Chau',
    'Sai Kung',
    'Chek Lap Kok',
]

# HKO No.8 lower threshold for 10-minute sustained wind (km/h)
NO8_THRESHOLD = 63

# Time window when Signal No.8 was effective for Taili
START_TS = pd.to_datetime('2023-07-17 00:40')
END_TS = pd.to_datetime('2023-07-17 16:20')


def read_all_csvs(data_dir: Path) -> pd.DataFrame:
    files = sorted([p for p in data_dir.glob('*.csv')])
    dfs = []
    for f in files:
        try:
            df = pd.read_csv(f)
        except Exception:
            continue
        if 'Date time' not in df.columns:
            continue
        df = df.copy()
        # CSV uses time field like 202307170040
        df['dt'] = pd.to_datetime(df['Date time'].astype(str), format='%Y%m%d%H%M', errors='coerce')
        df = df.dropna(subset=['dt'])
        dfs.append(df)
    if not dfs:
        raise SystemExit('No CSV files found or no parsable data in %s' % data_dir)
    all_df = pd.concat(dfs, ignore_index=True)
    return all_df


def extract_reference_timeseries(all_df: pd.DataFrame) -> pd.DataFrame:
    # Filter window
    df = all_df[(all_df['dt'] >= START_TS) & (all_df['dt'] <= END_TS)].copy()
    if df.empty:
        return pd.DataFrame()
    # Keep relevant columns
    col_speed = '10-Minute Mean Speed(km/hour)'
    df[col_speed] = pd.to_numeric(df[col_speed], errors='coerce')
    # Pivot to wide format with dt index and stations as columns
    pivot = df.pivot_table(index='dt', columns='Automatic Weather Station', values=col_speed, aggfunc='first')
    # Reindex time series to include regular 10-min steps in the window
    full_index = pd.date_range(start=START_TS, end=END_TS, freq='10T')
    pivot = pivot.reindex(full_index)
    # Keep only reference stations (if present)
    available = [s for s in REF_STATIONS if s in pivot.columns]
    pivot_ref = pivot[available]
    return pivot_ref


def plot_timeseries(pivot_ref: pd.DataFrame):
    plt.rcParams.update({'figure.max_open_warning': 0})
    fig, ax = plt.subplots(figsize=(14,6))
    for col in pivot_ref.columns:
        ax.plot(pivot_ref.index, pivot_ref[col], marker='o', label=col)
    # threshold line
    ax.axhline(NO8_THRESHOLD, color='k', linestyle='--', linewidth=1.5, label=f'No.8 threshold ({NO8_THRESHOLD} km/h)')
    # highlight regions where >=50% stations exceed threshold
    above = (pivot_ref >= NO8_THRESHOLD)
    frac = above.sum(axis=1) / max(1, len(pivot_ref.columns))
    # fill_between expects x, y1, y2. We'll shade entire vertical region using transform
    ax.fill_between(pivot_ref.index, 0, pivot_ref.max(axis=1).fillna(0), where=frac>=0.5, color='red', alpha=0.08, transform=ax.get_xaxis_transform(), label='>=50% stations >= threshold')

    ax.set_title('10-min Mean Wind Speed — 8 Reference Stations (Taili)\n{} to {}'.format(START_TS.strftime('%Y-%m-%d %H:%M'), END_TS.strftime('%Y-%m-%d %H:%M')))
    ax.set_ylabel('Wind speed (km/h)')
    ax.set_xlabel('Datetime')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax.legend(loc='upper right', fontsize='small')
    plt.xticks(rotation=45)
    plt.tight_layout()
    outpng = OUTPUT_DIR / 'taili_8stations_wind_timeseries.png'
    fig.savefig(outpng)
    print('Saved plot to', outpng)
    plt.close(fig)


def save_csv(pivot_ref: pd.DataFrame):
    outcsv = OUTPUT_DIR / 'taili_8stations_timeseries.csv'
    pivot_ref.to_csv(outcsv, index_label='datetime')
    print('Saved timeseries CSV to', outcsv)


def main():
    print('Reading CSV files from', DATA_DIR)
    all_df = read_all_csvs(DATA_DIR)
    pivot_ref = extract_reference_timeseries(all_df)
    if pivot_ref.empty:
        print('No reference station data found in the time window')
        return
    save_csv(pivot_ref)
    plot_timeseries(pivot_ref)


if __name__ == '__main__':
    main()
