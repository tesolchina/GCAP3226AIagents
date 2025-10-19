# Part 3: Web Crawler for Policy Analysis
## GCAP3226: Empowering Citizens through Data

**Status:** ✅ Complete  
**Date:** October 13, 2025  
**Case Study:** cyberdefender.hk (Hong Kong Government Cybersecurity Portal)

---

## 📋 Overview

This module teaches students how to systematically collect quantitative data from government websites using ethical web crawling techniques. Students learn to:

1. Analyze robots.txt and respect crawling permissions
2. Discover content using sitemaps
3. Identify pages with quantitative data
4. Implement ethical crawling practices
5. Extract and organize data for policy analysis

---

## 📁 Project Structure

```
Part3WebCrawler/
├── README.md                          # This file
├── overviewPlan.md                    # Initial project plan
├── work_log.md                        # Detailed process log ⭐
├── PROJECT_SUMMARY.md                 # Complete documentation ⭐⭐⭐
├── QUICK_REFERENCE.md                 # Student cheat sheet ⭐
├── WebCrawling_Tutorial.ipynb         # Interactive tutorial ⭐⭐⭐
│
└── cyberdefender/                     # Case study implementation
    ├── README.md                      # Project overview
    ├── requirements.txt               # Python dependencies
    │
    ├── scripts/
    │   ├── crawler.py                 # Main crawler (475 lines) ⭐⭐
    │   ├── analyze_results.py         # Results analyzer
    │   └── crawl_downloads.py         # Focused crawler
    │
    ├── data/
    │   ├── pages/                     # Downloaded HTML pages
    │   ├── downloads/                 # PDF, Excel, CSV files
    │   └── sitemaps/                  # Sitemap XML files
    │
    ├── logs/                          # Crawl execution logs
    └── analysis/                      # Analysis results (JSON)
```

---

## 🚀 Quick Start

### For Students

**Start here:** Open `WebCrawling_Tutorial.ipynb` in Jupyter

```bash
cd /workspaces/GCAP3226AIagents/vibeCoding101/Part3WebCrawler
jupyter notebook WebCrawling_Tutorial.ipynb
```

**Quick reference:** See `QUICK_REFERENCE.md` for code snippets

### For Instructors

**Complete documentation:** Read `PROJECT_SUMMARY.md`

**Implementation details:** Review `work_log.md`

**Example code:** Explore `cyberdefender/scripts/crawler.py`

---

## 📚 Key Files Explained

### 1. WebCrawling_Tutorial.ipynb ⭐⭐⭐
**Interactive Jupyter notebook for students**

**Contents:**
- Part 1: Web Crawling Ethics & robots.txt
- Part 2: Sitemap Discovery & Parsing
- Part 3: Quantitative Data Detection
- Part 4: Ethical Crawling Implementation
- Part 5: Comparison with Google Search
- Part 6: Student Assignment
- Part 7: Ethical Considerations

**Usage:** Self-paced learning with hands-on exercises

---

### 2. QUICK_REFERENCE.md ⭐
**Student cheat sheet**

Quick code snippets for:
- Checking robots.txt
- Finding sitemaps
- Basic crawling
- Data detection
- Error handling
- Rate limiting
- Ethics checklist

**Usage:** Keep open while coding

---

### 3. PROJECT_SUMMARY.md ⭐⭐⭐
**Complete project documentation**

Includes:
- Executive summary
- Technical implementation details
- Test results and analysis
- Educational value assessment
- Best practices and lessons learned
- Future enhancements
- Comparison: Crawler vs. Google Search

**Usage:** Instructor reference, project report

---

### 4. cyberdefender/scripts/crawler.py ⭐⭐
**Working web crawler implementation**

Features:
- Automatic sitemap discovery (found 149 URLs)
- Quantitative data detection algorithm
- Ethical crawling (2-second rate limiting)
- Comprehensive logging
- Metadata storage (JSON)
- File download capability

