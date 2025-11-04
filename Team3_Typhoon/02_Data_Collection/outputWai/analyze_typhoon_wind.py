#!/usr/bin/env python3
"""
Typhoon Weipa Wind Speed Analysis
Analysis of wind speed data from 8 HKO reference stations during Signal No. 8
Signal No. 8 Period: 2025-07-20 00:20 to 2025-07-20 19:40
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os
import glob
import numpy as np

# Configuration
DATA_DIR = "/workspaces/GCAP3226AIagents/Team3_Typhoon/02_Data_Collection/韋帕 7.19 2230 - 7.21 0010"
OUTPUT_DIR = "/workspaces/GCAP3226AIagents/Team3_Typhoon/02_Data_Collection/outputWai"

# 8 Reference stations used by HKO for tropical cyclone warnings
REFERENCE_STATIONS = [
    'Ta Kwu Ling',      # 打鼓嶺
    'Lau Fau Shan',     # 流浮山
    'Sha Tin',          # 沙田
    'Tsing Yi',         # 青衣
    'Kai Tak',          # 啓德
    'Cheung Chau',      # 長洲
    'Sai Kung',         # 西質
    'Chek Lap Kok'      # 赤鱲角
]

# Signal No. 8 thresholds (km/h)
SIGNAL_8_LOWER_THRESHOLD = 63  # Lower bound for Signal 8
SIGNAL_8_UPPER_THRESHOLD = 117  # Upper bound for Signal 8

# Signal No. 8 effective period
SIGNAL_8_START = datetime(2025, 7, 20, 0, 20)
SIGNAL_8_END = datetime(2025, 7, 20, 19, 40)


def load_wind_data():
    """Load all CSV files and combine into a single DataFrame"""
    csv_files = sorted(glob.glob(os.path.join(DATA_DIR, "*.csv")))
    
    all_data = []
    for file in csv_files:
        df = pd.read_csv(file)
        all_data.append(df)
    
    # Combine all dataframes
    combined_df = pd.concat(all_data, ignore_index=True)
    
    # Convert datetime column
    combined_df['datetime'] = pd.to_datetime(combined_df['Date time'], format='%Y%m%d%H%M')
    
    # Convert wind speed to numeric, handling N/A values
    combined_df['10-Minute Mean Speed(km/hour)'] = pd.to_numeric(
        combined_df['10-Minute Mean Speed(km/hour)'], errors='coerce'
    )
    
    return combined_df


def filter_signal_8_period(df):
    """Filter data for Signal No. 8 period"""
    mask = (df['datetime'] >= SIGNAL_8_START) & (df['datetime'] <= SIGNAL_8_END)
    return df[mask].copy()


def filter_reference_stations(df):
    """Filter data for the 8 reference stations"""
    return df[df['Automatic Weather Station'].isin(REFERENCE_STATIONS)].copy()


def create_time_series_plot(df):
    """Create time series plot showing wind speeds at all 8 stations"""
    plt.figure(figsize=(16, 10))
    
    for station in REFERENCE_STATIONS:
        station_data = df[df['Automatic Weather Station'] == station]
        station_data = station_data.sort_values('datetime')
        
        plt.plot(station_data['datetime'], 
                station_data['10-Minute Mean Speed(km/hour)'],
                marker='o', markersize=3, linewidth=1.5, 
                label=station, alpha=0.8)
    
    # Add threshold lines
    plt.axhline(y=SIGNAL_8_LOWER_THRESHOLD, color='red', linestyle='--', 
                linewidth=2, label=f'Signal 8 Lower Threshold ({SIGNAL_8_LOWER_THRESHOLD} km/h)')
    plt.axhline(y=SIGNAL_8_UPPER_THRESHOLD, color='darkred', linestyle='--', 
                linewidth=2, label=f'Signal 8 Upper Threshold ({SIGNAL_8_UPPER_THRESHOLD} km/h)')
    
    # Add shaded region for Signal 8 range
    plt.axhspan(SIGNAL_8_LOWER_THRESHOLD, SIGNAL_8_UPPER_THRESHOLD, 
                alpha=0.1, color='red', label='Signal 8 Range')
    
    plt.xlabel('Date and Time', fontsize=12, fontweight='bold')
    plt.ylabel('10-Minute Mean Wind Speed (km/h)', fontsize=12, fontweight='bold')
    plt.title('Wind Speed at 8 HKO Reference Stations during Typhoon Weipa Signal No. 8\n'
              f'{SIGNAL_8_START.strftime("%Y-%m-%d %H:%M")} to {SIGNAL_8_END.strftime("%Y-%m-%d %H:%M")}',
              fontsize=14, fontweight='bold', pad=20)
    
    plt.legend(loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    output_file = os.path.join(OUTPUT_DIR, 'wind_speed_time_series.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"✓ Time series plot saved: {output_file}")
    plt.close()


def create_heatmap(df):
    """Create heatmap showing wind speeds across stations and time"""
    # Pivot data for heatmap
    pivot_data = df.pivot_table(
        values='10-Minute Mean Speed(km/hour)',
        index='Automatic Weather Station',
        columns='datetime',
        aggfunc='mean'
    )
    
    # Reorder rows to match REFERENCE_STATIONS order
    pivot_data = pivot_data.reindex(REFERENCE_STATIONS)
    
    plt.figure(figsize=(20, 8))
    
    # Create custom colormap with threshold highlighting
    cmap = sns.color_palette("YlOrRd", as_cmap=True)
    
    sns.heatmap(pivot_data, cmap=cmap, linewidths=0.5, 
                cbar_kws={'label': 'Wind Speed (km/h)'}, 
                vmin=0, vmax=120)
    
    plt.xlabel('Date and Time', fontsize=12, fontweight='bold')
    plt.ylabel('Weather Station', fontsize=12, fontweight='bold')
    plt.title('Wind Speed Heatmap - 8 HKO Reference Stations during Typhoon Weipa Signal No. 8\n'
              f'{SIGNAL_8_START.strftime("%Y-%m-%d %H:%M")} to {SIGNAL_8_END.strftime("%Y-%m-%d %H:%M")}',
              fontsize=14, fontweight='bold', pad=20)
    
    # Format x-axis to show fewer labels
    n_ticks = 20
    tick_positions = np.linspace(0, len(pivot_data.columns) - 1, n_ticks, dtype=int)
    plt.xticks(tick_positions + 0.5, 
               [pivot_data.columns[i].strftime('%m-%d %H:%M') for i in tick_positions],
               rotation=45, ha='right')
    
    plt.tight_layout()
    
    output_file = os.path.join(OUTPUT_DIR, 'wind_speed_heatmap.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"✓ Heatmap saved: {output_file}")
    plt.close()


def create_station_comparison(df):
    """Create box plot comparing wind speeds across stations"""
    plt.figure(figsize=(14, 8))
    
    # Prepare data for box plot
    station_data = []
    station_labels = []
    
    for station in REFERENCE_STATIONS:
        station_df = df[df['Automatic Weather Station'] == station]
        wind_speeds = station_df['10-Minute Mean Speed(km/hour)'].dropna()
        station_data.append(wind_speeds)
        station_labels.append(station)
    
    # Create box plot
    bp = plt.boxplot(station_data, labels=station_labels, patch_artist=True,
                     showmeans=True, meanline=True)
    
    # Color boxes
    for patch in bp['boxes']:
        patch.set_facecolor('lightblue')
        patch.set_alpha(0.7)
    
    # Add threshold lines
    plt.axhline(y=SIGNAL_8_LOWER_THRESHOLD, color='red', linestyle='--', 
                linewidth=2, label=f'Signal 8 Lower Threshold ({SIGNAL_8_LOWER_THRESHOLD} km/h)')
    plt.axhline(y=SIGNAL_8_UPPER_THRESHOLD, color='darkred', linestyle='--', 
                linewidth=2, label=f'Signal 8 Upper Threshold ({SIGNAL_8_UPPER_THRESHOLD} km/h)')
    
    plt.xlabel('Weather Station', fontsize=12, fontweight='bold')
    plt.ylabel('10-Minute Mean Wind Speed (km/h)', fontsize=12, fontweight='bold')
    plt.title('Wind Speed Distribution Comparison - 8 HKO Reference Stations\n'
              'during Typhoon Weipa Signal No. 8',
              fontsize=14, fontweight='bold', pad=20)
    plt.xticks(rotation=45, ha='right')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    
    output_file = os.path.join(OUTPUT_DIR, 'wind_speed_comparison.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"✓ Station comparison plot saved: {output_file}")
    plt.close()


def create_threshold_analysis(df):
    """Analyze how many stations exceeded thresholds over time"""
    # Group by datetime and count stations exceeding threshold
    threshold_counts = []
    
    for dt in sorted(df['datetime'].unique()):
        dt_data = df[df['datetime'] == dt]
        
        count_above_lower = (dt_data['10-Minute Mean Speed(km/hour)'] >= SIGNAL_8_LOWER_THRESHOLD).sum()
        count_above_upper = (dt_data['10-Minute Mean Speed(km/hour)'] >= SIGNAL_8_UPPER_THRESHOLD).sum()
        total_stations = len(dt_data)
        
        threshold_counts.append({
            'datetime': dt,
            'above_lower_threshold': count_above_lower,
            'above_upper_threshold': count_above_upper,
            'total_stations': total_stations,
            'percentage_above_lower': (count_above_lower / total_stations * 100) if total_stations > 0 else 0
        })
    
    threshold_df = pd.DataFrame(threshold_counts)
    
    # Plot
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 10), sharex=True)
    
    # Plot 1: Number of stations above thresholds
    ax1.plot(threshold_df['datetime'], threshold_df['above_lower_threshold'], 
             marker='o', linewidth=2, color='orange', label=f'≥ {SIGNAL_8_LOWER_THRESHOLD} km/h')
    ax1.plot(threshold_df['datetime'], threshold_df['above_upper_threshold'], 
             marker='s', linewidth=2, color='red', label=f'≥ {SIGNAL_8_UPPER_THRESHOLD} km/h')
    ax1.axhline(y=4, color='green', linestyle='--', linewidth=2, 
                label='HKO Criterion: 4+ stations (50%)')
    ax1.set_ylabel('Number of Stations', fontsize=12, fontweight='bold')
    ax1.set_title('Number of Stations Exceeding Wind Speed Thresholds Over Time',
                  fontsize=13, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(0, 8.5)
    
    # Plot 2: Percentage of stations above lower threshold
    ax2.bar(threshold_df['datetime'], threshold_df['percentage_above_lower'], 
            width=0.008, color='steelblue', alpha=0.7)
    ax2.axhline(y=50, color='green', linestyle='--', linewidth=2, 
                label='HKO Criterion: 50% of stations')
    ax2.set_xlabel('Date and Time', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Percentage (%)', fontsize=12, fontweight='bold')
    ax2.set_title('Percentage of Stations Meeting Signal 8 Wind Speed Criterion',
                  fontsize=13, fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim(0, 105)
    
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    output_file = os.path.join(OUTPUT_DIR, 'threshold_analysis.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"✓ Threshold analysis plot saved: {output_file}")
    plt.close()
    
    return threshold_df


def create_summary_statistics(df):
    """Generate and save summary statistics"""
    summary_stats = []
    
    for station in REFERENCE_STATIONS:
        station_data = df[df['Automatic Weather Station'] == station]['10-Minute Mean Speed(km/hour)']
        
        stats = {
            'Station': station,
            'Mean Speed (km/h)': station_data.mean(),
            'Max Speed (km/h)': station_data.max(),
            'Min Speed (km/h)': station_data.min(),
            'Std Dev (km/h)': station_data.std(),
            'Times ≥ 63 km/h': (station_data >= SIGNAL_8_LOWER_THRESHOLD).sum(),
            'Times ≥ 117 km/h': (station_data >= SIGNAL_8_UPPER_THRESHOLD).sum(),
            'Total Readings': len(station_data)
        }
        summary_stats.append(stats)
    
    stats_df = pd.DataFrame(summary_stats)
    
    # Save to CSV
    output_file = os.path.join(OUTPUT_DIR, 'summary_statistics.csv')
    stats_df.to_csv(output_file, index=False)
    print(f"✓ Summary statistics saved: {output_file}")
    
    # Create a formatted table image
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.axis('tight')
    ax.axis('off')
    
    # Format numbers in the table
    table_data = []
    for _, row in stats_df.iterrows():
        table_data.append([
            row['Station'],
            f"{row['Mean Speed (km/h)']:.1f}",
            f"{row['Max Speed (km/h)']:.1f}",
            f"{row['Min Speed (km/h)']:.1f}",
            f"{row['Std Dev (km/h)']:.1f}",
            f"{int(row['Times ≥ 63 km/h'])}",
            f"{int(row['Times ≥ 117 km/h'])}",
            f"{int(row['Total Readings'])}"
        ])
    
    table = ax.table(cellText=table_data,
                     colLabels=stats_df.columns,
                     cellLoc='center',
                     loc='center',
                     bbox=[0, 0, 1, 1])
    
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 2)
    
    # Style header
    for i in range(len(stats_df.columns)):
        table[(0, i)].set_facecolor('#4CAF50')
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    # Alternate row colors
    for i in range(1, len(table_data) + 1):
        for j in range(len(stats_df.columns)):
            if i % 2 == 0:
                table[(i, j)].set_facecolor('#f0f0f0')
    
    plt.title('Summary Statistics - Wind Speed at 8 HKO Reference Stations\n'
              'during Typhoon Weipa Signal No. 8',
              fontsize=14, fontweight='bold', pad=20)
    
    output_file = os.path.join(OUTPUT_DIR, 'summary_statistics_table.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"✓ Summary statistics table saved: {output_file}")
    plt.close()
    
    return stats_df


def generate_report(df, threshold_df, stats_df):
    """Generate a markdown report with analysis results"""
    report = f"""# Typhoon Weipa (韋帕) Wind Speed Analysis Report

