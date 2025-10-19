# Empowering Citizens through Data: Participatory Policy Analysis for Hong Kong - Week 3 Lecture Enhancement

## Executive Summary

Week 3 of the course focused heavily on structuring the **Group Project**, which is identified as the most important assessment component. The instructor outlined the necessary steps for forming teams, selecting from eight proposed topics (or proposing an open-ended one), and adhering to a strict timeline spanning several weeks, emphasizing the goal of evaluating government data governance practices. A key element of the project involves using the **Access to Information (ATI)** mechanism to formally request data from government departments.

The latter half of the lecture transitioned into a technical recap of Week 2's data visualization techniques using **Jupyter Notebooks** and **AI assistance (GitHub Copilot)**, followed by an in-depth introduction to **Linear Regression** using the Municipal Solid Waste Charging Scheme survey data as a case study. This introduction served to bridge the quantitative modeling skills (taught by Dr. Wu) with the qualitative policy analysis required for the main project.

## Key Topics Covered

*   Logistics and Administration (WhatsApp group, Moodle setup).
*   Detailed instructions and timeline for the **Group Project**.
*   Overview of the eight proposed project topics, focusing on policy areas in Hong Kong.
*   Recap of **Data Visualization** using Python/Jupyter Notebooks.
*   Introduction to **Linear Regression** methodology and assumptions.
*   Case Study: Analyzing public support for the **Municipal Solid Waste Charging Scheme** using regression.
*   Guidance on using AI tools (Copilot) for coding and analysis.

***

## Main Discussion Points

### 1. Group Project Setup and Logistics

*   **Communication:** Students are strongly encouraged to join the **WhatsApp group** for close interaction.
*   **Assessment Weight:** The Group Project is the **most important component** of the assessment, underpinning presentations, reflective essays, and human-AI collaboration notes.
*   **Team Formation:**
    *   Group size should be **4 to 6 members**.
    *   Students are encouraged to form teams by the end of Week 3.
    *   Ideal teams should include at least one student from a **Computer Science or Math major** to facilitate quantitative work, promoting **transdisciplinary thinking**.
*   **Timeline Overview (Weeks 3-7):**
    *   **Weeks 3 & 4:** Explore topics, form teams, learn math modeling tools.
    *   **Week 5:** Finalize topic; small group meetings.
    *   **Weeks 6 & 7:** Begin data collection, including sending formal requests to the government under the **Access to Information (ATI) Code**.

### 2. Project Mission and Stages

The core mission is to **synergize quantitative reasoning with qualitative reasoning** to evaluate how government staff practice **data governance** and demonstrate how decisions can be improved using data.

*   **Stage 1: Topic Selection & Review:** Select a specific government decision (avoid broad topics). Review existing information (news, documents) to gauge data-driven adoption.
*   **Stage 2: Data Collection:**
    *   Source 1: **data.gov.hk** for existing quantitative data.
    *   Source 2: Formal requests to government departments via **ATI** (deadline Week 6).
    *   Fieldwork may be necessary if government data is incomplete.
    *   **Week 7 Goal:** Complete a **data inventory table** and submit all ATI requests.
*   **Stage 3: Analysis & Argumentation:** Apply math models and critical thinking skills to demonstrate that the government *can* do a better job using data. The goal is to create a convincing, feasible demo for lawmakers and staff.

### 3. Project Topics Overview

The instructor presented 8 potential topics:

*   **Topics 1-3 (Bus Service):** Focus on public transportation optimization (frequency, merging stops, route coordination via simulation). Solutions should have potential to scale city-wide.
*   **Topic 4 (MSW Charging Scheme):** Analyzing public perception and how government storytelling/publicity decisions influence policy acceptance. Preliminary work exists.
*   **Topic 5 (Green Net Community):** Evaluating the cost-effectiveness of the Green Net Community project (preliminary student research suggests it may be a waste of money).
*   **Topic 6 (Flu Shot):** Re-examining influenza vaccination data using new math models.
*   **Topic 7 (Typhoon Signal Timing):** Analyzing the Hong Kong Observatory's decision to change the timing of hoisting Typhoon Signal No. 8, contrasting their traditional data-driven approach with the recent specific case.
*   **Topic 8 (Open-Ended):** Explore any dataset on **data.gov.hk** and connect it to a specific government policy or decision. Requires more independent exploration and potentially programming.

### 4. Data Visualization Recap (Week 2)

