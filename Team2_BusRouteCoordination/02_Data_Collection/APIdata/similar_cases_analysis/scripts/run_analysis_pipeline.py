#!/usr/bin/env python3
"""
Bus Route Analysis Pipeline
Comprehensive data collection and overlap analysis with logging
"""

import sys
import os
import logging
from datetime import datetime
import traceback

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from comprehensive_data_collector import BusDataCollector
from overlap_analyzer import OverlapAnalyzer

def setup_logging():
    """Setup comprehensive logging"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"analysis_pipeline_{timestamp}.log"
    
    # Create logs directory
    os.makedirs("logs", exist_ok=True)
    log_path = f"logs/{log_file}"
    
    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_path, encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    logger = logging.getLogger(__name__)
    logger.info("=" * 80)
    logger.info("🚌 BUS ROUTE ANALYSIS PIPELINE STARTED")
    logger.info("=" * 80)
    logger.info(f"📅 Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(f"📁 Log File: {log_path}")
    logger.info("=" * 80)
    
    return logger, log_path

def run_data_collection(logger):
    """Run comprehensive data collection"""
    logger.info("📊 PHASE 1: DATA COLLECTION")
    logger.info("-" * 50)
    
    try:
        logger.info("🚌 Initializing data collector...")
        collector = BusDataCollector()
        
        logger.info("📊 Starting comprehensive data collection...")
        results = collector.run_comprehensive_collection()
        
        logger.info("✅ Data collection completed successfully!")
        logger.info(f"📈 Collection Results:")
        logger.info(f"   - KMB Routes: {len(results['kmb_routes'])}")
        logger.info(f"   - KMB Stops: {len(results['kmb_stops'])}")
        logger.info(f"   - KMB Route-Stops: {len(results['kmb_route_stops'])}")
        logger.info(f"   - Citybus Routes: {len(results['citybus_routes'])}")
        
        return results
        
    except Exception as e:
        logger.error(f"❌ Data collection failed: {str(e)}")
        logger.error(f"📋 Traceback: {traceback.format_exc()}")
        return None

def run_overlap_analysis(logger, data_results):
    """Run overlap analysis"""
    logger.info("🔍 PHASE 2: OVERLAP ANALYSIS")
    logger.info("-" * 50)
    
    try:
        logger.info("🔍 Initializing overlap analyzer...")
        analyzer = OverlapAnalyzer()
        
        logger.info("📊 Starting comprehensive overlap analysis...")
        analysis_results = analyzer.run_comprehensive_analysis()
        
        logger.info("✅ Overlap analysis completed successfully!")
        logger.info(f"📈 Analysis Results:")
        logger.info(f"   - KMB-KMB Overlaps: {len(analysis_results['kmb_overlaps'])}")
        logger.info(f"   - KMB-Citybus Overlaps: {len(analysis_results['kmb_citybus_overlaps'])}")
        
        return analysis_results
        
    except Exception as e:
        logger.error(f"❌ Overlap analysis failed: {str(e)}")
        logger.error(f"📋 Traceback: {traceback.format_exc()}")
        return None

def generate_summary_report(logger, data_results, analysis_results):
    """Generate comprehensive summary report"""
    logger.info("📋 PHASE 3: SUMMARY REPORT")
    logger.info("-" * 50)
    
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = f"analysis/summary_report_{timestamp}.md"
        
        # Create analysis directory
        os.makedirs("analysis", exist_ok=True)
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("# Bus Route Analysis Summary Report\n\n")
            f.write(f"**Analysis Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("## 📊 Data Collection Summary\n\n")
            if data_results:
                f.write(f"- **KMB Routes:** {len(data_results['kmb_routes'])}\n")
                f.write(f"- **KMB Stops:** {len(data_results['kmb_stops'])}\n")
                f.write(f"- **KMB Route-Stops:** {len(data_results['kmb_route_stops'])}\n")
                f.write(f"- **Citybus Routes:** {len(data_results['citybus_routes'])}\n\n")
            
            f.write("## 🔍 Overlap Analysis Summary\n\n")
            if analysis_results:
                f.write(f"- **KMB-KMB Overlaps:** {len(analysis_results['kmb_overlaps'])}\n")
                f.write(f"- **KMB-Citybus Overlaps:** {len(analysis_results['kmb_citybus_overlaps'])}\n\n")
                
                # High priority overlaps
                high_priority = [o for o in analysis_results['kmb_overlaps'] if o.get('overlap_percentage', 0) >= 0.75]
                f.write(f"- **High Priority Routes:** {len(high_priority)}\n\n")
                
                if high_priority:
                    f.write("### 🎯 High Priority Overlaps\n\n")
                    for i, overlap in enumerate(high_priority[:10], 1):
                        f.write(f"{i}. **KMB {overlap['route1']} vs KMB {overlap['route2']}**\n")
                        f.write(f"   - Overlap: {overlap['overlap_count']} stops ({overlap['overlap_percentage']:.1%})\n")
                        f.write(f"   - Common Stops: {', '.join(overlap['common_stops'][:5])}{'...' if len(overlap['common_stops']) > 5 else ''}\n\n")
            
            f.write("## 📁 Generated Files\n\n")
            if data_results and 'csv_files' in data_results:
                f.write("### CSV Files\n")
                for name, path in data_results['csv_files'].items():
                    f.write(f"- **{name}:** {path}\n")
                f.write("\n")
            
            if analysis_results and 'csv_files' in analysis_results:
                f.write("### Analysis Files\n")
                for name, path in analysis_results['csv_files'].items():
                    f.write(f"- **{name}:** {path}\n")
                f.write("\n")
            
            f.write("## 🎯 Recommendations\n\n")
            f.write("1. **Immediate Action:** Implement coordination for high-priority overlapping routes\n")
            f.write("2. **Medium-term:** Develop comprehensive coordination framework\n")
            f.write("3. **Long-term:** System-wide coordination implementation\n\n")
            
            f.write("## 📊 Next Steps\n\n")
            f.write("1. Review generated CSV files for detailed analysis\n")
            f.write("2. Implement coordination for identified high-priority routes\n")
            f.write("3. Monitor coordination effectiveness\n")
            f.write("4. Expand coordination to additional routes\n\n")
        
        logger.info(f"✅ Summary report created: {report_file}")
        return report_file
        
    except Exception as e:
        logger.error(f"❌ Summary report generation failed: {str(e)}")
        logger.error(f"📋 Traceback: {traceback.format_exc()}")
        return None

def main():
    """Main analysis pipeline"""
    # Setup logging
    logger, log_path = setup_logging()
    
    try:
        # Phase 1: Data Collection
        logger.info("🚀 Starting analysis pipeline...")
        data_results = run_data_collection(logger)
        
        if not data_results:
            logger.error("❌ Pipeline failed at data collection phase")
            return False
        
        # Phase 2: Overlap Analysis
        analysis_results = run_overlap_analysis(logger, data_results)
        
        if not analysis_results:
            logger.error("❌ Pipeline failed at overlap analysis phase")
            return False
        
        # Phase 3: Summary Report
        summary_report = generate_summary_report(logger, data_results, analysis_results)
        
        # Final summary
        logger.info("🎉 ANALYSIS PIPELINE COMPLETED SUCCESSFULLY!")
        logger.info("=" * 80)
        logger.info(f"📊 Data Collection: ✅ Completed")
        logger.info(f"🔍 Overlap Analysis: ✅ Completed")
        logger.info(f"📋 Summary Report: ✅ Completed")
        logger.info(f"📁 Log File: {log_path}")
        if summary_report:
            logger.info(f"📄 Summary Report: {summary_report}")
        logger.info("=" * 80)
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Pipeline failed with error: {str(e)}")
        logger.error(f"📋 Traceback: {traceback.format_exc()}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