## Analysis Period
- **Signal No. 8 Effective Period**: {SIGNAL_8_START.strftime('%Y-%m-%d %H:%M')} to {SIGNAL_8_END.strftime('%Y-%m-%d %H:%M')}
- **Duration**: {(SIGNAL_8_END - SIGNAL_8_START).total_seconds() / 3600:.1f} hours

## HKO Signal No. 8 Criteria
According to Hong Kong Observatory guidelines:
- **Wind Speed Range**: 63-117 km/h (sustained winds)
- **Issuance Criterion**: Signal is issued when **half or more** (4 or more out of 8) reference anemometers register or are expected to register sustained winds within the prescribed range and the wind condition is expected to persist.

## 8 Reference Stations
The following 8 near-sea level reference anemometers are used by HKO for tropical cyclone warnings:

1. **Ta Kwu Ling** (打鼓嶺)
2. **Lau Fau Shan** (流浮山)
3. **Sha Tin** (沙田)
4. **Tsing Yi** (青衣)
5. **Kai Tak** (啓德)
6. **Cheung Chau** (長洲)
7. **Sai Kung** (西質)
8. **Chek Lap Kok** (赤鱲角)

## Key Findings

### 1. Overall Wind Speed Statistics

"""
    
    # Add summary statistics
    for _, row in stats_df.iterrows():
        report += f"**{row['Station']}**\n"
        report += f"- Mean Speed: {row['Mean Speed (km/h)']:.1f} km/h\n"
        report += f"- Maximum Speed: {row['Max Speed (km/h)']:.1f} km/h\n"
        report += f"- Times exceeding 63 km/h threshold: {int(row['Times ≥ 63 km/h'])} out of {int(row['Total Readings'])} readings "
        report += f"({row['Times ≥ 63 km/h'] / row['Total Readings'] * 100:.1f}%)\n\n"
    
    # Calculate overall compliance
    max_stations_above = threshold_df['above_lower_threshold'].max()
    times_criterion_met = (threshold_df['above_lower_threshold'] >= 4).sum()
    total_time_points = len(threshold_df)
    
    report += f"""
