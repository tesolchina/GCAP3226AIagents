# 🔍 Guide: Exploring Other DATA.GOV.HK Datasets

## Introduction

This guide helps you explore and use other datasets from Hong Kong's open data portal for your policy analysis projects. The key is that **AI agents can write Python code for you** as long as you provide the right information about APIs and dataset locations.

---

## 🎯 The Power of AI + Open Data

### What AI Agents Can Do For You

When you provide:
- ✅ A dataset URL from DATA.GOV.HK
- ✅ Clear instructions about what you want
- ✅ Your policy analysis question

AI agents can automatically:
- 🤖 Find and test the API
- 🤖 Write Python code to access data
- 🤖 Create visualizations
- 🤖 Generate documentation
- 🤖 Produce analysis-ready outputs

**You don't need to be a programmer!** You just need to know how to ask the right questions.

---

## 📊 Popular Datasets for Policy Analysis

### 🚇 Transport & Mobility

| Dataset | Use Cases | API Available |
|---------|-----------|---------------|
| **MTR Next Train** | Transit accessibility, service patterns | ✅ Yes |
| **Bus Route Data** | Coverage analysis, route optimization | ✅ Yes |
| **Traffic Speed Map** | Congestion analysis, peak hours | ✅ Yes |
| **Parking Vacancy** | Parking policy, urban planning | ✅ Yes |
| **Bicycle Path Network** | Active transport, infrastructure | ✅ Yes |

**Example Policy Questions:**
- How can we improve public transit coverage in underserved areas?
- What are the peak congestion times and where?
- Is parking availability linked to traffic patterns?

### 🌤️ Environment & Climate

| Dataset | Use Cases | API Available |
|---------|-----------|---------------|
| **Air Quality Health Index** | Public health, pollution policy | ✅ Yes |
| **Weather Data** | Climate analysis, extreme events | ✅ Yes |
| **Noise Complaints** | Quality of life, urban planning | ✅ Yes |
| **Tree Locations** | Green space, urban forestry | ✅ Yes |
| **Beach Water Quality** | Recreation, public health | ✅ Yes |

**Example Policy Questions:**
- How does air quality correlate with health outcomes?
- Which areas lack green space?
- Are noise complaints related to traffic patterns?

### 🏥 Health & Safety

| Dataset | Use Cases | API Available |
|---------|-----------|---------------|
| **Hospital Wait Times** | Healthcare access, efficiency | ✅ Yes |
| **Flu Vaccination Data** | Public health campaigns | ✅ Yes |
| **Food License Data** | Business registration, compliance | ✅ Yes |
| **Emergency Call Data** | Public safety, resource allocation | ✅ Yes |

**Example Policy Questions:**
- How can we improve flu vaccination rates?
- Where are healthcare services most needed?
- What factors predict emergency call volumes?

### 🏘️ Housing & Development

| Dataset | Use Cases | API Available |
|---------|-----------|---------------|
| **Property Transactions** | Market analysis, affordability | ✅ Yes |
| **Public Housing Data** | Social housing policy | ✅ Yes |
| **Building Permits** | Development trends | ✅ Yes |
| **Land Sales** | Urban development | ✅ Yes |

**Example Policy Questions:**
- Is housing becoming less affordable?
- Where should new public housing be built?
- What are development trends by district?

### 📚 Education & Demographics

| Dataset | Use Cases | API Available |
|---------|-----------|---------------|
| **School Locations** | Education access, planning | ✅ Yes |
| **Population Census** | Demographics, planning | ✅ Yes |
| **Elderly Care Facilities** | Aging policy, resource allocation | ✅ Yes |

**Example Policy Questions:**
- Are schools equitably distributed?
- How is population aging affecting different districts?
- Where are elderly services most needed?

---

## 🚀 Step-by-Step: Using Any Dataset

### Step 1: Find Your Dataset

1. Go to **https://data.gov.hk/en-datasets**
2. Use search or browse by category
3. Look for datasets with **API access**
4. Read the dataset description

### Step 2: Prepare Your Instructions

Use the **INSTRUCTION_TEMPLATE.md** in this folder:

