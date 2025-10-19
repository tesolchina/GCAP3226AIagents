# Lecture Transcript Enhancement: Empowering Citizens Through Data: Participatory Policy Analysis for Hong Kong (Week 1)

## Executive Summary

This document summarizes the introductory lecture for the course **"Empowering Citizens Through Data: Participatory Policy Analysis for Hong Kong."** The course is a unique, **transdisciplinary collaboration** between the Mathematics Department and the Language Centre, aiming to equip students with both quantitative reasoning skills (data science, statistics) and qualitative communication abilities (policy analysis, advocacy). The fundamental motivation is to **empower citizens** by enabling them to critically review government policy through data analysis and engage constructively with public policy-making processes.

The core mission of the course is to investigate the extent to which the Hong Kong government currently employs **data-informed policymaking**. To achieve this, students will learn to utilize the **Access to Information (ATI) Code** to formally request data and insights from government departments. Following data acquisition, students will apply mathematical models, such as **optimization and linear regression**, implemented via **Python and AI-assisted programming (GitHub Copilot)**, to propose data-driven improvements to existing policies. The course structure emphasizes practical application, group projects, and the ethical integration of new technologies like AI into policy analysis workflows.

---

## Key Topics Covered

*   Course structure, unique co-hosting arrangement (Maths and Language departments).
*   The core motivation: Empowering citizens through data-driven policy participation.
*   The central empirical question: To what extent does the HK government use data for decision-making?
*   Methodology: Utilizing the **Access to Information (ATI) Code** for data requests.
*   Technological tools: Python, Jupyter Notebooks, and **AI-assisted programming (GitHub Copilot)**.
*   Mathematical models to be covered: **Optimization** (via simulation modeling) and **Linear Regression**.
*   Course assessment structure and workload.
*   Introduction to **Customized Chatbots** and the HKBU General AI Platform API.
*   Case study introduction: Data governance issues exemplified by the "Bus App" problem.

---

## Main Discussion Points

### 1. Course Uniqueness and Collaboration

**Simon Wang:**
*   The course is co-hosted by the **Mass Department** and the **Language Centre**, a rare transdisciplinary collaboration between a math teacher and a language teacher.
*   This combination is crucial because real-world problem-solving requires both **quantitative reasoning** (essential in the age of big data and AI) and **qualitative skills** (critical thinking, strong writing, humanities perspective).
*   **Talia** brings a strong quantitative background (PhD in Math, statistical modeling for public health), while Simon leverages expertise in engaging with the government from a **citizen's role**—questioning practices and critically reviewing policy.

### 2. Course Objectives and Central Mission