### 2. Signal No. 8 Criterion Compliance

- **Maximum number of stations simultaneously exceeding 63 km/h**: {int(max_stations_above)} out of 8 stations
- **Times when 4+ stations met criterion**: {times_criterion_met} out of {total_time_points} time points ({times_criterion_met/total_time_points*100:.1f}%)
- **Peak wind speed recorded**: {df['10-Minute Mean Speed(km/hour)'].max():.1f} km/h

### 3. Threshold Exceedance Summary

"""
    
    # Count how many stations never/rarely exceeded threshold
    stations_below_threshold = stats_df[stats_df['Times ≥ 63 km/h'] == 0]['Station'].tolist()
    stations_frequently_above = stats_df[stats_df['Times ≥ 63 km/h'] > total_time_points * 0.5]['Station'].tolist()
    
    if stations_below_threshold:
        report += f"**Stations that never exceeded 63 km/h threshold**: {', '.join(stations_below_threshold)}\n\n"
    
    if stations_frequently_above:
        report += f"**Stations that frequently exceeded 63 km/h threshold (>50% of time)**: {', '.join(stations_frequently_above)}\n\n"
    
    report += """
## Visualizations Generated

1. **wind_speed_time_series.png** - Time series showing wind speeds at all 8 stations over the Signal 8 period
2. **wind_speed_heatmap.png** - Heatmap visualization of wind speeds across stations and time
3. **wind_speed_comparison.png** - Box plot comparing wind speed distributions across stations
4. **threshold_analysis.png** - Analysis of how many stations exceeded thresholds over time
5. **summary_statistics_table.png** - Summary statistics table for all stations
6. **summary_statistics.csv** - Detailed statistics in CSV format