```markdown
INPUT:
Dataset URL: [paste the data.gov.hk URL]
Description: [what data this provides]
My policy question: [your specific question]

PROCESS:
1. Fetch the dataset page
2. Find the API endpoint
3. Test the API
4. Create visualization
5. Generate analysis

OUTPUT:
- Python code to access data
- Visualization of key patterns
- Data summary table
- Jupyter notebook with analysis
```

### Step 3: Give Instructions to AI Agent

Example prompt:

```
I want to analyze air quality data to understand pollution patterns in Hong Kong.

INPUT:
Dataset URL: https://data.gov.hk/en-data/dataset/hk-epd-airteam-air-quality-health-index
Description: Real-time Air Quality Health Index (AQHI) for different areas

PROCESS:
Please:
1. Access this dataset and find the API
2. Write Python code to fetch current AQHI data
3. Create a visualization showing AQHI by district
4. Generate a time-series analysis if historical data available
5. Create executable Jupyter notebook cells

OUTPUT:
- README.md explaining the data
- Python script with visualization
- Jupyter notebook with executable cells
- Sample output images
```

### Step 4: Review and Run the Code

The AI agent will generate:
- ✅ Documentation
- ✅ Working Python code
- ✅ Visualization scripts
- ✅ Jupyter notebook cells

You can then:
- Run the code in Jupyter notebook
- Modify parameters for your analysis
- Create custom visualizations
- Export data for reports

---

## 💡 Tips for Success

### Finding Good Datasets

✅ **Look for datasets with:**
- API access (easier to work with)
- Regular updates (more current)
- Good documentation
- Relevance to your policy question

❌ **Avoid datasets that:**
- Only have PDF downloads
- Haven't been updated in years
- Lack clear descriptions
- Have complex authentication

### Writing Good Instructions

✅ **Be specific about:**
- What data you need
- What visualizations you want
- What format you prefer
- Your end goal (report, presentation, etc.)

❌ **Don't be vague:**
- "Get some data"
- "Make a chart"
- "Analyze stuff"

### Working with AI Agents

✅ **Do:**
- Provide the exact dataset URL
- Explain your policy question
- Ask for executable code
- Request visualizations
- Specify output formats

❌ **Don't:**
- Assume the AI knows which dataset
- Skip explaining your goal
- Forget to ask for visualization
- Ignore error messages

---

## 📋 Real-World Examples

### Example 1: Bus Route Coverage Analysis

**Policy Question:** Are bus services adequate in elderly-populated areas?

**Datasets Needed:**
1. Bus route data
2. Population by age data
3. Bus stop locations

**AI Instructions:**
```markdown
Please help me analyze bus coverage for elderly populations:

1. Access bus route data: [URL]
2. Access population demographics: [URL]
3. Create a map showing bus stop density vs elderly population
4. Calculate coverage metrics
5. Generate visualization in Jupyter notebook
```

**AI Will Generate:**
- Python code to fetch both datasets
- Map visualization with heatmap overlay
- Statistical analysis of coverage
- Recommendations based on data

### Example 2: Air Quality & Health Analysis

**Policy Question:** Does poor air quality correlate with hospital visits?

**Datasets Needed:**
1. Air Quality Health Index
2. Hospital emergency visits

**AI Instructions:**
```markdown
Please analyze the relationship between air quality and health:

1. Access AQHI data: [URL]
2. Access hospital data: [URL]
3. Create time-series comparison
4. Calculate correlation
5. Generate visualization in Jupyter notebook
```

**AI Will Generate:**
- Data fetching and cleaning code
- Correlation analysis
- Line charts showing both metrics
- Statistical significance tests

### Example 3: Housing Affordability Trends

**Policy Question:** Is housing becoming less affordable over time?

**Datasets Needed:**
1. Property transaction prices
2. Income statistics

**AI Instructions:**
```markdown
Please analyze housing affordability trends:

1. Access property price data: [URL]
2. Access income data: [URL]
3. Calculate price-to-income ratio
4. Create trend visualization
5. Generate analysis in Jupyter notebook
```

**AI Will Generate:**
- Data import and merging code
- Ratio calculation
- Trend line charts
- District-by-district comparison

---

## 🔧 Technical Tips

### Understanding API Parameters

Most DATA.GOV.HK APIs use similar patterns:

