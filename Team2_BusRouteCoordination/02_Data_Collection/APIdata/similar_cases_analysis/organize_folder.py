#!/usr/bin/env python3
"""
Folder Organization Script
Organizes the messy similar_cases_analysis folder into a clean structure
"""

import os
import shutil
from datetime import datetime

def create_folders():
    """Create organized folder structure"""
    folders = [
        "01_ARCHIVE_OLD_FILES",
        "02_CURRENT_ANALYSIS", 
        "03_SCRIPTS",
        "04_DATA",
        "05_REPORTS",
        "06_RESULTS"
    ]
    
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"✅ Created folder: {folder}")

def move_files():
    """Move files to appropriate folders"""
    
    # Files to archive (old/duplicate files)
    archive_files = [
        "ANALYSIS_LOG.md",
        "ANALYSIS_RESULTS.md", 
        "ANALYSIS_STATUS_REPORT.md",
        "COMPLETE_ANALYSIS_SUMMARY.md",
        "COMPREHENSIVE_OVERLAP_ANALYSIS.md",
        "DATA_ACCESS_REPORT.md",
        "DATA_UPDATE_REPORT.md",
        "DIGITAL_POLICY_ENQUIRY_EMAIL.md",
        "EXECUTION_LOG.md",
        "EXECUTION_PLAN.md",
        "KMB_272A_272K_ANALYSIS.md",
        "KMB_DETAILED_OVERLAP_ANALYSIS.md",
        "KMB_OVERLAP_ANALYSIS_REPORT.md",
        "KMB_OVERLAP_SUMMARY_REPORT.md",
        "README.md",
        "requirements.txt"
    ]
    
    # Current analysis files (keep most recent)
    current_files = [
        "FINAL_SUMMARY.md",
        "EXECUTION_REPORT.md"
    ]
    
    # Scripts
    script_files = [
        "comprehensive_data_collector.py",
        "overlap_analyzer.py", 
        "run_analysis_pipeline.py",
        "test_api_access.py",
        "simple_api_test.py",
        "execute_analysis.py",
        "route_overlap_analyzer.py",
        "coordination_analyzer.py",
        "visualization_generator.py",
        "overlap_analysis_runner.py",
        "demo_analysis.py",
        "get_272A_272K_data.py",
        "fetch_citybus_routes_company.py",
        "test_citybus_api.py"
    ]
    
    # Data files
    data_files = [
        "COMPREHENSIVE_OVERLAP_RESULTS.csv",
        "KMB_272A_272K_DETAILED_ANALYSIS.csv",
        "KMB_Coordination_Summary.csv",
        "KMB_Detailed_Overlap_Analysis.csv",
        "KMB_Route_Overlap_Analysis.csv"
    ]
    
    # Move files to appropriate folders
    print("\n📁 Moving files to organized folders...")
    
    # Archive old files
    for file in archive_files:
        if os.path.exists(file):
            shutil.move(file, f"01_ARCHIVE_OLD_FILES/{file}")
            print(f"   📦 Archived: {file}")
    
    # Move current analysis files
    for file in current_files:
        if os.path.exists(file):
            shutil.move(file, f"02_CURRENT_ANALYSIS/{file}")
            print(f"   📊 Current: {file}")
    
    # Move scripts
    for file in script_files:
        if os.path.exists(file):
            shutil.move(file, f"03_SCRIPTS/{file}")
            print(f"   🐍 Script: {file}")
    
    # Move data files
    for file in data_files:
        if os.path.exists(file):
            shutil.move(file, f"04_DATA/{file}")
            print(f"   📊 Data: {file}")
    
    # Move data folder
    if os.path.exists("data"):
        shutil.move("data", "04_DATA/data")
        print(f"   📁 Moved: data/ folder")
    
    # Move scripts folder
    if os.path.exists("scripts"):
        # Move individual script files first
        for root, dirs, files in os.walk("scripts"):
            for file in files:
                if file.endswith('.py'):
                    src = os.path.join(root, file)
                    dst = f"03_SCRIPTS/{file}"
                    if os.path.exists(src) and not os.path.exists(dst):
                        shutil.move(src, dst)
                        print(f"   🐍 Script: {file}")
        
        # Move remaining script folders
        for item in os.listdir("scripts"):
            if os.path.isdir(f"scripts/{item}") and item != "__pycache__":
                shutil.move(f"scripts/{item}", f"03_SCRIPTS/{item}")
                print(f"   📁 Moved: scripts/{item}")
    
    # Move results folder
    if os.path.exists("results"):
        shutil.move("results", "06_RESULTS/results")
        print(f"   📁 Moved: results/ folder")

