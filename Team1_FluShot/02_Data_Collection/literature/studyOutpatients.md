# Assessing Vaccination Effectiveness Among Outpatients: Methodology Framework

## Overview
This document outlines how to assess influenza vaccination effectiveness among outpatients using a similar approach to the Lee et al. 2024 study, which focused on hospitalized children. The methodology can be adapted for outpatient settings to evaluate vaccine effectiveness against mild to moderate influenza cases.

## Reference Study: Lee et al. 2024
**Title**: Influenza vaccine effectiveness against influenza-associated hospitalizations in children, Hong Kong, November 2023 to June 2024  
**Methodology**: Test-negative design with conditional logistic regression  
**Population**: 4,367 children hospitalized with acute respiratory illness  
**Key Finding**: 55% VE against A(H3N2), 54% VE against A(H1N1), 66% VE against influenza B

## Adapted Methodology for Outpatient Settings

### 1. Study Design: Test-Negative Design for Outpatients

#### **Target Population**
- **Primary care clinics**: Family Medicine Clinics (FMC), Private Medical Practitioner (PMP) clinics
- **Age groups**: All ages (not limited to children)
- **Inclusion criteria**: 
  - Acute respiratory illness (ARI) symptoms
  - Fever ≥37.5°C or subjective fever
  - Onset within 7 days
  - Seeking outpatient care

#### **Case Definition**
- **ILI cases**: Fever + cough/sore throat
- **Severity stratification**: Mild, moderate, severe (based on symptoms)
- **Laboratory confirmation**: PCR testing for influenza A/B

#### **Control Group**
- **Influenza-negative**: PCR negative for influenza A/B
- **SARS-CoV-2 negative**: Exclude COVID-19 cases to avoid confounding
- **Other respiratory viruses**: Include/exclude based on study objectives

### 2. Data Collection Framework

#### **Clinical Data**
- **Demographics**: Age, sex, district of residence
- **Symptoms**: Fever, cough, sore throat, headache, myalgia, fatigue
- **Severity indicators**: Duration of illness, functional impact
- **Comorbidities**: Underlying medical conditions
- **Healthcare utilization**: Previous visits, medication use

#### **Vaccination Data**
- **Vaccination status**: Received influenza vaccine (yes/no)
- **Vaccination timing**: Date of vaccination relative to illness onset
- **Vaccine type**: Quadrivalent inactivated, live attenuated, trivalent
- **Previous vaccination**: History of prior season vaccination
- **Vaccination source**: School program, private clinic, public clinic

#### **Laboratory Data**
- **PCR results**: Influenza A/B, subtype (H1N1, H3N2), lineage (B/Victoria, B/Yamagata)
- **Other respiratory viruses**: RSV, adenovirus, rhinovirus, etc.
- **Sample collection**: Nasal swab, throat swab, combined
- **Testing platform**: Multiplex PCR, rapid antigen tests

### 3. Statistical Analysis Approach

#### **Primary Analysis: Conditional Logistic Regression**
```r
# Model specification
model <- clogit(influenza_positive ~ vaccination_status + 
                age + sex + underlying_conditions + 
                prior_vaccination + time_period, 
                data = study_data, 
                method = "exact")
```

#### **Key Variables**
- **Outcome**: Influenza positive (PCR confirmed)
- **Exposure**: Vaccination status (vaccinated vs. unvaccinated)
- **Covariates**: 
  - Age (continuous or categorical)
  - Sex
  - Underlying medical conditions
  - Prior vaccination history
  - Time period (to control for temporal trends)

#### **Stratification Analysis**
- **By age group**: 0-4, 5-17, 18-64, 65+ years
- **By vaccine type**: Inactivated vs. live attenuated
- **By time since vaccination**: <2 weeks, 2-4 weeks, >4 weeks
- **By influenza subtype**: A(H1N1), A(H3N2), B/Victoria, B/Yamagata

### 4. Sample Size Considerations

#### **Power Calculation**
- **Expected VE**: 50-60% (based on Lee et al. 2024)
- **Vaccination coverage**: 40-60% (varies by age group)
- **Influenza positivity rate**: 15-25% among ARI cases
- **Required sample size**: ~2,000-3,000 outpatients per season