```python
# Common parameter patterns
params = {
    'date': '2025-10-13',      # Date filter
    'district': 'Central',      # Location filter
    'lang': 'en',              # Language
    'format': 'json'           # Response format
}
```

### Handling API Responses

```python
import requests

response = requests.get(api_url, params=params)
data = response.json()

# Check status
if data.get('status') == 1:
    # Success - process data
    process_data(data)
else:
    # Error - show message
    print(f"Error: {data.get('message')}")
```

### Creating Visualizations

```python
import matplotlib.pyplot as plt
import pandas as pd

# Create DataFrame
df = pd.DataFrame(data)

# Simple bar chart
df.plot(kind='bar', x='category', y='value')
plt.title('My Analysis')
plt.savefig('output.png')
plt.show()
```

---

## 📚 Resources for Each Dataset Category

### Transport Data
- **Main Portal:** https://data.gov.hk/en-datasets/category/transport
- **Key Providers:** MTR, Transport Department, Highways Department
- **Update Frequency:** Real-time to daily

### Environment Data
- **Main Portal:** https://data.gov.hk/en-datasets/category/environment
- **Key Providers:** EPD, HKO, Agriculture Department
- **Update Frequency:** Hourly to daily

### Health Data
- **Main Portal:** https://data.gov.hk/en-datasets/category/health
- **Key Providers:** Department of Health, Hospital Authority
- **Update Frequency:** Daily to monthly

### Housing Data
- **Main Portal:** https://data.gov.hk/en-datasets/category/housing
- **Key Providers:** Rating & Valuation Department, Housing Authority
- **Update Frequency:** Monthly to quarterly

---

## ✅ Checklist for Your Project

### Before You Start
- [ ] I have a clear policy question
- [ ] I've searched DATA.GOV.HK for relevant datasets
- [ ] I've confirmed the dataset has API or download access
- [ ] I've read the dataset description
- [ ] I understand what data is available

### Prepare Instructions
- [ ] I've filled out the INSTRUCTION_TEMPLATE.md
- [ ] I've specified what visualizations I want
- [ ] I've explained my policy question clearly
- [ ] I've provided the exact dataset URLs

### After AI Generates Code
- [ ] I've reviewed the README documentation
- [ ] I've run the Python code successfully
- [ ] I've checked the visualizations
- [ ] I've verified the data makes sense
- [ ] I've saved outputs for my report

---

## 🎓 Learning Outcomes

By exploring different datasets, you will:

1. **Understand Open Data**
   - What data government provides
   - How to access it programmatically
   - Terms of use and limitations

2. **Develop Data Literacy**
   - Reading API documentation
   - Understanding data formats
   - Interpreting visualizations

3. **Master AI Collaboration**
   - Writing clear instructions
   - Reviewing generated code
   - Iterating on analysis

4. **Apply to Policy**
   - Connecting data to questions
   - Evidence-based arguments
   - Data-driven recommendations

---

## 🚀 Ready to Explore?

### Your Next Steps

1. **Choose a policy question** from your group project
2. **Search DATA.GOV.HK** for relevant datasets
3. **Use INSTRUCTION_TEMPLATE.md** to prepare your request
4. **Give instructions to AI agent** and get working code
5. **Run the code** in Jupyter notebook
6. **Analyze results** for your policy report

### Remember

**The key learning is:** AI agents can write Python code for you as long as you provide the right information about APIs and dataset locations. You don't need to be a programmer—you need to be a good communicator!

---

## 📞 Need Help?

### If you're stuck:
1. Check if the dataset has API access
2. Review the INSTRUCTION_TEMPLATE.md
3. Look at the MTR example in this folder
4. Make sure your instructions are specific
5. Ask your AI agent to explain any errors

### Common Issues:
- **"Can't find API"** → Check if dataset has "API" badge on data.gov.hk
- **"Code doesn't work"** → Make sure you installed requirements.txt
- **"No visualization"** → Explicitly ask for charts in your instructions
- **"Data confusing"** → Ask AI to add explanatory comments

---

**Happy exploring! Remember: AI + Open Data = Powerful Policy Analysis 🚀**

*Guide created for GCAP3226 - Empowering Citizens through Data*
