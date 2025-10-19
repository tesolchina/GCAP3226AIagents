# 📋 Sample Instruction Template for API Data Access

## Purpose
This template helps you create clear instructions for AI agents to access and work with government open data APIs.

---

## Template Structure

### 1. INPUT (Dataset Information)

**Dataset URL**: [Paste the DATA.GOV.HK dataset page URL here]

Example:
```
https://data.gov.hk/en-data/dataset/mtr-data2-nexttrain-data
```

**Dataset Description**: [Brief description of what data this provides]

Example:
```
Real-time MTR train arrival information for all stations and lines
```

---

### 2. PROCESS (What the AI Agent Should Do)

#### Step 1: Analyze the Dataset Page
- [ ] Fetch the dataset webpage
- [ ] Identify the API endpoint(s)
- [ ] Find documentation links (PDF, webpage, etc.)
- [ ] Extract sample data formats

#### Step 2: Understand the API
- [ ] Download and analyze API documentation
- [ ] Test the API endpoint with sample parameters
- [ ] Understand the response format (JSON, XML, CSV, etc.)
- [ ] Identify required and optional parameters

#### Step 3: Create Documentation
- [ ] Write a comprehensive README explaining:
  - What data is available
  - How to access the API
  - Parameter requirements
  - Response format
  - Code examples
  
#### Step 4: Generate Working Code
- [ ] Create a simple example script
- [ ] Create an advanced test suite
- [ ] Add error handling
- [ ] Include data parsing functions
- [ ] Add visualization capabilities (if applicable)

#### Step 5: Validate and Test
- [ ] Run the code with real API calls
- [ ] Generate sample output files
- [ ] Create summary reports
- [ ] Verify all functionality works

---

### 3. OUTPUT (Expected Deliverables)

#### Documentation Files
- [ ] **README.md** - Comprehensive API documentation
- [ ] **QUICKSTART.md** - Quick start guide
- [ ] **overview.md** - Project overview

#### Code Files
- [ ] **simple_example.py** - Beginner-friendly example
- [ ] **advanced_test.py** - Full-featured test suite with visualization
- [ ] **requirements.txt** - Python dependencies

#### Output Files
- [ ] **api_output.json** - Sample JSON data from API
- [ ] **api_report.txt** - Human-readable summary
- [ ] **visualization.png/html** - Data visualization (if applicable)

#### Jupyter Notebook Integration
- [ ] Add executable code cells to notebook
- [ ] Include visualization outputs
- [ ] Provide clear explanations
- [ ] Add interactive examples

---

## 🎯 Example Instructions for AI Agent

### Complete Example: MTR Next Train Data

```markdown
INPUT:
Dataset URL: https://data.gov.hk/en-data/dataset/mtr-data2-nexttrain-data
Description: Real-time MTR train arrival information

PROCESS:
1. Fetch the webpage and find the API endpoint
2. Download API documentation PDFs
3. Test the API with sample station codes
4. Analyze JSON response structure
5. Create comprehensive documentation
6. Write Python code with visualization
7. Generate sample outputs

OUTPUT:
- Complete API documentation (README.md)
- Simple and advanced Python examples
- Working code with data visualization
- Sample JSON outputs
- Jupyter notebook with executable cells
- Instructions for exploring similar datasets
```

---

## 📊 Dataset Categories on DATA.GOV.HK

When exploring datasets for your project, consider these categories:

### 🚇 Transport
- MTR train schedules
- Bus routes and frequency
- Traffic speed maps
- Parking availability
- Ferry schedules

### 🌤️ Climate and Weather
- Temperature and humidity
- Air quality index
- Rainfall data
- UV index
- Weather warnings

### 🏙️ City Management
- Public facility locations
- Waste collection schedules
- Noise complaints
- Street lighting
- Tree locations

### 🏥 Health
- Hospital wait times
- Disease statistics
- Vaccination data
- Healthcare facility locations

### 🏘️ Housing
- Property prices
- Public housing data
- Building permits
- Land sales

### 💼 Employment
- Labor statistics
- Wage data
- Job vacancies
- Industry trends

### 🎓 Education
- School locations
- Student enrollment
- Exam results
- Education expenditure

### 🔐 Law and Security
- Crime statistics
- Emergency call data
- Traffic accidents

---

## 🔍 How to Find the Right Dataset for Your Project

### Step 1: Identify Your Policy Question
Example: "How can we improve public transportation accessibility?"

### Step 2: Brainstorm Relevant Data
- Bus route coverage
- MTR station locations
- Population density
- Elderly population distribution

### Step 3: Search DATA.GOV.HK
Visit: https://data.gov.hk/en-datasets
- Use the search bar
- Browse by category
- Check related datasets

### Step 4: Evaluate the Dataset
Ask yourself:
- ✅ Does it have an API or downloadable format?
- ✅ Is it updated regularly?
- ✅ Does it have documentation?
- ✅ Is it relevant to my policy question?

### Step 5: Use This Template
Fill in the INPUT, PROCESS, and OUTPUT sections above, then give it to an AI agent!

---

## 💡 Tips for Success

### For Students
1. **Start with your policy question** - Let the question guide your data needs
2. **Explore multiple datasets** - Combine data from different sources
3. **Check data freshness** - Ensure the data is recent and relevant
4. **Read the documentation** - Understand limitations and usage terms
5. **Test small first** - Start with a simple query before scaling up

### For AI Agents
1. **Be thorough** - Don't skip steps in the PROCESS
2. **Test everything** - Validate all code before delivering
3. **Document clearly** - Assume the reader is a beginner
4. **Provide examples** - Show, don't just tell
5. **Think about use cases** - Help users understand practical applications

---

## 📝 Fill-in Template

Use this blank template for your project:

```markdown
## My Dataset Project

### INPUT
Dataset URL: _________________________________

Dataset Description: _________________________________

Specific data I need: _________________________________

### PROCESS
AI Agent Tasks:
1. _________________________________
2. _________________________________
3. _________________________________
4. _________________________________
5. _________________________________

### OUTPUT
Expected Files:
1. _________________________________
2. _________________________________
3. _________________________________
4. _________________________________

Visualization Needed: [ ] Yes  [ ] No
If yes, what type? _________________________________

Jupyter Notebook Updates Needed: [ ] Yes  [ ] No
If yes, what to include? _________________________________
```

---

## 🎓 Learning Objectives

By using this template, students will learn to:
- ✅ Identify relevant government open data sources
- ✅ Understand API structures and documentation
- ✅ Write clear instructions for AI collaboration
- ✅ Create reproducible data access workflows
- ✅ Visualize and interpret API data
- ✅ Apply data to policy analysis questions

---

## 🔗 Related Resources

- **DATA.GOV.HK**: https://data.gov.hk/en-datasets
- **API Best Practices**: See README.md in this folder
- **Python Visualization**: matplotlib, seaborn, plotly
- **Jupyter Notebooks**: For interactive data exploration

---

## ✅ Checklist Before Starting

- [ ] I have identified a clear policy question
- [ ] I have found a relevant dataset on DATA.GOV.HK
- [ ] I have checked that the dataset has API access or is downloadable
- [ ] I have filled in the template above
- [ ] I understand what outputs I need
- [ ] I am ready to give instructions to an AI agent

---

**Ready to explore more datasets? Use this template and let AI agents help you access Hong Kong's open data! 🚀**

*Template created for GCAP3226 - Empowering Citizens through Data*