## Interpretation

This analysis provides insight into whether the issuance of Signal No. 8 was justified based on actual wind measurements at the 8 reference stations. The visualizations show:

- How wind speeds evolved over the typhoon period
- Which stations experienced the strongest winds
- Whether the HKO criterion (4+ stations with sustained winds ≥ 63 km/h) was met
- Spatial variation in wind speeds across Hong Kong

## Data Source
Wind data collected from Hong Kong Observatory during Typhoon Weipa
Period: July 19-21, 2025
"""
    
    output_file = os.path.join(OUTPUT_DIR, 'analysis_report.md')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"✓ Analysis report saved: {output_file}")


def main():
    """Main execution function"""
    print("\n" + "="*70)
    print("Typhoon Weipa Wind Speed Analysis")
    print("="*70 + "\n")
    
    # Load data
    print("Loading wind data...")
    df = load_wind_data()
    print(f"✓ Loaded {len(df)} total records")
    
    # Filter for Signal 8 period
    print(f"\nFiltering for Signal 8 period ({SIGNAL_8_START} to {SIGNAL_8_END})...")
    df_signal8 = filter_signal_8_period(df)
    print(f"✓ Filtered to {len(df_signal8)} records during Signal 8")
    
    # Filter for reference stations
    print("\nFiltering for 8 reference stations...")
    df_filtered = filter_reference_stations(df_signal8)
    print(f"✓ Filtered to {len(df_filtered)} records from reference stations")
    
    # Generate visualizations
    print("\nGenerating visualizations...")
    print("-" * 70)
    
    create_time_series_plot(df_filtered)
    create_heatmap(df_filtered)
    create_station_comparison(df_filtered)
    threshold_df = create_threshold_analysis(df_filtered)
    stats_df = create_summary_statistics(df_filtered)
    
    # Generate report
    print("\nGenerating analysis report...")
    generate_report(df_filtered, threshold_df, stats_df)
    
    print("\n" + "="*70)
    print("Analysis complete! All results saved to:")
    print(OUTPUT_DIR)
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