*   **Process:** Load data, understand variables, use correct visualization types (bar/pie for categorical; histogram/boxplot for continuous).
*   **Preference:** Bar charts are preferred over pie charts for judging magnitude.
*   **Case Study (Waste Charging Questionnaire):** Visualizations showed initial public support, and the effect of providing information (landfill limits, Korean success story) on shifting opinions (e.g., decrease in "strongly oppose" but also a decrease in "strongly support").
*   **Tool Access:** The Jupyter Notebook for visualization is available on Moodle under the "Jupyter Notebook" section. Students can use VS Code or **Google Colab** (with limitations regarding Copilot access).

### 5. Introduction to Regression Modeling (Dr. Wu)

*   **Focus:** The course will focus on two main models: **Regression** and **Optimization via Simulation**.
*   **Case Study: MSW Charging Scheme Support:**
    *   **Research Questions:** 1) What factors influence support level? 2) Did pre/post information testing change support?
    *   **Methodology:** Used a questionnaire with variables covering attitude (fairness), knowledge, behavior, and demographics.
    *   **Sampling Limitation:** The sample size (N=97) was non-probability based, leading to potential **selection bias** (e.g., high proportion of Master's degree holders).
*   **Linear Regression Basics:**
    *   Used to determine the association between a response variable ($Y$, e.g., support level) and explanatory variables ($X$).
    *   **Assumptions:** Response variable should ideally be continuous (though ordinal data like 1-5 can be approximated if sample size is large enough and distribution is roughly bell-shaped). The relationship between X and Y is assumed to be **linear**.
    *   **Interpretation:** Coefficients ($\beta_0, \beta_1$) quantify the expected change in $Y$ for a one-unit increase in $X$, **holding other variables constant** (in multiple regression).
    *   **Causality:** Regression only shows **association**, not causation.
*   **Regression Results (Fairness vs. Support):**
    *   Perceived fairness was significantly associated with support ($R^2 \approx 52\%$).
    *   **Policy Recommendation:** Prioritize enhancing public engagement to boost perceived **government responsiveness** (which showed a slightly larger coefficient than fairness).
*   **Multiple Linear Regression & Forward Selection:**
    *   When controlling for multiple factors, only **perceived fairness** and **perceived government responsiveness** remained statistically significant predictors of support.

***

## Important Concepts

*   **Transdisciplinary Thinking:** Combining quantitative (Math/CS) and qualitative (Language Center) approaches.
*   **Access to Information (ATI) Code:** The "secret weapon" tool used to formally request data from government departments.
*   **Data-Driven Approach:** Making government decisions informed by quantitative data.
*   **Linear Regression:** A statistical method to model the linear relationship between a response variable and one or more explanatory variables.
*   **Coefficient ($\beta_1$):** The estimated change in the response variable for a one-unit change in the explanatory variable.
*   **P-value:** Used to test the significance of coefficients; a value $< 0.05$ suggests the association is statistically significant (i.e., the coefficient is significantly different from zero).
*   **$R^2$ (R-squared):** Measures the proportion of the variance in the response variable that is predictable from the explanatory variable(s).
*   **Selection Bias:** Bias introduced when the sample is not representative of the population (e.g., surveying only easily accessible friends/family).

***

## Student Activities/Interactions

*   **Group Formation Check:** Instructor asked for a show of hands regarding students who already had team members.
*   **CS/Math Major Introductions:** Students Bonnie (CS) and Amy (Math) were invited to introduce themselves to help facilitate team formation.
*   **Break:** A 5-minute break was called to allow students to network and finalize teams.
*   **In-Class Exercise:** The second half of the class was dedicated to an in-class exercise involving running the regression models in the provided Jupyter Notebook, with the instruction that this exercise counts toward the final grade.
*   **AI Coding Guidance:** Students were reminded they can use Copilot or other AI tools for coding but must understand the generated code.

***

## Key Takeaways

*   The Group Project is the central focus of the course and requires immediate action on team formation and topic selection by the end of Week 3.
*   The project methodology involves rigorous data collection, including formal ATI requests to the government.
*   Quantitative skills, specifically **Linear Regression**, are essential tools for analyzing public opinion data and building evidence-based policy arguments.
*   Policy analysis requires linking quantitative findings (e.g., what factors drive support) with qualitative discourse analysis (how the government communicates).
*   Even with AI assistance, students must actively engage with the code and results to ensure they understand the underlying analytical process.

***

## Questions Raised

*   **Technical Question:** A student asked for clarification on how to properly download and open the Jupyter Notebook file from Moodle using VS Code, or alternatively, how to upload it to Google Colab.
*   **General Inquiry:** A student asked about the deadline for the in-class exercise (Instructor confirmed it could be submitted later that day, with optional follow-up questions on the 6th floor).