**Usage:** 
```bash
cd cyberdefender
python3 scripts/crawler.py --max-pages 10
```

---

### 5. work_log.md
**Step-by-step development log**

Documents:
- Each step of the implementation
- Decisions made and why
- Problems encountered and solutions
- Test results and analysis

**Usage:** Understand the development process

---

## 🎯 Learning Objectives

By completing this module, students will be able to:

1. ✅ **Understand Ethics**
   - Check and interpret robots.txt
   - Implement rate limiting
   - Use descriptive User-Agent

2. ✅ **Technical Skills**
   - Parse XML sitemaps
   - Extract data from HTML
   - Handle errors gracefully
   - Save and organize data

3. ✅ **Data Literacy**
   - Identify quantitative vs. qualitative content
   - Recognize data patterns
   - Evaluate data quality

4. ✅ **Policy Analysis**
   - Collect government data systematically
   - Build evidence for policy research
   - Document methodology

---

## 📊 Project Results

### Test Crawl Statistics (5 pages)
- **Success Rate:** 80% (4/5 pages)
- **Pages with Data:** 4 (100% of successful crawls)
- **Data Detection:** Tables found on all 4 pages
- **URLs Discovered:** 149 across 6 sitemaps

### Key Findings
1. ✅ Table detection: 100% accuracy
2. ✅ Keyword detection working ("data", "rate")
3. ✅ Error handling successful (handled 404)
4. ⚠️ Number detection needs improvement for Asian content
5. 💡 Downloads sitemap (21 files) is high-value target

---

## 🛠️ Installation

### Prerequisites
```bash
python3 -m pip install requests beautifulsoup4 lxml pandas
```

Or using requirements.txt:
```bash
cd cyberdefender
pip install -r requirements.txt
```

### Test Installation
```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
print("✓ All dependencies installed!")
```

---

## 💻 Usage Examples

### Example 1: Check robots.txt
```python
import requests
response = requests.get("https://cyberdefender.hk/robots.txt")
print(response.text)
```

### Example 2: Crawl with the provided script
```bash
cd cyberdefender
python3 scripts/crawler.py --max-pages 5
```

### Example 3: Analyze results
```bash
python3 scripts/analyze_results.py
```

### Example 4: Use in your code
```python
from crawler import CyberDefenderCrawler

crawler = CyberDefenderCrawler(output_dir="my_data")
crawler.crawl_site(max_pages=10)
```

---

## 📝 Student Assignment

### Task
Choose a Hong Kong government website and crawl it for quantitative data.

### Recommended Sites
1. **Census and Statistics Department:** https://www.censtatd.gov.hk
   - Population, economy, social statistics
   
2. **Environmental Protection Department:** https://www.epd.gov.hk
   - Air quality, waste, environmental reports
   
3. **Transport Department:** https://www.td.gov.hk
   - Traffic statistics, public transport data
   
4. **Food and Health Bureau:** https://www.fhb.gov.hk
   - Healthcare statistics, disease surveillance

### Deliverables
1. Python code (well-commented)
2. Data files collected
3. Analysis report (500-1000 words)
4. Ethical reflection (200-300 words)

### Grading Rubric
- Code functionality (30%)
- Data quality (25%)
- Analysis depth (25%)
- Ethics & documentation (20%)

---

## 🔍 Key Concepts

### 1. robots.txt
File that tells crawlers what they can/cannot access
```
User-agent: *
Disallow: /private/
Allow: /public/
```

### 2. Sitemap
XML file listing all pages on a website
- Makes crawling more efficient
- Usually at `/sitemap.xml` or `/sitemap_index.xml`

### 3. Rate Limiting
Waiting between requests to avoid overloading servers
```python
import time
time.sleep(2)  # Wait 2 seconds
```

### 4. Quantitative Data
Data that can be measured or counted:
- Numbers, percentages, statistics
- Tables, charts, graphs
- Reports with data

---

## ⚖️ Ethical Guidelines

