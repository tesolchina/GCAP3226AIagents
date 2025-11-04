# Team 2: API Data Collection - Overview for Students

## 📋 **Important Note for Students**
**You are NOT expected to write or run the code in this folder.** This folder contains technical implementation details for reference and understanding. Your role is to:

1. **Understand the overall workflow** and data collection approach
2. **Reflect on the methodology** and its implications for your research
3. **Use the insights** to inform your project analysis and recommendations
4. **Focus on the research questions** rather than technical implementation

## 🎯 **Purpose of This Folder**
This folder contains the technical framework for collecting and analyzing real-time bus data to support your research on bus route coordination. The files here demonstrate how data can be collected from Hong Kong's open data APIs to answer your research questions.

## 📁 **Folder Structure**

```
APIdata/
├── README.md                           # This overview document
├── scripts/                            # Technical implementation scripts
│   └── Data_Collection_Script_Template.py
├── data_structure/                     # Data organization framework
│   └── (data organization templates)
└── documentation/                      # Technical documentation
    ├── API_data_collection.md
    └── Similar_Cases_Analysis.md
```

## 🔍 **What You Should Understand**

### **1. Data Collection Workflow**
- **How data is collected:** From Hong Kong Government Open Data APIs
- **What data is collected:** Real-time bus arrival times, route information, stop data
- **When data is collected:** Continuous monitoring during peak and off-peak hours
- **Why this matters:** Provides evidence for your research on coordination decisions

### **2. Research Methodology**
- **Primary Data Sources:** Direct API access to real-time bus data
- **Secondary Analysis:** Comparison of different routes and coordination approaches
- **City-wide Analysis:** Identification of similar cases across Hong Kong
- **Impact Assessment:** How coordination decisions affect passenger experience

### **3. Key Research Questions Addressed**
- **What decisions does TD make** about coordinating overlapping routes?
- **What data is available** to inform these decisions?
- **How do coordination decisions** affect passenger experience?
- **What are the consequences** of current coordination approaches?

## 📊 **Data Sources Available**

### **Citybus Real-time Data**
- **Source:** [data.gov.hk Citybus API](https://data.gov.hk/en-data/dataset/ctb-eta-transport-realtime-eta)
- **Data:** Real-time arrival times, route information, stop data
- **Update Frequency:** Every 1 minute
- **Relevance:** Provides data for Citybus route 582

### **KMB/LWB Real-time Data**
- **Source:** [data.gov.hk KMB API](https://data.gov.hk/en-data/dataset/hk-td-tis_21-etakmb)
- **Data:** Real-time arrival times, route information, stop data
- **Update Frequency:** Every 1 minute
- **Relevance:** Provides data for KMB route 272A

## 🎯 **Your Research Focus**

### **Primary Research Questions**
1. **What specific decisions does the Transport Department make regarding coordination of overlapping routes from different operators?**
2. **What data does the Transport Department have access to for making coordination decisions?**
3. **How does the Transport Department's decision not to coordinate affect passenger experience and operational efficiency?**
4. **What factors influence the Transport Department's coordination decisions?**

### **Analysis Framework**
- **Decision Analysis:** Understanding TD's specific coordination decisions
- **Data Availability Assessment:** What data TD has access to and how it's used
- **Impact Analysis:** Consequences of current coordination decisions
- **Policy Recommendations:** Evidence-based recommendations for improved coordination

## 📈 **Expected Outcomes**

### **Research Impact**
- **Decision-Making Understanding:** Clear analysis of TD's coordination decisions
- **Data Availability Assessment:** Comprehensive evaluation of data access and utilization
- **Policy Process Analysis:** Framework for understanding transportation decision-making

### **Policy Recommendations**
- **Decision-Making Improvements:** Recommendations for TD's coordination decision processes
- **Data Access Enhancements:** Recommendations for improved data availability
- **Coordination Strategies:** Evidence-based recommendations for route coordination

## 🔄 **Workflow Understanding**

### **Phase 1: Data Collection (Weeks 5-7)**
1. **Route-Specific Data:** Collect data for KMB 272A and Citybus 582
2. **Real-time Monitoring:** Track bus arrivals and passenger patterns
3. **Overlap Analysis:** Analyze the 8 overlapping stops
4. **Coordination Assessment:** Evaluate current coordination effectiveness

### **Phase 2: City-wide Analysis (Weeks 6-8)**
1. **Similar Cases Identification:** Find other routes with significant overlaps
2. **Coordination Patterns:** Analyze different approaches to route coordination
3. **Best Practices:** Identify successful coordination examples
4. **Improvement Opportunities:** Find areas for better coordination

### **Phase 3: Analysis and Recommendations (Weeks 8-10)**
1. **Performance Analysis:** Assess impact of coordination decisions
2. **Mathematical Modeling:** Develop optimization models
3. **Policy Recommendations:** Create evidence-based recommendations
4. **Report Writing:** Document findings and recommendations

## 📚 **How to Use This Folder**

### **For Understanding (Not Implementation)**
1. **Read the documentation** to understand the data collection approach
2. **Review the scripts** to understand the technical methodology
3. **Reflect on the implications** for your research questions
4. **Use the insights** to inform your analysis and recommendations

### **Key Documents to Review**
- **`documentation/API_data_collection.md`:** Comprehensive data collection plan
- **`documentation/Similar_Cases_Analysis.md`:** Framework for city-wide analysis
- **`scripts/Data_Collection_Script_Template.py`:** Technical implementation example

### **Questions to Consider**
1. **How does this data collection approach support your research questions?**
2. **What insights can you gain from understanding the data collection methodology?**
3. **How does this technical framework inform your analysis of TD's decisions?**
4. **What are the implications for your policy recommendations?**

## 🎓 **Learning Objectives**

### **By understanding this technical framework, you should be able to:**
1. **Explain the data collection methodology** and its relevance to your research
2. **Understand the types of data available** for analyzing coordination decisions
3. **Reflect on the implications** of data availability for decision-making
4. **Develop informed recommendations** based on understanding of data collection approaches

### **Focus Areas for Your Research**
- **Decision-Making Analysis:** How TD makes coordination decisions
- **Data Utilization:** How available data is used in decision-making
- **Impact Assessment:** Consequences of coordination decisions
- **Policy Recommendations:** Evidence-based recommendations for improvement

## 📝 **Next Steps**

### **For Your Project**
1. **Review the documentation** to understand the data collection approach
2. **Reflect on the methodology** and its implications for your research
3. **Use the insights** to inform your analysis of TD's decisions
4. **Develop recommendations** based on understanding of data collection capabilities

### **For Your Report**
1. **Explain the data collection methodology** in your methodology section
2. **Discuss the implications** of data availability for decision-making
3. **Analyze the impact** of coordination decisions on passenger experience
4. **Provide recommendations** for improved coordination based on data insights

---

*This folder provides the technical foundation for understanding how data can be collected and analyzed to support your research on bus route coordination. Focus on understanding the methodology and its implications rather than implementing the technical details.*
