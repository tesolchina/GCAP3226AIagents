#!/usr/bin/env python3
"""
Analyze topics in Presentation1 MD files and team directories, then generate a comprehensive report.
"""
import os
import re
from pathlib import Path
from collections import defaultdict

def extract_keywords(text, min_length=4):
    """Extract meaningful keywords from text."""
    # Common stop words to exclude
    stop_words = {
        'this', 'that', 'these', 'those', 'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
        'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'been', 'be', 'have', 'has', 'had',
        'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'can', 'must',
        'our', 'we', 'they', 'you', 'your', 'their', 'his', 'her', 'its', 'my', 'me', 'him', 'us',
        'about', 'into', 'through', 'during', 'including', 'against', 'among', 'throughout', 'despite',
        'towards', 'upon', 'concerning', 'to', 'of', 'for', 'with', 'on', 'at', 'from', 'by', 'about',
        'into', 'through', 'during', 'including', 'against', 'among', 'throughout', 'despite',
        'what', 'which', 'who', 'when', 'where', 'why', 'how', 'all', 'each', 'every', 'both', 'few',
        'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
        'than', 'too', 'very', 'just', 'now', 'then', 'here', 'there', 'when', 'where', 'why', 'how'
    }
    
    # Extract words (alphanumeric, at least min_length chars)
    words = re.findall(r'\b[a-zA-Z]{' + str(min_length) + r',}\b', text.lower())
    
    # Filter out stop words and return unique words
    keywords = [w for w in words if w not in stop_words]
    return list(set(keywords))

