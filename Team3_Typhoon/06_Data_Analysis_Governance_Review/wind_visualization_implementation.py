#!/usr/bin/env python3
"""
Wind Strength Data Visualization Implementation
Team3_Typhoon - Signal 8 Wind Data Visualization

This script implements comprehensive visualization techniques for wind strength
data changes over time during Signal 8 periods.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# Set up plotting style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class WindDataVisualizer:
    """
    Comprehensive wind data visualization class for Signal 8 analysis
    """
    
    def __init__(self):
        self.signal8_thresholds = {
            'lower': 63,  # km/h
            'upper': 117  # km/h
        }
        self.station_colors = {
            'HKIA': '#1f77b4',
            'Chek Lap Kok': '#ff7f0e', 
            'Tsing Yi': '#2ca02c',
            'Tate\'s Cairn': '#d62728',
            'Tai Mo Shan': '#9467bd'
        }
        self.signal_colors = {
            'below_threshold': '#2E8B57',
            'approaching_threshold': '#FFD700',
            'above_threshold': '#DC143C',
            'signal_8_active': '#FF6347'
        }
    
    def create_time_series_plot(self, data, title="Signal 8 Wind Speed Timeline"):
        """
        Create comprehensive time series plot for wind speed analysis
        
        Args:
            data (pd.DataFrame): Wind data with columns ['timestamp', 'wind_speed', 'station']
            title (str): Plot title
            
        Returns:
            matplotlib.figure.Figure: Time series plot
        """
        fig, ax = plt.subplots(figsize=(15, 8))
        
        # Plot wind speed over time for each station
        for station in data['station'].unique():
            station_data = data[data['station'] == station]
            ax.plot(station_data['timestamp'], station_data['wind_speed'],
                   label=f'{station}', linewidth=2, 
                   color=self.station_colors.get(station, '#000000'))
        
        # Add Signal 8 thresholds
        ax.axhline(y=self.signal8_thresholds['lower'], color='orange', 
                   linestyle='--', alpha=0.7, label='Signal 8 Lower Threshold (63 km/h)')
        ax.axhline(y=self.signal8_thresholds['upper'], color='red', 
                   linestyle='--', alpha=0.7, label='Signal 8 Upper Threshold (117 km/h)')
        
        # Highlight Signal 8 active periods (if available in data)
        if 'signal8_active' in data.columns:
            signal8_periods = data[data['signal8_active'] == True]
            if not signal8_periods.empty:
                ax.scatter(signal8_periods['timestamp'], signal8_periods['wind_speed'],
                          color='red', s=50, alpha=0.7, label='Signal 8 Active Periods')
        
        ax.set_xlabel('Time', fontsize=12)
        ax.set_ylabel('Wind Speed (km/h)', fontsize=12)
        ax.set_title(title, fontsize=14, fontweight='bold')
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        return fig
    
    def create_threshold_analysis(self, data, title="Signal 8 Threshold Compliance"):
        """
        Create threshold compliance analysis visualization
        
        Args:
            data (pd.DataFrame): Wind data
            title (str): Plot title
            
        Returns:
            matplotlib.figure.Figure: Threshold analysis plot
        """
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 12))
        
        # Wind speed over time with threshold zones
        for station in data['station'].unique():
            station_data = data[data['station'] == station]
            ax1.plot(station_data['timestamp'], station_data['wind_speed'],
                    label=f'{station}', linewidth=2,
                    color=self.station_colors.get(station, '#000000'))
        
        # Add threshold zones
        ax1.axhspan(0, self.signal8_thresholds['lower'], 
                   color='green', alpha=0.2, label='Below Signal 8 Threshold')
        ax1.axhspan(self.signal8_thresholds['lower'], self.signal8_thresholds['upper'],
                   color='yellow', alpha=0.2, label='Signal 8 Range')
        ax1.axhspan(self.signal8_thresholds['upper'], data['wind_speed'].max() + 10,
                   color='red', alpha=0.2, label='Above Signal 8 Threshold')
        
        ax1.set_ylabel('Wind Speed (km/h)')
        ax1.set_title('Wind Speed vs. Signal 8 Thresholds')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Threshold compliance histogram
        wind_speeds = data['wind_speed'].values
        below_threshold = wind_speeds < self.signal8_thresholds['lower']
        in_range = (wind_speeds >= self.signal8_thresholds['lower']) & (wind_speeds <= self.signal8_thresholds['upper'])
        above_threshold = wind_speeds > self.signal8_thresholds['upper']
        
        categories = ['Below Threshold', 'In Signal 8 Range', 'Above Threshold']
        counts = [np.sum(below_threshold), np.sum(in_range), np.sum(above_threshold)]
        colors = ['green', 'yellow', 'red']
        
        ax2.bar(categories, counts, color=colors, alpha=0.7)
        ax2.set_ylabel('Number of Measurements')
        ax2.set_title('Signal 8 Threshold Compliance Distribution')
        ax2.grid(True, alpha=0.3)
        
        # Add percentage annotations
        total = len(wind_speeds)
        for i, count in enumerate(counts):
            percentage = (count / total) * 100
            ax2.text(i, count + 0.5, f'{percentage:.1f}%', 
                    ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        return fig
    
    def create_multi_station_comparison(self, data, title="Multi-Station Wind Speed Comparison"):
        """
        Create multi-station wind speed comparison visualization
        
        Args:
            data (pd.DataFrame): Wind data
            title (str): Plot title
            
        Returns:
            matplotlib.figure.Figure: Multi-station comparison plot
        """
        stations = data['station'].unique()
        n_stations = len(stations)
        
        # Create subplot grid
        n_cols = 2
        n_rows = (n_stations + 1) // 2
        
        fig, axes = plt.subplots(n_rows, n_cols, figsize=(16, 4 * n_rows))
        if n_rows == 1:
            axes = axes.reshape(1, -1)
        
        for i, station in enumerate(stations):
            row = i // n_cols
            col = i % n_cols
            ax = axes[row, col]
            
            station_data = data[data['station'] == station]
            
            # Plot wind speed
            ax.plot(station_data['timestamp'], station_data['wind_speed'],
                   label=f'{station} Wind Speed', linewidth=2,
                   color=self.station_colors.get(station, '#000000'))
            
            # Add thresholds
            ax.axhline(y=self.signal8_thresholds['lower'], color='orange', 
                      linestyle='--', alpha=0.7, label='Signal 8 Lower Threshold')
            ax.axhline(y=self.signal8_thresholds['upper'], color='red', 
                      linestyle='--', alpha=0.7, label='Signal 8 Upper Threshold')
            
            ax.set_title(f'{station} Wind Speed Analysis')
            ax.set_ylabel('Wind Speed (km/h)')
            ax.grid(True, alpha=0.3)
            ax.legend()
        
        # Hide empty subplots
        for i in range(n_stations, n_rows * n_cols):
            row = i // n_cols
            col = i % n_cols
            axes[row, col].set_visible(False)
        
        plt.suptitle(title, fontsize=16, fontweight='bold')
        plt.tight_layout()
        return fig
    
    def create_wind_heatmap(self, data, title="Wind Speed Heatmap by Station and Time"):
        """
        Create wind speed heatmap visualization
        
        Args:
            data (pd.DataFrame): Wind data
            title (str): Plot title
            
        Returns:
            matplotlib.figure.Figure: Wind speed heatmap
        """
        # Pivot data for heatmap
        pivot_data = data.pivot_table(
            values='wind_speed', 
            index='station', 
            columns='timestamp', 
            aggfunc='mean'
        )
        
        fig, ax = plt.subplots(figsize=(20, 8))
        
        # Create heatmap
        sns.heatmap(pivot_data, cmap='YlOrRd', annot=False, 
                   cbar_kws={'label': 'Wind Speed (km/h)'}, ax=ax)
        
        ax.set_title(title, fontsize=14, fontweight='bold')
        ax.set_xlabel('Time')
        ax.set_ylabel('Weather Station')
        
        plt.tight_layout()
        return fig
    
    def create_regional_comparison(self, hk_data, macau_data, title="Hong Kong vs. Macau Wind Comparison"):
        """
        Create regional comparative analysis visualization
        
        Args:
            hk_data (pd.DataFrame): Hong Kong wind data
            macau_data (pd.DataFrame): Macau wind data
            title (str): Plot title
            
        Returns:
            matplotlib.figure.Figure: Regional comparison plot
        """
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 12))
        
        # Hong Kong data
        if not hk_data.empty:
            ax1.plot(hk_data['timestamp'], hk_data['wind_speed'],
                    label='Hong Kong Wind Speed', color='blue', linewidth=2)
            ax1.axhline(y=self.signal8_thresholds['lower'], color='orange', 
                       linestyle='--', alpha=0.7, label='Signal 8 Threshold')
            ax1.set_title('Hong Kong Wind Speed During Typhoon Event')
            ax1.set_ylabel('Wind Speed (km/h)')
            ax1.grid(True, alpha=0.3)
            ax1.legend()
        
        # Macau data
        if not macau_data.empty:
            ax2.plot(macau_data['timestamp'], macau_data['wind_speed'],
                    label='Macau Wind Speed', color='red', linewidth=2)
            ax2.axhline(y=self.signal8_thresholds['lower'], color='orange', 
                       linestyle='--', alpha=0.7, label='Signal 8 Threshold')
            ax2.set_title('Macau Wind Speed During Typhoon Event')
            ax2.set_xlabel('Time')
            ax2.set_ylabel('Wind Speed (km/h)')
            ax2.grid(True, alpha=0.3)
            ax2.legend()
        
        plt.suptitle(title, fontsize=16, fontweight='bold')
        plt.tight_layout()
        return fig
    
    def create_interactive_dashboard(self, data):
        """
        Create interactive Plotly dashboard
        
        Args:
            data (pd.DataFrame): Wind data
            
        Returns:
            plotly.graph_objects.Figure: Interactive dashboard
        """
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Wind Speed Timeline', 'Threshold Analysis', 
                          'Station Comparison', 'Wind Distribution'),
            specs=[[{"secondary_y": False}, {"secondary_y": False}],
                   [{"secondary_y": False}, {"secondary_y": False}]]
        )
        
        # Wind speed timeline
        for station in data['station'].unique():
            station_data = data[data['station'] == station]
            fig.add_trace(
                go.Scatter(x=station_data['timestamp'], y=station_data['wind_speed'],
                          mode='lines', name=station, line=dict(width=2)),
                row=1, col=1
            )
        
        # Add threshold lines
        fig.add_hline(y=self.signal8_thresholds['lower'], line_dash="dash", 
                     line_color="orange", row=1, col=1)
        fig.add_hline(y=self.signal8_thresholds['upper'], line_dash="dash", 
                     line_color="red", row=1, col=1)
        
        # Threshold analysis
        wind_speeds = data['wind_speed'].values
        below_threshold = np.sum(wind_speeds < self.signal8_thresholds['lower'])
        in_range = np.sum((wind_speeds >= self.signal8_thresholds['lower']) & 
                         (wind_speeds <= self.signal8_thresholds['upper']))
        above_threshold = np.sum(wind_speeds > self.signal8_thresholds['upper'])
        
        fig.add_trace(
            go.Bar(x=['Below Threshold', 'In Range', 'Above Threshold'],
                  y=[below_threshold, in_range, above_threshold],
                  marker_color=['green', 'yellow', 'red']),
            row=1, col=2
        )
        
        # Station comparison box plot
        for station in data['station'].unique():
            station_data = data[data['station'] == station]
            fig.add_trace(
                go.Box(y=station_data['wind_speed'], name=station),
                row=2, col=1
            )
        
        # Wind speed distribution
        fig.add_trace(
            go.Histogram(x=wind_speeds, nbinsx=20, name='Wind Speed Distribution'),
            row=2, col=2
        )
        
        fig.update_layout(
            title_text="Signal 8 Wind Data Analysis Dashboard",
            showlegend=True,
            height=800
        )
        
        return fig
    
    def generate_sample_data(self, n_hours=24, n_stations=4):
        """
        Generate sample wind data for demonstration
        
        Args:
            n_hours (int): Number of hours of data to generate
            n_stations (int): Number of weather stations
            
        Returns:
            pd.DataFrame: Sample wind data
        """
        # Generate time series
        timestamps = pd.date_range(start='2024-01-01', periods=n_hours*6, freq='10min')
        
        stations = ['HKIA', 'Chek Lap Kok', 'Tsing Yi', 'Tate\'s Cairn'][:n_stations]
        
        data = []
        for station in stations:
            # Generate realistic wind speed data
            base_wind = np.random.normal(30, 10, len(timestamps))
            
            # Add Signal 8 period (higher winds)
            signal8_start = len(timestamps) // 3
            signal8_end = 2 * len(timestamps) // 3
            base_wind[signal8_start:signal8_end] += np.random.normal(40, 15, signal8_end - signal8_start)
            
            # Ensure positive values
            base_wind = np.maximum(base_wind, 0)
            
            for i, timestamp in enumerate(timestamps):
                data.append({
                    'timestamp': timestamp,
                    'station': station,
                    'wind_speed': base_wind[i],
                    'wind_gust': base_wind[i] * np.random.uniform(1.2, 1.8),
                    'wind_direction': np.random.uniform(0, 360),
                    'signal8_active': signal8_start <= i <= signal8_end
                })
        
        return pd.DataFrame(data)

def main():
    """
    Main function to demonstrate wind data visualization
    """
    print("🌪️ Signal 8 Wind Data Visualization Demo")
    print("=" * 50)
    
    # Initialize visualizer
    visualizer = WindDataVisualizer()
    
    # Generate sample data
    print("📊 Generating sample wind data...")
    sample_data = visualizer.generate_sample_data(n_hours=24, n_stations=4)
    print(f"✅ Generated {len(sample_data)} data points")
    
    # Create visualizations
    print("\n📈 Creating visualizations...")
    
    # 1. Time series plot
    print("1. Creating time series plot...")
    fig1 = visualizer.create_time_series_plot(sample_data)
    fig1.savefig('signal8_timeline.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: signal8_timeline.png")
    
    # 2. Threshold analysis
    print("2. Creating threshold analysis...")
    fig2 = visualizer.create_threshold_analysis(sample_data)
    fig2.savefig('signal8_threshold_analysis.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: signal8_threshold_analysis.png")
    
    # 3. Multi-station comparison
    print("3. Creating multi-station comparison...")
    fig3 = visualizer.create_multi_station_comparison(sample_data)
    fig3.savefig('signal8_multi_station.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: signal8_multi_station.png")
    
    # 4. Wind heatmap
    print("4. Creating wind heatmap...")
    fig4 = visualizer.create_wind_heatmap(sample_data)
    fig4.savefig('signal8_heatmap.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: signal8_heatmap.png")
    
    # 5. Interactive dashboard
    print("5. Creating interactive dashboard...")
    fig5 = visualizer.create_interactive_dashboard(sample_data)
    fig5.write_html('signal8_dashboard.html')
    print("✅ Saved: signal8_dashboard.html")
    
    # 6. Regional comparison (using sample data)
    print("6. Creating regional comparison...")
    hk_data = sample_data[sample_data['station'].isin(['HKIA', 'Chek Lap Kok'])]
    macau_data = sample_data[sample_data['station'].isin(['Tsing Yi', 'Tate\'s Cairn'])]
    fig6 = visualizer.create_regional_comparison(hk_data, macau_data)
    fig6.savefig('signal8_regional_comparison.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: signal8_regional_comparison.png")
    
    print("\n🎉 Visualization demo completed!")
    print("📁 Generated files:")
    print("   - signal8_timeline.png")
    print("   - signal8_threshold_analysis.png")
    print("   - signal8_multi_station.png")
    print("   - signal8_heatmap.png")
    print("   - signal8_dashboard.html")
    print("   - signal8_regional_comparison.png")

if __name__ == "__main__":
    main()