#### **Recruitment Strategy**
- **Multi-site approach**: 10-15 outpatient clinics across Hong Kong
- **Geographic distribution**: Hong Kong Island, Kowloon, New Territories
- **Seasonal recruitment**: Peak influenza season (January-March)
- **Incentive structure**: Small compensation for participation

### 5. Data Sources and Partnerships

#### **Primary Care Networks**
- **Hospital Authority**: Family Medicine Clinics
- **Private sector**: Private Medical Practitioner clinics
- **School health**: School-based vaccination programs
- **Community clinics**: NGO-run health centers

#### **Laboratory Services**
- **Public laboratories**: CHP, Hospital Authority
- **Private laboratories**: Commercial testing services
- **Point-of-care testing**: Rapid antigen tests in clinics
- **Centralized testing**: Reference laboratory confirmation

#### **Data Integration**
- **Electronic health records**: Automated data extraction
- **Vaccination registries**: School vaccination database
- **Laboratory information systems**: Test result integration
- **Health information exchange**: Cross-system data sharing

### 6. Methodological Challenges and Solutions

#### **Challenge 1: Selection Bias**
- **Problem**: Vaccinated individuals may have different healthcare-seeking behavior
- **Solution**: 
  - Include all ARI cases regardless of vaccination status
  - Adjust for healthcare utilization patterns
  - Use propensity score matching

#### **Challenge 2: Confounding by Indication**
- **Problem**: High-risk individuals more likely to be vaccinated
- **Solution**:
  - Adjust for underlying medical conditions
  - Stratify by risk groups
  - Use instrumental variables

#### **Challenge 3: Temporal Confounding**
- **Problem**: Influenza circulation varies over time
- **Solution**:
  - Time-matched controls (2-week periods)
  - Adjust for epidemic phase
  - Use time-varying covariates

#### **Challenge 4: Vaccine Effectiveness Waning**
- **Problem**: VE decreases over time since vaccination
- **Solution**:
  - Include time since vaccination as covariate
  - Stratify by vaccination timing
  - Model waning effects

### 7. Outcome Measures and Endpoints

#### **Primary Endpoints**
- **Overall VE**: Against any influenza type/subtype
- **Strain-specific VE**: Against A(H1N1), A(H3N2), B/Victoria, B/Yamagata
- **Age-stratified VE**: By age group and risk status
- **Time-stratified VE**: By time since vaccination

#### **Secondary Endpoints**
- **Symptom severity**: Duration of illness, functional impact
- **Healthcare utilization**: Repeat visits, medication use
- **Complications**: Secondary infections, hospitalizations
- **Quality of life**: Work/school absenteeism, daily activities

### 8. Implementation Timeline

#### **Phase 1: Study Design and Setup (Months 1-3)**
- Protocol development and ethics approval
- Site selection and partnership agreements
- Laboratory testing setup and validation
- Staff training and standard operating procedures

#### **Phase 2: Pilot Study (Months 4-6)**
- Small-scale recruitment (200-300 participants)
- Protocol validation and refinement
- Data collection system testing
- Preliminary analysis and power calculation

#### **Phase 3: Full Study (Months 7-18)**
- Large-scale recruitment (2,000-3,000 participants)
- Data collection and quality control
- Laboratory testing and result management
- Interim analysis and monitoring

#### **Phase 4: Analysis and Reporting (Months 19-24)**
- Statistical analysis and modeling
- Results interpretation and validation
- Manuscript preparation and publication
- Policy recommendations and dissemination

### 9. Expected Outcomes and Applications

#### **Research Outcomes**
- **VE estimates**: Overall and strain-specific effectiveness
- **Age-specific patterns**: Differential protection by age group
- **Temporal dynamics**: Waning effects and seasonal variation
- **Risk factor analysis**: Comorbidity and demographic influences

