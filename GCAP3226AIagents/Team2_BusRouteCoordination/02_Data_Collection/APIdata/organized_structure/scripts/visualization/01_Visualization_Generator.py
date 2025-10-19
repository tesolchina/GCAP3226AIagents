#!/usr/bin/env python3
"""
Team 2: Bus Route Coordination - Visualization Generator
Author: Team 2 - Bus Route Coordination
Date: 2024
Purpose: Generate visualizations for route overlap analysis and coordination patterns
"""

import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
import os
import logging
from typing import Dict, List, Tuple
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class VisualizationGenerator:
    """
    Generator for route overlap and coordination visualizations
    """
    
    def __init__(self, data_dir="data", results_dir="results"):
        self.data_dir = data_dir
        self.results_dir = results_dir
        self.ensure_directories()
        
        # Set visualization style
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
        
    def ensure_directories(self):
        """Create necessary directories"""
        directories = [
            f"{self.results_dir}/visualizations",
            f"{self.results_dir}/charts",
            f"{self.results_dir}/maps"
        ]
        
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
            logger.info(f"Created directory: {directory}")
    
    def load_overlap_data(self, filepath):
        """
        Load route overlap data from JSON file
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data
        except Exception as e:
            logger.error(f"Error loading overlap data: {str(e)}")
            return None
    
    def create_overlap_distribution_chart(self, overlap_results):
        """
        Create chart showing distribution of route overlaps
        """
        logger.info("Creating overlap distribution chart...")
        
        # Extract overlap counts
        overlap_counts = [result['overlap_count'] for result in overlap_results]
        
        # Create figure
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Histogram
        ax1.hist(overlap_counts, bins=20, alpha=0.7, color='skyblue', edgecolor='black')
        ax1.set_xlabel('Number of Overlapping Stops')
        ax1.set_ylabel('Number of Route Pairs')
        ax1.set_title('Distribution of Route Overlaps')
        ax1.grid(True, alpha=0.3)
        
        # Box plot
        ax2.boxplot(overlap_counts, vert=True)
        ax2.set_ylabel('Number of Overlapping Stops')
        ax2.set_title('Overlap Count Distribution')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Save chart
        chart_path = f"{self.results_dir}/charts/overlap_distribution_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        plt.savefig(chart_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        logger.info(f"Saved overlap distribution chart: {chart_path}")
        return chart_path
    
    def create_operator_combination_chart(self, overlap_results):
        """
        Create chart showing operator combinations
        """
        logger.info("Creating operator combination chart...")
        
        # Count operator combinations
        operator_combinations = {}
        for result in overlap_results:
            combo = f"{result['route1']['operator']}-{result['route2']['operator']}"
            operator_combinations[combo] = operator_combinations.get(combo, 0) + 1
        
        # Create pie chart
        fig, ax = plt.subplots(figsize=(10, 8))
        
        labels = list(operator_combinations.keys())
        sizes = list(operator_combinations.values())
        colors = plt.cm.Set3(np.linspace(0, 1, len(labels)))
        
        wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', 
                                         colors=colors, startangle=90)
        
        ax.set_title('Distribution of Route Overlaps by Operator Combination')
        
        # Save chart
        chart_path = f"{self.results_dir}/charts/operator_combinations_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        plt.savefig(chart_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        logger.info(f"Saved operator combination chart: {chart_path}")
        return chart_path
    
    def create_top_overlapping_routes_chart(self, overlap_results, top_n=20):
        """
        Create chart showing top overlapping routes
        """
        logger.info(f"Creating top {top_n} overlapping routes chart...")
        
        # Get top N overlapping routes
        top_routes = overlap_results[:top_n]
        
        # Prepare data
        route_labels = []
        overlap_counts = []
        
        for result in top_routes:
            label = f"{result['route1']['operator']} {result['route1']['route_id']} vs {result['route2']['operator']} {result['route2']['route_id']}"
            route_labels.append(label)
            overlap_counts.append(result['overlap_count'])
        
        # Create horizontal bar chart
        fig, ax = plt.subplots(figsize=(12, max(8, len(route_labels) * 0.4)))
        
        y_pos = np.arange(len(route_labels))
        bars = ax.barh(y_pos, overlap_counts, color='lightcoral', alpha=0.7)
        
        ax.set_yticks(y_pos)
        ax.set_yticklabels(route_labels, fontsize=8)
        ax.set_xlabel('Number of Overlapping Stops')
        ax.set_title(f'Top {top_n} Route Pairs by Overlap Count')
        ax.grid(True, alpha=0.3)
        
        # Add value labels on bars
        for i, (bar, count) in enumerate(zip(bars, overlap_counts)):
            ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2, 
                   str(count), va='center', fontsize=8)
        
        plt.tight_layout()
        
        # Save chart
        chart_path = f"{self.results_dir}/charts/top_overlapping_routes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        plt.savefig(chart_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        logger.info(f"Saved top overlapping routes chart: {chart_path}")
        return chart_path
    
    def create_coordination_effectiveness_chart(self, coordination_results):
        """
        Create chart showing coordination effectiveness
        """
        logger.info("Creating coordination effectiveness chart...")
        
        if not coordination_results:
            logger.warning("No coordination results available for visualization")
            return None
        
        # Extract effectiveness scores
        effectiveness_scores = [r['coordination_effectiveness']['score'] for r in coordination_results]
        
        # Create figure
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Histogram of effectiveness scores
        ax1.hist(effectiveness_scores, bins=15, alpha=0.7, color='lightgreen', edgecolor='black')
        ax1.set_xlabel('Coordination Effectiveness Score')
        ax1.set_ylabel('Number of Route Pairs')
        ax1.set_title('Distribution of Coordination Effectiveness')
        ax1.grid(True, alpha=0.3)
        
        # Effectiveness levels
        levels = ['High' if score > 0.7 else 'Medium' if score > 0.4 else 'Low' for score in effectiveness_scores]
        level_counts = {'High': levels.count('High'), 'Medium': levels.count('Medium'), 'Low': levels.count('Low')}
        
        ax2.bar(level_counts.keys(), level_counts.values(), color=['green', 'orange', 'red'], alpha=0.7)
        ax2.set_ylabel('Number of Route Pairs')
        ax2.set_title('Coordination Effectiveness Levels')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Save chart
        chart_path = f"{self.results_dir}/charts/coordination_effectiveness_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        plt.savefig(chart_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        logger.info(f"Saved coordination effectiveness chart: {chart_path}")
        return chart_path
    
    def create_interactive_overlap_map(self, overlap_results):
        """
        Create interactive map showing route overlaps
        """
        logger.info("Creating interactive overlap map...")
        
        # Prepare data for map
        map_data = []
        for result in overlap_results:
            map_data.append({
                'route1': f"{result['route1']['operator']} {result['route1']['route_id']}",
                'route2': f"{result['route2']['operator']} {result['route2']['route_id']}",
                'overlap_count': result['overlap_count'],
                'overlap_percentage': result['overlap_percentage']
            })
        
        # Create interactive scatter plot
        df = pd.DataFrame(map_data)
        
        fig = px.scatter(df, x='overlap_count', y='overlap_percentage',
                        size='overlap_count', color='overlap_count',
                        hover_data=['route1', 'route2'],
                        title='Route Overlap Analysis',
                        labels={'overlap_count': 'Number of Overlapping Stops',
                               'overlap_percentage': 'Overlap Percentage'})
        
        # Save interactive chart
        chart_path = f"{self.results_dir}/maps/interactive_overlap_map_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        fig.write_html(chart_path)
        
        logger.info(f"Saved interactive overlap map: {chart_path}")
        return chart_path
    
    def create_comprehensive_dashboard(self, overlap_results, coordination_results=None):
        """
        Create comprehensive dashboard with multiple visualizations
        """
        logger.info("Creating comprehensive dashboard...")
        
        # Create subplots
        fig = plt.figure(figsize=(20, 15))
        
        # 1. Overlap distribution
        ax1 = plt.subplot(2, 3, 1)
        overlap_counts = [result['overlap_count'] for result in overlap_results]
        ax1.hist(overlap_counts, bins=20, alpha=0.7, color='skyblue')
        ax1.set_title('Distribution of Route Overlaps')
        ax1.set_xlabel('Number of Overlapping Stops')
        ax1.set_ylabel('Number of Route Pairs')
        
        # 2. Operator combinations
        ax2 = plt.subplot(2, 3, 2)
        operator_combinations = {}
        for result in overlap_results:
            combo = f"{result['route1']['operator']}-{result['route2']['operator']}"
            operator_combinations[combo] = operator_combinations.get(combo, 0) + 1
        
        ax2.pie(operator_combinations.values(), labels=operator_combinations.keys(), autopct='%1.1f%%')
        ax2.set_title('Operator Combinations')
        
        # 3. Top overlapping routes
        ax3 = plt.subplot(2, 3, 3)
        top_10 = overlap_results[:10]
        route_labels = [f"{r['route1']['operator']} {r['route1']['route_id']}" for r in top_10]
        overlap_counts_top = [r['overlap_count'] for r in top_10]
        
        ax3.barh(range(len(route_labels)), overlap_counts_top, color='lightcoral')
        ax3.set_yticks(range(len(route_labels)))
        ax3.set_yticklabels(route_labels, fontsize=8)
        ax3.set_title('Top 10 Overlapping Routes')
        ax3.set_xlabel('Overlap Count')
        
        # 4. Overlap percentage distribution
        ax4 = plt.subplot(2, 3, 4)
        overlap_percentages = [result['overlap_percentage'] for result in overlap_results]
        ax4.hist(overlap_percentages, bins=20, alpha=0.7, color='lightgreen')
        ax4.set_title('Overlap Percentage Distribution')
        ax4.set_xlabel('Overlap Percentage')
        ax4.set_ylabel('Number of Route Pairs')
        
        # 5. Coordination effectiveness (if available)
        if coordination_results:
            ax5 = plt.subplot(2, 3, 5)
            effectiveness_scores = [r['coordination_effectiveness']['score'] for r in coordination_results]
            ax5.hist(effectiveness_scores, bins=15, alpha=0.7, color='gold')
            ax5.set_title('Coordination Effectiveness')
            ax5.set_xlabel('Effectiveness Score')
            ax5.set_ylabel('Number of Route Pairs')
        else:
            ax5 = plt.subplot(2, 3, 5)
            ax5.text(0.5, 0.5, 'Coordination Analysis\nNot Available', 
                    ha='center', va='center', transform=ax5.transAxes)
            ax5.set_title('Coordination Effectiveness')
        
        # 6. Summary statistics
        ax6 = plt.subplot(2, 3, 6)
        ax6.axis('off')
        
        summary_text = f"""
        Analysis Summary:
        
        Total Route Pairs: {len(overlap_results)}
        Average Overlap: {np.mean(overlap_counts):.1f} stops
        Max Overlap: {max(overlap_counts)} stops
        Min Overlap: {min(overlap_counts)} stops
        
        High Overlap (10+ stops): {len([c for c in overlap_counts if c >= 10])}
        Medium Overlap (5-9 stops): {len([c for c in overlap_counts if 5 <= c < 10])}
        Low Overlap (3-4 stops): {len([c for c in overlap_counts if 3 <= c < 5])}
        """
        
        ax6.text(0.1, 0.9, summary_text, transform=ax6.transAxes, 
                fontsize=10, verticalalignment='top', fontfamily='monospace')
        
        plt.tight_layout()
        
        # Save dashboard
        dashboard_path = f"{self.results_dir}/visualizations/comprehensive_dashboard_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        plt.savefig(dashboard_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        logger.info(f"Saved comprehensive dashboard: {dashboard_path}")
        return dashboard_path
    
    def generate_all_visualizations(self, overlap_data_path, coordination_data_path=None):
        """
        Generate all visualizations from data files
        """
        logger.info("Generating all visualizations...")
        
        # Load overlap data
        overlap_results = self.load_overlap_data(overlap_data_path)
        if not overlap_results:
            logger.error("Failed to load overlap data")
            return
        
        # Load coordination data if available
        coordination_results = None
        if coordination_data_path:
            coordination_results = self.load_overlap_data(coordination_data_path)
        
        # Generate visualizations
        visualizations = {}
        
        # 1. Overlap distribution chart
        visualizations['overlap_distribution'] = self.create_overlap_distribution_chart(overlap_results)
        
        # 2. Operator combination chart
        visualizations['operator_combinations'] = self.create_operator_combination_chart(overlap_results)
        
        # 3. Top overlapping routes chart
        visualizations['top_overlapping_routes'] = self.create_top_overlapping_routes_chart(overlap_results)
        
        # 4. Interactive overlap map
        visualizations['interactive_map'] = self.create_interactive_overlap_map(overlap_results)
        
        # 5. Coordination effectiveness chart (if data available)
        if coordination_results:
            visualizations['coordination_effectiveness'] = self.create_coordination_effectiveness_chart(coordination_results)
        
        # 6. Comprehensive dashboard
        visualizations['dashboard'] = self.create_comprehensive_dashboard(overlap_results, coordination_results)
        
        # Save visualization summary
        summary = {
            'generated_at': datetime.now().isoformat(),
            'visualizations': visualizations,
            'data_summary': {
                'total_overlap_pairs': len(overlap_results),
                'coordination_analysis_available': coordination_results is not None
            }
        }
        
        summary_path = f"{self.results_dir}/visualizations/visualization_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(summary_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Generated {len(visualizations)} visualizations")
        logger.info(f"Visualization summary saved: {summary_path}")
        
        return visualizations

def main():
    """
    Main function to generate visualizations
    """
    generator = VisualizationGenerator()
    
    # Example usage - you would replace these with actual data file paths
    overlap_data_path = "data/overlap_analysis/route_overlaps_20241201_120000.json"
    coordination_data_path = "data/coordination_analysis/coordination_patterns_20241201_120000.json"
    
    # Generate all visualizations
    visualizations = generator.generate_all_visualizations(overlap_data_path, coordination_data_path)
    
    print(f"\n=== VISUALIZATIONS GENERATED ===")
    for name, path in visualizations.items():
        print(f"{name}: {path}")

if __name__ == "__main__":
    main()