**Simon Wang:**
*   **Objective:** To offer analytical tools to enable **data-informed policymaking**.
*   **Key Question:** To what extent are Hong Kong government staff actually making decisions based on data? (The short answer is: **We don't know**, because the government doesn't readily disclose this information.)
*   **Mission:** Students, as a team, are tasked with finding out the extent of data usage in government decisions. The likely disappointing finding will serve as a foundation to argue for a **data-driven approach** to achieve better policies.
*   **Process:**
    1.  Evaluate current government policy analysis practices.
    2.  Use data acquisition methods to uncover practices.
    3.  Propose a **better way** using mathematical models and analytics (Talia's role).
    4.  Present the argument (current practice vs. proposed better way) to **lawmakers** (the gatekeepers).

### 3. Data Acquisition: Access to Information (ATI) Code

**Simon Wang:**
*   The course will take a **fresh approach** using the **Code on Access to Information (Gonhoi Jiu Xiaoza)**.
*   Students will send direct questions to specific government departments regarding their data usage in policy decisions.
*   **Time Constraint Warning:** The government has a standard reply time of **3 weeks**, extendable by another **7 weeks** under exceptional circumstances. This necessitates careful planning and potentially breaking down inquiries into smaller, separate applications.

### 4. Mathematical Tools and Implementation

**Talia:**
*   The course will involve programming languages to implement mathematical models, specifically **Python**.
*   **AI-Assisted Programming:** The textbook referenced is *Learn AI Assisted Python Programming*. The primary tool will be **GitHub Copilot** for syntax and code generation.
*   **Mathematical Models:** The course will focus on two types of models applied to case studies:
    1.  **Optimization:** Used for problems involving minimizing cost/waste or maximizing profit/efficiency (e.g., finding the shortest path, minimizing study time).
    2.  **Linear Regression:** Used to study relationships between variables (e.g., how population density impacts service demand, or factors influencing support for the garbage bag charging scheme).

### 5. Simulation Modeling (Optimization Case Study)

**Talia & Simon Wang:**
*   Instead of theoretical methods, **simulation modeling** (a "virtual experiment") will be used for optimization problems.
*   **Bus Frequency Case Study (Bus Route 56):** A previous student project simulated bus operations to calculate the **bus seat occupation rate (KPI)**.
    *   Data collected in the field (passenger counts) provided the empirical foundation for simulation parameters.
    *   **Data Governance Link:** Simon highlighted that this manual collection points to **untapped potential** if the Transport Department shared operational data (e.g., Octopus card data) held by bus companies.
*   **Purpose of Simulation:** To model complex systems, assess dynamic behavior, and test **"what-if" scenarios** (e.g., changing frequency from 30 to 20 minutes) in a cheaper, safer virtual environment, providing quantitative justification where government criteria are currently vague.

### 6. AI and Programming Accessibility

**Simon Wang & Talia:**
*   **Accessibility for Non-Math Students:** Students should not worry about a strong math background. The math content will not exceed introductory statistics/mathematics levels.
*   **AI Support:** AI tools like Copilot significantly lower the barrier to entry for programming.
    *   **Vibe Coding:** Using natural language prompts to generate code.
    *   **For Zero Programmers:** Use a general AI chatbot first to generate a framework, then move to Copilot for refinement.
*   **New Programming Skills:** The focus shifts from mastering syntax to developing two key skills:
    1.  **Breaking down large problems** into smaller, manageable tasks for the AI.
    2.  **Prompt Engineering** (precise communication with the AI).

### 7. Customized Chatbots and Learning Companions

**Simon Wang:**
*   Introduction to **Customized Chatbots** using the **HKBU General AI Platform API**.
*   **API (Application Programming Interface):** Explained as the protocol/agreement allowing one program to communicate with a remote server/program using code, requiring an **API Key** for access.
*   **Socratic Dialogue Partner:** A prototype chatbot designed to guide students through questions using the Socratic method, rather than providing direct answers, fostering deeper exploration.
*   **GCAP Social Issues Analyst:** A second chatbot customized specifically for this course, capable of assisting with data-driven analysis, information requests, and model selection.
*   **Learning Outcome:** These tools aim to provide a **personalized learning experience** and act as "learning buddies" contextualized to the course material.

### 8. Case Study: Data Governance and Citizen Action

**Simon Wang:**
*   **Bus App Case:** Two bus stops with the same name caused confusion and missed buses due to poor data quality.
*   **Resolution:** Persistent engagement (including escalating to an Assistant Director) led the bus company to add distinguishing codes, highlighting that **citizen pressure can effect change**.
*   **Lesson:** This is fundamentally a **data governance problem**—the need for clean, high-quality, and accessible data.

---

## Important Concepts

*   **Transdisciplinary Collaboration:** Combining expertise from vastly different fields (Math and Language) to solve complex problems.
*   **Data-Informed Policymaking:** The principle that public decisions should be guided and validated by empirical data.
*   **Access to Information (ATI) Code:** A legal framework used by citizens to formally request non-public government information.
*   **Simulation Modeling:** Using computer models (virtual experiments) to mimic complex, dynamic systems over time to test scenarios.
*   **Optimization:** Mathematical approach focused on finding the best possible outcome (maximum or minimum) under given constraints.
*   **Linear Regression:** A statistical method used to model the linear relationship between a dependent variable and one or more independent variables.
*   **GitHub Copilot:** An AI programming assistant that suggests code completions based on context and natural language comments.
*   **Prompt Engineering:** The skill of crafting precise inputs (prompts) to guide Large Language Models (LLMs) to produce desired outputs.
*   **API (Application Programming Interface):** A set of rules and protocols that allows different software applications to communicate with each other programmatically.
*   **Data Governance:** The overall management of data availability, usability, integrity, and security throughout its lifecycle.

---

## Student Activities/Interactions

*   **Discussion with Eric:** Asked about the extent of government data usage.
*   **Discussion with Bonnie:** Shared observations about government projects mixing data with "vision," referencing consulting firms.
*   **Class Survey:** Quick poll on students' math/science backgrounds.
*   **AI Tutor Setup:** Students were guided through setting up an account on the HKBU General AI platform to generate an **API Key** for accessing customized chatbots.
*   **Hands-on Setup:** Students were encouraged to install necessary software (Python, VS Code, Copilot setup guide provided in Moodle) for the following week's hands-on session.
*   **Break:** A 5-minute break was taken after the simulation discussion.

---

## Key Takeaways

*   This course uniquely merges quantitative data analysis with qualitative policy engagement.
*   The primary goal is to empirically investigate and challenge the level of **data-driven decision-making** within the Hong Kong government.
*   Students will learn practical skills in **ATI requests**, **Python programming**, and **AI-assisted development**.
*   Mathematical tools will be focused on **simulation (optimization)** and **regression**, kept accessible to all backgrounds.
*   The course embraces the use of **AI tools** (like Copilot and custom chatbots) as essential components of modern policy analysis workflows.
*   Citizen action, when executed correctly (e.g., persistent, evidence-based engagement), can lead to tangible improvements in public services (e.g., data quality).

---

## Questions Raised

*   **Simon Wang (to the class):** To what extent is the Hong Kong government making decisions based on data?
*   **Simon Wang (to the class):** How are we going to find out the extent of government data usage? (Leading to the ATI discussion).
*   **Simon Wang (to the class):** Given the limited field data used for the bus simulation, how do we assess the usefulness or validity of that simulation?
*   **Talia (Response to validity question):** Model validity depends heavily on the **quality and accurate estimation of key parameters** derived from data, as well as the correctness of the overall simulation logic.
*   **Simon Wang (Follow-up):** What is the purpose of doing the simulation if we only have limited data? (Answered by showing how simulation quantifies the vague criteria used by the Department of Transportation).
*   **General Class Questions:** Questions regarding the math prerequisites and the accessibility of the programming components were raised and addressed.