#!/usr/bin/env python3
"""
Team 2: Bus Route Coordination - Main Analysis Runner
Author: Team 2 - Bus Route Coordination
Date: 2024
Purpose: Main script to run complete similar cases analysis
"""

import os
import sys
import json
import logging
from datetime import datetime
from pathlib import Path

# Add current directory to path for imports
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

from route_overlap_analyzer import RouteOverlapAnalyzer
from coordination_analyzer import CoordinationAnalyzer
from visualization_generator import VisualizationGenerator

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SimilarCasesAnalysisRunner:
    """
    Main runner for similar cases analysis
    """
    
    def __init__(self):
        self.data_dir = "data"
        self.results_dir = "results"
        self.ensure_directories()
        
    def ensure_directories(self):
        """Create necessary directories"""
        directories = [
            self.data_dir,
            self.results_dir,
            f"{self.results_dir}/reports",
            f"{self.results_dir}/logs"
        ]
        
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
            logger.info(f"Created directory: {directory}")
    
    def run_complete_analysis(self, min_overlap=5, coordination_analysis_hours=1):
        """
        Run complete similar cases analysis
        """
        logger.info("=== STARTING COMPLETE SIMILAR CASES ANALYSIS ===")
        start_time = datetime.now()
        
        analysis_results = {
            'analysis_start_time': start_time.isoformat(),
            'parameters': {
                'min_overlap': min_overlap,
                'coordination_analysis_hours': coordination_analysis_hours
            }
        }
        
        try:
            # Step 1: Route Overlap Analysis
            logger.info("Step 1: Running route overlap analysis...")
            overlap_analyzer = RouteOverlapAnalyzer(self.data_dir, self.results_dir)
            overlap_results = overlap_analyzer.run_complete_analysis(min_overlap)
            
            analysis_results['overlap_analysis'] = {
                'status': 'completed',
                'total_overlapping_pairs': len(overlap_results['overlap_results']),
                'high_overlap_routes': len(overlap_results['categories']['high_overlap']),
                'medium_overlap_routes': len(overlap_results['categories']['medium_overlap']),
                'low_overlap_routes': len(overlap_results['categories']['low_overlap'])
            }
            
            # Step 2: Coordination Analysis (for top overlapping routes)
            logger.info("Step 2: Running coordination analysis...")
            coordination_analyzer = CoordinationAnalyzer(self.data_dir, self.results_dir)
            
            # Select top 5 overlapping route pairs for coordination analysis
            top_route_pairs = []
            for result in overlap_results['overlap_results'][:5]:
                route1_info = {
                    'operator': result['route1']['operator'],
                    'route_id': result['route1']['route_id'],
                    'route_name': result['route1']['route_name']
                }
                route2_info = {
                    'operator': result['route2']['operator'],
                    'route_id': result['route2']['route_id'],
                    'route_name': result['route2']['route_name']
                }
                top_route_pairs.append((route1_info, route2_info))
            
            coordination_results = coordination_analyzer.analyze_multiple_route_pairs(
                top_route_pairs, duration_hours=coordination_analysis_hours
            )
            
            analysis_results['coordination_analysis'] = {
                'status': 'completed',
                'pairs_analyzed': len(top_route_pairs),
                'coordination_results': coordination_results
            }
            
            # Step 3: Visualization Generation
            logger.info("Step 3: Generating visualizations...")
            visualization_generator = VisualizationGenerator(self.data_dir, self.results_dir)
            
            # Find the most recent overlap data file
            overlap_data_files = list(Path(self.data_dir).glob("overlap_analysis/route_overlaps_*.json"))
            if overlap_data_files:
                latest_overlap_file = max(overlap_data_files, key=os.path.getctime)
                visualizations = visualization_generator.generate_all_visualizations(str(latest_overlap_file))
                
                analysis_results['visualizations'] = {
                    'status': 'completed',
                    'generated_charts': len(visualizations)
                }
            else:
                logger.warning("No overlap data files found for visualization")
                analysis_results['visualizations'] = {'status': 'failed', 'reason': 'No data files found'}
            
            # Step 4: Generate Final Report
            logger.info("Step 4: Generating final report...")
            final_report = self.generate_final_report(analysis_results, overlap_results, coordination_results)
            
            analysis_results['final_report'] = final_report
            analysis_results['analysis_end_time'] = datetime.now().isoformat()
            analysis_results['analysis_duration'] = str(datetime.now() - start_time)
            
            # Save complete analysis results
            self.save_analysis_results(analysis_results)
            
            logger.info("=== ANALYSIS COMPLETE ===")
            self.print_summary(analysis_results)
            
            return analysis_results
            
        except Exception as e:
            logger.error(f"Analysis failed: {str(e)}")
            analysis_results['error'] = str(e)
            analysis_results['analysis_end_time'] = datetime.now().isoformat()
            return analysis_results
    
    def generate_final_report(self, analysis_results, overlap_results, coordination_results):
        """
        Generate comprehensive final report
        """
        report = {
            'report_timestamp': datetime.now().isoformat(),
            'executive_summary': {
                'total_route_pairs_analyzed': len(overlap_results['overlap_results']),
                'high_priority_coordination_opportunities': len(overlap_results['categories']['high_overlap']),
                'coordination_analysis_completed': coordination_results is not None
            },
            'key_findings': {
                'top_overlapping_routes': overlap_results['overlap_results'][:10],
                'coordination_effectiveness': coordination_results['comparative_analysis'] if coordination_results else None
            },
            'recommendations': {
                'immediate_actions': [
                    f"Focus on {len(overlap_results['categories']['high_overlap'])} high-overlap route pairs for coordination",
                    "Implement coordination analysis for top overlapping routes",
                    "Develop coordination strategies for medium-overlap routes"
                ],
                'long_term_actions': [
                    "Establish systematic coordination framework",
                    "Monitor coordination effectiveness over time",
                    "Develop policy recommendations based on analysis results"
                ]
            },
            'data_quality': {
                'overlap_analysis_completed': analysis_results['overlap_analysis']['status'] == 'completed',
                'coordination_analysis_completed': analysis_results['coordination_analysis']['status'] == 'completed',
                'visualizations_generated': analysis_results['visualizations']['status'] == 'completed'
            }
        }
        
        # Save final report
        report_path = f"{self.results_dir}/reports/final_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Final report saved: {report_path}")
        return report
    
    def save_analysis_results(self, analysis_results):
        """
        Save complete analysis results
        """
        results_path = f"{self.results_dir}/reports/complete_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(results_path, 'w', encoding='utf-8') as f:
            json.dump(analysis_results, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Complete analysis results saved: {results_path}")
    
    def print_summary(self, analysis_results):
        """
        Print analysis summary
        """
        print("\n" + "="*60)
        print("SIMILAR CASES ANALYSIS - COMPLETE")
        print("="*60)
        
        if 'overlap_analysis' in analysis_results:
            overlap = analysis_results['overlap_analysis']
            print(f"Route Overlap Analysis: {overlap['status']}")
            print(f"  - Total overlapping pairs: {overlap['total_overlapping_pairs']}")
            print(f"  - High overlap routes (10+ stops): {overlap['high_overlap_routes']}")
            print(f"  - Medium overlap routes (5-9 stops): {overlap['medium_overlap_routes']}")
            print(f"  - Low overlap routes (3-4 stops): {overlap['low_overlap_routes']}")
        
        if 'coordination_analysis' in analysis_results:
            coord = analysis_results['coordination_analysis']
            print(f"Coordination Analysis: {coord['status']}")
            print(f"  - Route pairs analyzed: {coord['pairs_analyzed']}")
        
        if 'visualizations' in analysis_results:
            viz = analysis_results['visualizations']
            print(f"Visualizations: {viz['status']}")
            if viz['status'] == 'completed':
                print(f"  - Charts generated: {viz['generated_charts']}")
        
        if 'analysis_duration' in analysis_results:
            print(f"Total analysis time: {analysis_results['analysis_duration']}")
        
        print("="*60)

def main():
    """
    Main function to run similar cases analysis
    """
    runner = SimilarCasesAnalysisRunner()
    
    # Run complete analysis
    # Parameters:
    # - min_overlap: Minimum number of overlapping stops to consider (default: 5)
    # - coordination_analysis_hours: Hours to collect coordination data (default: 1)
    results = runner.run_complete_analysis(min_overlap=5, coordination_analysis_hours=1)
    
    if 'error' in results:
        print(f"\nAnalysis failed: {results['error']}")
        sys.exit(1)
    else:
        print("\nAnalysis completed successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