### Always
✅ Check robots.txt first  
✅ Use descriptive User-Agent  
✅ Implement rate limiting (≥1 second)  
✅ Handle errors gracefully  
✅ Log your activities  
✅ Use data responsibly  

### Never
❌ Ignore robots.txt  
❌ Crawl faster than allowed  
❌ Collect personal data  
❌ Overwhelm servers  
❌ Violate terms of service  
❌ Use data unethically  

---

## 🔗 Resources

### Documentation
- **robots.txt:** https://www.robotstxt.org/
- **Sitemaps:** https://www.sitemaps.org/
- **Beautiful Soup:** https://www.crummy.com/software/BeautifulSoup/
- **Requests:** https://docs.python-requests.org/

### Hong Kong Data
- **Open Data Portal:** https://data.gov.hk
- **GovHK:** https://www.gov.hk
- **Census Dept:** https://www.censtatd.gov.hk

### Ethics & Best Practices
- **Web Scraping Best Practices:** https://www.scrapehero.com/web-scraping-best-practices/
- **Ethical Web Scraping:** https://towardsdatascience.com/ethics-in-web-scraping-b96b18136f01

---

## 🤝 Contributing

### For Students
- Complete the assignment
- Share interesting findings
- Suggest improvements

### For Instructors
- Provide feedback on tutorial
- Share teaching experiences
- Suggest additional examples

---

## 📈 Future Enhancements

### Short Term
- [ ] Add Chinese keyword detection
- [ ] Improve number pattern matching
- [ ] PDF text extraction
- [ ] Visualization dashboard

### Medium Term
- [ ] Parallel crawling
- [ ] Database storage (SQLite)
- [ ] Web interface
- [ ] Image analysis for charts

### Long Term
- [ ] NLP for content analysis
- [ ] Machine learning classification
- [ ] Automated report generation
- [ ] API for programmatic access

---

## 🏆 Project Achievements

✅ Functional crawler with real-world testing  
✅ Comprehensive educational materials  
✅ Interactive tutorial with exercises  
✅ Complete documentation  
✅ Ethical framework  
✅ Practical student assignment  
✅ Ready for course deployment  

---

## 📞 Support

### Questions?
1. Review the `WebCrawling_Tutorial.ipynb`
2. Check `QUICK_REFERENCE.md`
3. Read `PROJECT_SUMMARY.md`
4. Explore example code in `cyberdefender/scripts/`
5. Ask during office hours

### Issues?
- Check error logs in `cyberdefender/logs/`
- Verify dependencies are installed
- Ensure internet connectivity
- Review robots.txt compliance

---

## 📄 License & Usage

**For Educational Purposes**

This project is part of GCAP3226 coursework and is intended for educational use in teaching web scraping for policy analysis.

**Attribution:**
When using this material, please cite:
> Web Crawler Project, GCAP3226: Empowering Citizens through Data, October 2025

---

## 🎓 Course Integration

### Week 1-2: Introduction
- Introduce web crawling concepts
- Ethics and robots.txt
- Sitemap basics

### Week 3-4: Implementation
- Hands-on tutorial (Parts 1-4)
- Code examples and exercises
- Test on sample sites

### Week 5-6: Student Projects
- Assignment work
- Individual consulting
- Troubleshooting support

### Week 7: Presentations
- Share findings
- Discuss challenges
- Reflect on ethics

---

## ✨ Key Takeaways

1. **Web crawling is a powerful tool** for systematic data collection
2. **Ethics are paramount** - always crawl responsibly
3. **Sitemaps are invaluable** - use them when available
4. **Rate limiting is non-negotiable** - respect server resources
5. **Documentation matters** - log everything you do
6. **Start small** - test before full deployment
7. **Combine approaches** - use both crawling and manual search

---

**Ready to start crawling? Open the tutorial and begin your journey into web scraping for policy analysis! 🚀**

---

*Last updated: October 13, 2025*  
*Status: Production-ready for GCAP3226*