#### **Policy Applications**
- **Vaccination recommendations**: Age-specific and risk-based
- **Program evaluation**: School-based vaccination effectiveness
- **Resource allocation**: Vaccine distribution and prioritization
- **Public health messaging**: Risk communication and education

#### **Modeling Applications**
- **Outbreak prediction**: Incorporate VE data into forecasting models
- **Economic evaluation**: Cost-effectiveness of vaccination programs
- **Scenario analysis**: Impact of different vaccination strategies
- **Policy simulation**: Test effects of program changes

### 10. Quality Assurance and Validation

#### **Data Quality Control**
- **Standardized protocols**: Consistent data collection procedures
- **Training programs**: Staff education and certification
- **Quality monitoring**: Regular audits and feedback
- **Data validation**: Cross-checking and error detection

#### **Laboratory Quality Assurance**
- **Proficiency testing**: Regular quality control samples
- **Standardization**: Consistent testing protocols
- **Blinding**: Laboratory staff unaware of vaccination status
- **Confirmation**: Repeat testing for positive cases

#### **Statistical Validation**
- **Sensitivity analysis**: Test robustness of results
- **Bias assessment**: Evaluate potential confounding
- **Model validation**: Cross-validation and bootstrapping
- **External validation**: Compare with other studies

### 11. Ethical Considerations

#### **Informed Consent**
- **Clear explanation**: Study purpose and procedures
- **Voluntary participation**: No coercion or pressure
- **Data protection**: Confidentiality and privacy
- **Right to withdraw**: Participants can exit at any time

#### **Data Privacy**
- **Anonymization**: Remove personal identifiers
- **Secure storage**: Encrypted databases and servers
- **Access control**: Limited to authorized personnel
- **Data sharing**: Only aggregated, de-identified data

#### **Benefit-Risk Assessment**
- **Minimal risk**: Routine clinical care and testing
- **Potential benefits**: Improved understanding of vaccine effectiveness
- **Risk mitigation**: Standard safety protocols
- **Oversight**: Independent ethics committee monitoring

### 12. Budget and Resource Requirements

#### **Personnel Costs**
- **Principal investigator**: 20% FTE
- **Study coordinator**: 100% FTE
- **Data collectors**: 2-3 FTE
- **Laboratory technicians**: 1-2 FTE
- **Statistician**: 50% FTE

#### **Operational Costs**
- **Laboratory testing**: $50-100 per sample
- **Data collection**: $20-30 per participant
- **Site fees**: $10,000-20,000 per site
- **Equipment**: $50,000-100,000
- **Travel**: $10,000-20,000

#### **Total Budget Estimate**
- **Pilot study**: $200,000-300,000
- **Full study**: $800,000-1,200,000
- **Per participant**: $300-500

### 13. Success Metrics and Evaluation

#### **Recruitment Targets**
- **Sample size**: 2,000-3,000 participants
- **Vaccination coverage**: 40-60% among participants
- **Influenza positivity**: 15-25% among ARI cases
- **Geographic distribution**: All 18 districts represented

#### **Data Quality Metrics**
- **Completeness**: >95% data completeness
- **Accuracy**: <5% error rate
- **Timeliness**: <48 hours from collection to entry
- **Consistency**: <10% inter-rater variability

#### **Scientific Impact**
- **Publication**: High-impact journal articles
- **Policy influence**: Government recommendations
- **International recognition**: Conference presentations
- **Methodological contribution**: Novel approaches and insights

## Conclusion

Assessing vaccination effectiveness among outpatients using the Lee et al. 2024 methodology provides a comprehensive framework for evaluating influenza vaccine performance in real-world settings. The adapted approach offers several advantages:

1. **Broader population coverage**: Not limited to hospitalized cases
2. **Earlier detection**: Captures mild to moderate cases
3. **Cost-effectiveness**: Lower per-participant costs than hospital studies
4. **Policy relevance**: Directly applicable to primary care settings
5. **Modeling utility**: Provides data for outbreak prediction models

The methodology can be implemented in Hong Kong's healthcare system with appropriate partnerships, resources, and ethical oversight. The results will directly inform our flu outbreak prediction models and support evidence-based vaccination policy decisions.
