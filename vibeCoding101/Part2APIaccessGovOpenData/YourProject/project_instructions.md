# Project Instructions Template

**Fill this out and give it to the AI agent to generate your project code!**

---

## 📋 Project Information

**Project Name**: [Your project name here]

**Group Members**: 
- [Name 1]
- [Name 2]
- [Name 3]

**Policy Question**: 
[What policy question are you trying to answer? Be specific!]

Example: "How does air quality vary across different districts in Hong Kong during typhoon season?"

---

## 📊 Dataset Information

### Primary Dataset

**Dataset Name**: [Full name of the dataset]

**Source**: DATA.GOV.HK

**Dataset URL**: [Paste the full URL from DATA.GOV.HK]

**Data Format**: 
- [ ] API (real-time)
- [ ] CSV download
- [ ] JSON download
- [ ] Other: ___________

**Update Frequency**:
- [ ] Real-time
- [ ] Daily
- [ ] Weekly
- [ ] Monthly
- [ ] Annually

### Additional Datasets (if any)

**Dataset 2**: [Name and URL]

**Dataset 3**: [Name and URL]

---

## 🎯 What I Want the AI Agent to Do

### Step 1: Data Access
```
Please help me access the following dataset:
[Dataset URL]

I need to:
- [ ] Read the API documentation
- [ ] Understand the data structure
- [ ] Create Python code to fetch the data
- [ ] Handle errors gracefully
```

### Step 2: Data Processing
```
Once we have the data, please:
1. [Specific processing task 1]
   Example: Filter data for the year 2024
   
2. [Specific processing task 2]
   Example: Calculate monthly averages
   
3. [Specific processing task 3]
   Example: Group data by district
```

### Step 3: Data Analysis
```
I want to analyze:
1. [Analysis goal 1]
   Example: Compare PM2.5 levels between Kowloon and Hong Kong Island
   
2. [Analysis goal 2]
   Example: Identify peak pollution hours
   
3. [Analysis goal 3]
   Example: Calculate correlation with temperature
```

### Step 4: Visualizations
```
Please create the following visualizations:

Chart 1: [Type of chart] showing [what data]
Example: Bar chart showing average air quality by district

Chart 2: [Type of chart] showing [what data]
Example: Line chart showing PM2.5 trends over time

Chart 3: [Type of chart] showing [what data]
Example: Heatmap showing pollution levels by hour and day
```

### Step 5: Output Files
```
Please generate:
- [ ] JSON file with processed data
- [ ] CSV file with summary statistics
- [ ] Text report with findings
- [ ] PNG files with visualizations
- [ ] README explaining how to run the code
```

---

## 🔧 Technical Requirements

### Python Version
- [ ] Python 3.8+
- [ ] Any version is fine

### Required Libraries (that I know of)
- [ ] requests (for API access)
- [ ] pandas (for data processing)
- [ ] matplotlib (for visualizations)
- [ ] Other: ___________

**Note**: The AI agent will suggest additional libraries if needed!

### Data Constraints
- Time period: [e.g., Last 3 months, Year 2024, etc.]
- Geographic scope: [e.g., All Hong Kong, Specific districts, etc.]
- Data size: [Any limits?]

---

## 📝 Specific Instructions for AI

### Data Collection
```
[Be very specific about what data you want]

Example:
"Please fetch air quality data for the following stations:
- Central, Hong Kong Island
- Mong Kok, Kowloon
- Tuen Mun, New Territories

For each station, get hourly PM2.5 readings for October 2024."
```

### Analysis Details
```
[Explain exactly what you want to learn from the data]

Example:
"I want to know:
1. Which station has the worst air quality on average?
2. What time of day typically has the highest pollution?
3. Is there a difference between weekdays and weekends?
4. Are there any noticeable patterns or trends?"
```

### Output Format
```
[Specify how you want the results presented]

Example:
"Please organize the output as:
1. A summary JSON file with key statistics
2. Individual CSV files for each station
3. A markdown report with:
   - Executive summary
   - Key findings (bullet points)
   - Detailed analysis
   - Recommendations
4. Visualization PNGs saved in an 'images' folder"
```

---

## 🎨 Visualization Preferences

### Color Scheme
- [ ] Use default colors
- [ ] Specific colors: [list colors]
- [ ] Color-blind friendly palette

### Chart Style
- [ ] Professional/formal style
- [ ] Colorful and engaging
- [ ] Minimalist black and white

### Labels and Titles
- [ ] English only
- [ ] English and Traditional Chinese
- [ ] Include data source attribution

---

## 📋 Deliverables Checklist

The AI agent should create:

- [ ] Python script for data access (`[your_name]_api_access.py`)
- [ ] Python script for analysis (`[your_name]_analysis.py`)
- [ ] Python script for visualization (`[your_name]_visualization.py`)
- [ ] Requirements file (`requirements.txt`)
- [ ] Data dictionary (`data_dictionary.md`)
- [ ] README with instructions (`README_instructions.md`)
- [ ] Sample output files
- [ ] Test/validation code

---

## 🚨 Important Notes

### What I Already Know
```
[Tell AI what you already understand so it can adjust its explanations]

Example:
"I'm familiar with basic Python but new to APIs.
Please include comments explaining the API-related code."
```

### What I Need Explained
```
[What do you want AI to explain in detail?]

Example:
"Please explain:
- How the API authentication works
- What each visualization shows
- How to modify the code to use different date ranges"
```

### Potential Challenges
```
[Any concerns or known issues?]

Example:
"The API might be slow or rate-limited.
Please include retry logic and error handling."
```

---

## ✅ Before Submitting to AI

Make sure you have:
- [ ] Filled in all sections above
- [ ] Provided the dataset URL
- [ ] Clearly stated your policy question
- [ ] Specified what analysis you want
- [ ] Listed desired visualizations
- [ ] Checked the dataset is accessible

---

## 🤖 Ready to Give to AI!

Once completed, copy this entire document and say to the AI agent:

```
"I have filled out my project instructions. 
Please read this carefully and help me build my data access project.
Generate all the necessary Python code, documentation, and files
according to my specifications."
```

Then paste this document!

---

## 📚 Examples for Inspiration

### Example 1: Transportation Project
- Dataset: Bus route data
- Question: Which bus routes are most affected by delays?
- Analysis: Compare on-time performance across routes
- Visualization: Heatmap of delays by route and time

### Example 2: Health Project
- Dataset: Hospital admission data
- Question: How do flu cases vary seasonally?
- Analysis: Identify peak seasons and affected age groups
- Visualization: Time series of flu cases with seasonal markers

### Example 3: Environment Project
- Dataset: Weather and air quality
- Question: How does weather affect air pollution?
- Analysis: Correlation analysis between weather and AQI
- Visualization: Scatter plots with trend lines

---

*Save this file as `project_instructions.md` after filling it out!*
