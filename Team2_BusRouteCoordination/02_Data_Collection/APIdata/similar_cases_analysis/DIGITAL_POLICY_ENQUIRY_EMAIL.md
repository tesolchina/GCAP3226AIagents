# Digital Policy Office Enquiry Email

**To:** enquiry@digitalpolicy.gov.hk  
**From:** [Your Name/Organization]  
**Subject:** Citybus API Access Issues - Research Project Support Request  
**Date:** October 19, 2024  
**Priority:** High - Research Project Blocked  

---

## **Email Content**

Dear Digital Policy Office Team,

I hope this email finds you well. I am writing to seek your assistance with API access issues that are currently blocking an important research project on Hong Kong's public transportation system.

### **Project Background**
We are conducting research on bus route coordination optimization in Hong Kong, specifically analyzing overlapping routes between different operators (KMB and Citybus) to identify opportunities for improved coordination and passenger experience.

### **Current Situation**
Our research project has successfully collected data from the KMB API (`https://data.etabus.gov.hk/v1/transport/kmb/route`) and obtained 1,574 routes with complete information. However, we are experiencing significant difficulties accessing Citybus data through the official API endpoints.

### **Specific Issues Encountered**

#### **1. Citybus API Endpoints Returning 422 Errors**
The following endpoints are consistently returning "422 - Invalid/Missing parameter(s)" errors:

- `https://data.etabus.gov.hk/v1/transport/citybus/route`
- `https://data.etabus.gov.hk/v1/transport/citybus/company`
- `https://data.etabus.gov.hk/v1/transport/citybus/route-stop`
- `https://data.etabus.gov.hk/v1/transport/citybus/eta`

#### **2. Working Alternative Found**
We have identified a working alternative endpoint:
- `https://rt.data.gov.hk/v2/transport/citybus/route/ctb` (Successfully collected 394 routes)

However, this endpoint only provides basic route information and lacks critical data needed for our analysis:
- Route-stop mappings
- Real-time ETA data
- Detailed service information

### **Research Impact**
These API access issues are significantly limiting our research capabilities:

1. **Incomplete Data Coverage:** Missing critical Citybus data for comprehensive analysis
2. **Limited Analysis Scope:** Cannot perform complete overlap analysis between operators
3. **Research Delays:** Project timeline impacted by data access limitations
4. **Policy Implications:** Reduced ability to provide evidence-based recommendations

### **Specific Requests**

#### **1. API Documentation**
Could you please provide:
- Complete API documentation for Citybus endpoints
- Required parameters for each endpoint
- Example requests and responses
- Authentication requirements (if any)

#### **2. Technical Support**
We would appreciate assistance with:
- Correct API usage for Citybus endpoints
- Parameter requirements for route-stop and ETA data
- Troubleshooting the 422 errors
- Alternative data access methods

#### **3. Data Access**
Specifically, we need access to:
- Complete Citybus route database
- Route-stop mappings for all routes
- Real-time ETA data for coordination analysis
- Service information and timetables

### **Research Objectives**
Our research aims to:
- Identify routes with overlapping stops between KMB and Citybus
- Analyze coordination patterns and effectiveness
- Assess passenger impact of coordination decisions
- Develop evidence-based recommendations for improved coordination

### **Expected Outcomes**
The research will contribute to:
- Better understanding of bus route coordination in Hong Kong
- Evidence-based policy recommendations
- Improved passenger experience
- Enhanced transportation system efficiency

### **Current Workaround**
We are currently using the working `rt.data.gov.hk` endpoint to collect basic Citybus route information, but this limits our analysis capabilities significantly.

### **Timeline**
Our research project has a tight timeline, and API access issues are causing significant delays. We would greatly appreciate prompt assistance to resolve these issues.

### **Contact Information**
- **Project:** Bus Route Coordination Optimization Research
- **Organization:** [Your Organization]
- **Contact:** [Your Name]
- **Email:** [Your Email]
- **Phone:** [Your Phone]

### **Attachments**
- Detailed API testing results
- Data access report
- Research project outline

### **Next Steps**
We would appreciate:
1. **Immediate Response:** Acknowledgment of this enquiry
2. **Technical Support:** Assistance with API access issues
3. **Documentation:** Complete API documentation
4. **Follow-up:** Regular updates on resolution progress

### **Appreciation**
We greatly appreciate your time and assistance in resolving these API access issues. Your support will enable us to complete this important research project and contribute valuable insights to Hong Kong's transportation policy development.

Thank you for your attention to this matter. We look forward to your prompt response and assistance.

---

**Best regards,**  
[Your Name]  
[Your Title]  
[Your Organization]  
[Your Contact Information]

---

## **Email Attachments**

### **Attachment 1: API Testing Results**
```
Citybus API Testing Results - October 19, 2024

Working Endpoints:
- https://rt.data.gov.hk/v2/transport/citybus/route/ctb (394 routes)

Non-Working Endpoints:
- https://data.etabus.gov.hk/v1/transport/citybus/route (422 error)
- https://data.etabus.gov.hk/v1/transport/citybus/company (422 error)
- https://data.etabus.gov.hk/v1/transport/citybus/route-stop (422 error)
- https://data.etabus.gov.hk/v1/transport/citybus/eta (422 error)
```

### **Attachment 2: Data Access Report**
- Complete analysis of API accessibility issues
- Detailed testing results
- Data collection limitations
- Research impact assessment

### **Attachment 3: Research Project Outline**
- Project objectives and scope
- Research methodology
- Expected outcomes
- Timeline and milestones

---

## **Follow-up Actions**

### **Immediate (Within 24 hours)**
1. Send enquiry email to enquiry@digitalpolicy.gov.hk
2. Follow up with phone call if no response
3. Document all communications

### **Short-term (Within 1 week)**
1. Follow up on email if no response
2. Contact alternative support channels
3. Implement workarounds for missing data

### **Long-term (Within 1 month)**
1. Establish ongoing communication with Digital Policy Office
2. Develop comprehensive data collection strategy
3. Implement continuous monitoring of API status

---

*This enquiry email provides a comprehensive request for assistance with Citybus API access issues, including detailed problem description, research impact, and specific requests for support.*