def create_index_files():
    """Create index files for each folder"""
    
    # Create main index
    with open("INDEX.md", "w", encoding="utf-8") as f:
        f.write("# Bus Route Analysis - Organized Structure\n\n")
        f.write("## 📁 **Folder Organization**\n\n")
        f.write("### **01_ARCHIVE_OLD_FILES/**\n")
        f.write("- Old analysis files\n")
        f.write("- Duplicate reports\n")
        f.write("- Outdated documentation\n\n")
        f.write("### **02_CURRENT_ANALYSIS/**\n")
        f.write("- Most recent analysis results\n")
        f.write("- Final summary and execution report\n")
        f.write("- Current coordination recommendations\n\n")
        f.write("### **03_SCRIPTS/**\n")
        f.write("- All Python scripts\n")
        f.write("- Data collection scripts\n")
        f.write("- Analysis scripts\n\n")
        f.write("### **04_DATA/**\n")
        f.write("- Raw data files\n")
        f.write("- Processed data\n")
        f.write("- CSV files with results\n\n")
        f.write("### **05_REPORTS/**\n")
        f.write("- Analysis reports\n")
        f.write("- Documentation\n")
        f.write("- Status reports\n\n")
        f.write("### **06_RESULTS/**\n")
        f.write("- Analysis results\n")
        f.write("- Visualizations\n")
        f.write("- Output files\n\n")
        f.write("## 🎯 **Quick Access**\n\n")
        f.write("- **Current Analysis:** `02_CURRENT_ANALYSIS/`\n")
        f.write("- **Scripts:** `03_SCRIPTS/`\n")
        f.write("- **Data:** `04_DATA/`\n")
        f.write("- **Reports:** `05_REPORTS/`\n")
        f.write("- **Results:** `06_RESULTS/`\n\n")
        f.write("## 📊 **Key Files**\n\n")
        f.write("- **Final Summary:** `02_CURRENT_ANALYSIS/FINAL_SUMMARY.md`\n")
        f.write("- **Execution Report:** `02_CURRENT_ANALYSIS/EXECUTION_REPORT.md`\n")
        f.write("- **Main Script:** `03_SCRIPTS/run_analysis_pipeline.py`\n")
        f.write("- **Data Collection:** `03_SCRIPTS/comprehensive_data_collector.py`\n")
        f.write("- **Overlap Analysis:** `03_SCRIPTS/overlap_analyzer.py`\n\n")
        f.write("---\n\n")
        f.write("*This index provides quick access to all organized files and folders.*\n")
    
    print("✅ Created main index file: INDEX.md")

def main():
    """Main organization function"""
    print("🧹 Organizing Bus Route Analysis Folder")
    print("=" * 50)
    print(f"📅 Organization Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    # Create folders
    print("\n📁 Creating organized folder structure...")
    create_folders()
    
    # Move files
    print("\n📦 Moving files to appropriate folders...")
    move_files()
    
    # Create index
    print("\n📋 Creating index files...")
    create_index_files()
    
    # Final summary
    print("\n🎉 Folder organization completed!")
    print("=" * 50)
    print("📁 **Organized Structure:**")
    print("   - 01_ARCHIVE_OLD_FILES/ - Old files archived")
    print("   - 02_CURRENT_ANALYSIS/ - Most recent analysis")
    print("   - 03_SCRIPTS/ - All Python scripts")
    print("   - 04_DATA/ - All data files")
    print("   - 05_REPORTS/ - All reports and documentation")
    print("   - 06_RESULTS/ - All analysis results")
    print("=" * 50)
    print("✅ **Organization Complete!**")
    print("📋 **Check INDEX.md for quick access to all files**")

if __name__ == "__main__":
    main()
