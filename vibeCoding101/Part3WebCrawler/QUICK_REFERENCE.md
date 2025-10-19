# Web Crawler Quick Reference Guide
## GCAP3226 Student Cheat Sheet

### 1. Before You Start

```python
# Check robots.txt
import requests
response = requests.get("https://your-site.com/robots.txt")
print(response.text)
```

**What to look for:**
- `Disallow:` - URLs you CANNOT crawl
- `Allow:` - URLs you CAN crawl
- `Crawl-delay:` - Seconds to wait between requests

---

### 2. Find the Sitemap

```python
# Check sitemap
sitemap_url = "https://your-site.com/sitemap_index.xml"
response = requests.get(sitemap_url)
print(response.text)
```

**Common sitemap locations:**
- `/sitemap.xml`
- `/sitemap_index.xml`
- `/sitemap/sitemap.xml`

---

### 3. Set Up Your Crawler

```python
import requests
from bs4 import BeautifulSoup
import time

# Create session with User-Agent
session = requests.Session()
session.headers.update({
    'User-Agent': 'Student-Crawler/1.0 (Educational; your-email@example.com)'
})
```

---

### 4. Crawl One Page

```python
def crawl_page(url):
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    except Exception as e:
        print(f"Error: {e}")
        return None

# Use it
soup = crawl_page("https://example.com/page")
if soup:
    print(soup.get_text()[:500])  # First 500 characters
```

---

### 5. Detect Quantitative Data

```python
import re

def has_quantitative_data(soup):
    text = soup.get_text()
    
    # Count numbers
    numbers = re.findall(r'\d{1,3}(?:,\d{3})+|\d+(?:\.\d+)?%', text)
    
    # Count tables
    tables = len(soup.find_all('table'))
    
    # Check keywords
    keywords = ['statistics', 'data', 'analysis', 'report']
    has_keywords = any(kw in text.lower() for kw in keywords)
    
    return len(numbers) > 5 or tables > 0 or has_keywords
```

---

### 6. Rate Limiting (IMPORTANT!)

```python
import time

# Always wait between requests
time.sleep(2)  # 2 seconds

# Example loop
for url in urls:
    crawl_page(url)
    time.sleep(2)  # NEVER FORGET THIS!
```

**Rule of Thumb:**
- Government sites: 1-2 seconds
- Small sites: 2-3 seconds
- **NEVER** less than 0.5 seconds

---

### 7. Save Your Data

```python
import json

# Save HTML
with open('page.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

# Save metadata
metadata = {
    'url': url,
    'date': datetime.now().isoformat(),
    'has_data': True,
    'notes': 'Found 3 tables with statistics'
}
with open('metadata.json', 'w', encoding='utf-8') as f:
    json.dump(metadata, f, indent=2)
```

---

### 8. Handle Errors

```python
def safe_crawl(url):
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.content, 'html.parser')
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.Timeout:
        print("Timeout - site too slow")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    return None
```

---

### 9. Download Files

```python
def download_file(url, filename):
    response = session.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded: {filename}")

# Example
download_file("https://example.com/report.pdf", "report.pdf")
```

---

### 10. Complete Example

```python
import requests
from bs4 import BeautifulSoup
import time
import json

# Setup
session = requests.Session()
session.headers['User-Agent'] = 'Student-Crawler/1.0'

# URLs to crawl
urls = [
    "https://example.com/page1",
    "https://example.com/page2",
]

# Crawl each URL
results = []
for i, url in enumerate(urls, 1):
    print(f"[{i}/{len(urls)}] Crawling: {url}")
    
    try:
        response = session.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Analyze
        has_data = has_quantitative_data(soup)
        results.append({'url': url, 'has_data': has_data})
        
        print(f"  → Has data: {has_data}")
        
    except Exception as e:
        print(f"  → Error: {e}")
    
    time.sleep(2)  # Rate limiting!

# Save results
with open('results.json', 'w') as f:
    json.dump(results, f, indent=2)

print(f"\nDone! Crawled {len(urls)} pages")
```

---

## Ethics Checklist

Before you crawl, make sure you can answer YES to all:

- [ ] ✅ Checked robots.txt - am I allowed?
- [ ] ✅ Using a descriptive User-Agent
- [ ] ✅ Implementing rate limiting (≥1 second)
- [ ] ✅ Handling errors gracefully
- [ ] ✅ Not collecting personal data
- [ ] ✅ Using data for legitimate research
- [ ] ✅ Documenting my process

---

## Common Mistakes to Avoid

1. ❌ **No rate limiting** → Server overload
2. ❌ **Ignoring robots.txt** → Unethical
3. ❌ **No error handling** → Crashes
4. ❌ **No logging** → Can't debug
5. ❌ **Generic User-Agent** → Might get blocked
6. ❌ **No timeout** → Hangs forever
7. ❌ **Crawling login pages** → Privacy issues

---

## Useful Patterns

### Extract all links
```python
links = soup.find_all('a', href=True)
for link in links:
    print(link['href'])
```

### Extract all tables
```python
tables = soup.find_all('table')
for table in tables:
    print(table.get_text())
```

### Find numbers
```python
import re
numbers = re.findall(r'\d+(?:,\d{3})*(?:\.\d+)?', text)
```

### Check if PDF link
```python
if url.endswith('.pdf'):
    download_file(url, 'report.pdf')
```

---

## Help & Resources

**Documentation:**
- Beautiful Soup: https://www.crummy.com/software/BeautifulSoup/
- Requests: https://docs.python-requests.org/
- Python regex: https://docs.python.org/3/library/re.html

**Hong Kong Open Data:**
- https://data.gov.hk

**Questions?**
- Check the Jupyter notebook tutorial
- Review the example code in `cyberdefender/scripts/crawler.py`
- Ask during office hours

---

## Assignment Checklist

For your project, make sure you have:

- [ ] ✅ Checked robots.txt (include screenshot/output)
- [ ] ✅ Found sitemap (or explained why there isn't one)
- [ ] ✅ Written crawler code (well-commented)
- [ ] ✅ Implemented rate limiting
- [ ] ✅ Saved pages and metadata
- [ ] ✅ Analyzed results (what data did you find?)
- [ ] ✅ Written report (500-1000 words)
- [ ] ✅ Reflected on ethics

---

**Remember: With great crawling power comes great responsibility! 🕷️**