def analyze_file_topics(file_path):
    """Analyze topics in a single file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract keywords
        keywords = extract_keywords(content)
        
        # Identify main topics based on keyword frequency and context
        keyword_freq = {}
        for word in keywords:
            keyword_freq[word] = keyword_freq.get(word, 0) + content.lower().count(word)
        
        # Get top keywords
        top_keywords = sorted(keyword_freq.items(), key=lambda x: x[1], reverse=True)[:20]
        
        # Identify main topic based on content analysis
        content_lower = content.lower()
        topics = []
        
        # Topic detection patterns
        topic_patterns = {
            'Bus Route Coordination': ['bus route', 'kmb', 'city bus', 'ct bus', '272a', '582', 'coordination', 'timetable', 'simultaneous', 'overlapping'],
            'Waste Charging Scheme': ['waste charging', 'solid waste', 'municipal waste', 'food waste', 'recycling', 'landfill', 'waste disposal'],
            'Green Community Recycling': ['green community', 'green dollar', 'recycling network', 'gsc', 'recycling station', 'waste reduction', 'recycling rate'],
            'Typhoon Signal Analysis': ['typhoon', 'signal', 'wind', 'hko', 'hong kong observatory', 'signal 8', 'wind speed', 'precautionary'],
            'Flu Shot Vaccination': ['flu shot', 'influenza', 'vaccination', 'vaccine', 'flu vaccine', 'school', 'children', 'health'],
            'Bus Stop Optimization': ['bus stop', 'stop merge', 'st martin', 'johnson road', 'optimization', 'congestion', 'placement']
        }
        
        for topic, patterns in topic_patterns.items():
            score = sum(1 for pattern in patterns if pattern in content_lower)
            if score > 0:
                topics.append((topic, score))
        
        topics.sort(key=lambda x: x[1], reverse=True)
        main_topic = topics[0][0] if topics else "General Discussion"
        
        return {
            'file': str(file_path),
            'main_topic': main_topic,
            'top_keywords': [kw[0] for kw in top_keywords],
            'word_count': len(content.split()),
            'all_topics': [t[0] for t in topics[:3]]  # Top 3 topics
        }
    except Exception as e:
        return {
            'file': str(file_path),
            'error': str(e)
        }

def analyze_directory(directory_path, file_extensions=['.md', '.txt']):
    """Analyze all files in a directory."""
    directory = Path(directory_path)
    results = []
    
    if not directory.exists():
        return results
    
    # Find all markdown and text files
    for ext in file_extensions:
        for file_path in directory.rglob(f"*{ext}"):
            # Skip very large files or binary-like files
            try:
                if file_path.stat().st_size > 10 * 1024 * 1024:  # Skip files > 10MB
                    continue
                result = analyze_file_topics(file_path)
                results.append(result)
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    
    return results

def generate_report(presentation_results, team_results):
    """Generate a comprehensive report."""
    report = []
    report.append("# Topic Analysis Report")
    report.append("")
    report.append("## Overview")
    report.append("")
    report.append("This report analyzes topics across Presentation1 files and team project directories.")
    report.append("")
    
    # Presentation1 Analysis
    report.append("## Presentation1 Files Analysis")
    report.append("")
    
    topic_mapping = defaultdict(list)
    
    for result in presentation_results:
        if 'error' in result:
            continue
        
        filename = Path(result['file']).name
        main_topic = result['main_topic']
        topic_mapping[main_topic].append(filename)
        
        report.append(f"### {filename}")
        report.append("")
        report.append(f"- **Main Topic**: {main_topic}")
        report.append(f"- **Word Count**: {result['word_count']}")
        report.append(f"- **Top Keywords**: {', '.join(result['top_keywords'][:10])}")
        if len(result['all_topics']) > 1:
            report.append(f"- **Related Topics**: {', '.join(result['all_topics'][1:])}")
        report.append("")
    
    # Summary by topic
    report.append("## Presentation1 Files by Topic")
    report.append("")
    for topic, files in sorted(topic_mapping.items()):
        report.append(f"### {topic}")
        for file in sorted(files):
            report.append(f"- {file}")
        report.append("")
    
    # Team Analysis
    report.append("## Team Directories Analysis")
    report.append("")
    
    team_summaries = defaultdict(lambda: {'files': [], 'topics': defaultdict(int), 'total_files': 0})
    
    for team_name, results in team_results.items():
        report.append(f"### {team_name}")
        report.append("")
        
        if not results:
            report.append("No analyzable files found.")
            report.append("")
            continue
        
        # Count topics
        topics_count = defaultdict(int)
        for result in results:
            if 'error' in result:
                continue
            team_summaries[team_name]['total_files'] += 1
            team_summaries[team_name]['files'].append(Path(result['file']).name)
            if 'main_topic' in result:
                topics_count[result['main_topic']] += 1
                team_summaries[team_name]['topics'][result['main_topic']] += 1
        
        if topics_count:
            report.append("**Main Topics Found:**")
            for topic, count in sorted(topics_count.items(), key=lambda x: x[1], reverse=True):
                report.append(f"- {topic}: {count} file(s)")
            report.append("")
        
        report.append(f"**Total Files Analyzed**: {len(results)}")
        report.append("")
    
    # Cross-reference summary
    report.append("## Cross-Reference Summary")
    report.append("")
    report.append("### Presentation Files to Team Projects Mapping")
    report.append("")
    
    mapping = {
        'Bus Route Coordination': 'Team2_BusRouteCoordination',
        'Waste Charging Scheme': 'Team4_SolidWasteCharging',
        'Green Community Recycling': 'Team5_GreenCommunity',
        'Typhoon Signal Analysis': 'Team3_Typhoon',
        'Flu Shot Vaccination': 'Team1_FluShot',
        'Bus Stop Optimization': 'Team6_BusStopMerge'
    }
    
    for topic, team in mapping.items():
        report.append(f"- **{topic}**")
        pres_files = [f for f in topic_mapping.get(topic, [])]
        if pres_files:
            report.append(f"  - Presentation Files: {', '.join(pres_files)}")
        report.append(f"  - Team Directory: {team}")
        report.append("")
    
    return '\n'.join(report)

def main():
    base_dir = Path("/Users/simonwang/Documents/Usage/GCAP3226")
    
    # Analyze Presentation1 files
    print("Analyzing Presentation1 files...")
    presentation_dir = base_dir / "Course_Docs" / "Presentation1"
    presentation_files = list(presentation_dir.glob("*.md"))
    
    presentation_results = []
    for md_file in sorted(presentation_files):
        print(f"  Processing {md_file.name}...")
        result = analyze_file_topics(md_file)
        presentation_results.append(result)
    
    # Analyze team directories
    print("\nAnalyzing team directories...")
    team_dirs = {
        'Team1_FluShot': base_dir / "Team1_FluShot",
        'Team2_BusRouteCoordination': base_dir / "Team2_BusRouteCoordination",
        'Team3_Typhoon': base_dir / "Team3_Typhoon",
        'Team4_SolidWasteCharging': base_dir / "Team4_SolidWasteCharging",
        'Team5_GreenCommunity': base_dir / "Team5_GreenCommunity",
        'Team6_BusStopMerge': base_dir / "Team6_BusStopMerge"
    }
    
    team_results = {}
    for team_name, team_dir in team_dirs.items():
        print(f"  Processing {team_name}...")
        results = analyze_directory(team_dir)
        team_results[team_name] = results
        print(f"    Found {len(results)} files")
    
    # Generate report
    print("\nGenerating report...")
    report = generate_report(presentation_results, team_results)
    
    # Save report
    report_path = base_dir / "Presentation1_Topic_Analysis_Report.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\nReport saved to: {report_path}")
    print("\nSummary:")
    print(f"  - Presentation1 files analyzed: {len(presentation_results)}")
    for team_name, results in team_results.items():
        print(f"  - {team_name}: {len(results)} files")

if __name__ == "__main__":
    main()


