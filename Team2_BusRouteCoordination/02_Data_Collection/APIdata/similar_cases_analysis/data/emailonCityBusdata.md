# Citybus API Access Enquiry Email

## 📧 **Email Draft**

**To:** enquiry@digitalpolicy.gov.hk  
**Subject:** UPDATE: Citybus API Status - Partial Resolution Achieved  
**Date:** October 19, 2024  

---

**Dear City Bus Team, Transport Department and Digital Policy Office,**

I am writing to provide an update on Citybus API access status through Hong Kong Government Open Data APIs.

## ✅ **Good News - Partial Resolution**

Some Citybus API endpoints are now working successfully:

**Working Endpoints:**
- https://rt.data.gov.hk/v2/transport/citybus/route/ctb (200 OK) - **394+ routes collected**
- https://rt.data.gov.hk/v2/transport/citybus/company/ctb (200 OK) - **Company info available**

## ⚠️ **Remaining Issues**

Some endpoints are still returning 422 "Invalid/Missing parameter(s)" errors:

**Failed Endpoints:**
- https://rt.data.gov.hk/v2/transport/citybus/route-stop/ctb
- https://rt.data.gov.hk/v2/transport/citybus/eta/ctb
- https://data.etabus.gov.hk/v1/transport/citybus/route
- https://data.etabus.gov.hk/v1/transport/citybus/company
- https://data.etabus.gov.hk/v1/transport/citybus/route-stop
- https://data.etabus.gov.hk/v1/transport/citybus/eta

## 📊 **Public Impact**

This affects:
- Third-party app developers
- Transportation researchers
- Public service applications
- Real-time transit information systems
- Academic research projects

## 🔧 **Request**

Please urgently review and update the failing API endpoints to restore public data access. The public relies on this data for developing third-party applications and services.

**Priority:** High - Public data access is compromised

**Expected Resolution:** ASAP

## 📞 **Contact**

**Project:** Bus Route Coordination Research (GCAP3226)  
**Email:** [Your Email]  
**Phone:** [Your Phone]  

Thank you for your immediate attention to this matter.

**Best regards,**  
**[Your Name]**

---

## 📋 **Plain Text Version**

```
To: enquiry@digitalpolicy.gov.hk
Subject: Urgent: Citybus API Endpoint Failures - Public Data Access Issues
Date: October 19, 2024

Dear City Bus Team, Transport Department and Digital Policy Office,

I am writing to report critical API endpoint failures affecting public access to Citybus data through Hong Kong Government Open Data APIs.

URGENT ISSUE:
Multiple Citybus API endpoints are returning 422 "Invalid/Missing parameter(s)" errors, preventing public access to essential transportation data:

Failed Endpoints:
- https://rt.data.gov.hk/v2/transport/citybus/route-stop/ctb
- https://rt.data.gov.hk/v2/transport/citybus/eta/ctb
- https://data.etabus.gov.hk/v1/transport/citybus/route
- https://data.etabus.gov.hk/v1/transport/citybus/company
- https://data.etabus.gov.hk/v1/transport/citybus/route-stop
- https://data.etabus.gov.hk/v1/transport/citybus/eta

Working Endpoints:
- https://rt.data.gov.hk/v2/transport/citybus/route/ctb (200 OK)
- https://rt.data.gov.hk/v2/transport/citybus/company/ctb (200 OK)

PUBLIC IMPACT:
This affects:
- Third-party app developers
- Transportation researchers
- Public service applications
- Real-time transit information systems
- Academic research projects

REQUEST:
Please urgently review and update the failing API endpoints to restore public data access. The public relies on this data for developing third-party applications and services.

Priority: High - Public data access is compromised
Expected Resolution: ASAP

Contact:
Project: Bus Route Coordination Research (GCAP3226)
Email: [Your Email]
Phone: [Your Phone]

Thank you for your immediate attention to this matter.

Best regards,
[Your Name]
```

---

*This concise email addresses the urgent API endpoint failures and requests immediate review and updates for public data access.*