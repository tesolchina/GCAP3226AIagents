# Cyberdefender.hk Web Crawler Project

## Project Overview
This project demonstrates web crawling techniques for extracting quantitative data from government websites, specifically targeting https://cyberdefender.hk.

**Course:** GCAP3226 - Empowering Citizens through Data  
**Topic:** Web Crawling for Policy Analysis  
**Date:** October 13, 2025

## Objectives
1. Learn to respect robots.txt and crawling ethics
2. Extract pages containing quantitative data (numbers, charts, statistics)
3. Download relevant documents and files
4. Compare AI-powered crawling vs. Google site-specific search
5. Build reusable tools for government website analysis

## Target Website
- **URL:** https://cyberdefender.hk
- **Type:** Government cybersecurity information portal
- **Platform:** WordPress with Yoast SEO
- **Robots.txt:** Allows all crawling (no restrictions)

## Directory Structure
```
cyberdefender/
├── analysis/          # Data analysis results and reports
├── data/
│   ├── pages/        # Downloaded HTML pages with quantitative data
│   ├── downloads/    # PDF, Excel, and other document files
│   └── sitemaps/     # Sitemap XML files
├── logs/             # Crawl logs and error reports
└── scripts/          # Python crawler scripts
```

## Crawling Rules & Ethics
✅ **Allowed:** Full site crawl (robots.txt has no restrictions)  
⚠️ **Best Practices:**
- Implement rate limiting (1-2 seconds between requests)
- Respect server resources
- Identify our crawler with a proper User-Agent
- Log all activities for transparency

## Sitemaps Available
1. `post-sitemap.xml` - Blog posts
2. `page-sitemap.xml` - Static pages
3. `sdm_downloads-sitemap.xml` - **Downloadable files (KEY TARGET)**
4. `category-sitemap.xml` - Content categories
5. `gm_menu_block-sitemap.xml` - Menu structure
6. `r3d-sitemap.xml` - Custom content

## Keywords to Identify Quantitative Data
- Numbers: statistics, percentages, counts
- Financial data: budget, cost, expenditure
- Time series: dates, years, trends
- Charts/graphs: visualization indicators
- Tables: structured data presentation
- Data formats: CSV, Excel, PDF reports

## Tools & Libraries
- **requests** - HTTP requests
- **beautifulsoup4** - HTML parsing
- **lxml** - XML sitemap parsing
- **pandas** - Data analysis
- **re** - Pattern matching for numbers

## Usage
See the Jupyter notebook tutorial for step-by-step guidance on using these tools.

## Educational Goals
Students will learn to:
1. Analyze robots.txt and sitemaps
2. Implement ethical web crawling
3. Identify pages with quantitative data
4. Extract and organize data systematically
5. Apply these techniques to other government websites

## Related Resources
- [robots.txt Wikipedia](https://en.wikipedia.org/wiki/Robots.txt)
- [Sitemaps Protocol](https://www.sitemaps.org/)
- [Web Scraping Best Practices](https://www.scrapehero.com/web-scraping-best-practices/)
