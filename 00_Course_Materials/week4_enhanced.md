# Empowering Citizens through Data: Participatory Policy Analysis for Hong Kong - Week 4 Lecture Summary

## Executive Summary

Week 4 of the course focused on introducing essential technical prerequisites and diving into advanced quantitative reasoning tools, specifically **Simulation**, as a method for policy analysis. The session began with administrative necessities, requiring students to secure and utilize **API keys** from the HKBU ITO platform to access computational resources (tokens) for interacting with Large Language Models (LLMs) via a custom platform. This setup directly supports the course's unique assessment component: the **Reflective Essay**, which encourages students to use AI assistance while critically reflecting on course material and their group projects.

The core technical content, led by Tian Wu, transitioned from reviewing last week's regression concepts to introducing **Simulation** as the second major tool for policy analysis. This involved a detailed case study on evaluating bus route adjustments (City Bus No. 56) using simulation to predict changes in the **Seat Utilization Rate (KPI)**. The discussion emphasized the importance of identifying and modeling **random components** (travel time, passenger arrivals/departures) using appropriate probability distributions (Normal, Poisson, Binomial) and employing discrete event simulation frameworks like **SimPy**. The overarching goal is to equip students with the skills to use data-driven models to challenge or inform government decision-making, particularly in their group projects.

---

## Key Topics Covered

*   **Technical Setup:** API Key generation and usage for accessing HKBU General AI services.
*   **Assessment Component:** Introduction to the Reflective Essay (20% of grade) and its integration with AI tools.
*   **Data Visualization Review:** Appropriate use of Bar Charts vs. Scatter Plots, and detailed explanation of the **Box and Whisker Plot** (five-point summary, IQR, outliers).
*   **Regression Follow-up:** Limitations of Linear Regression for **Ordinal Categorical Responses** (suggesting Logistic/Ordinal Regression).
*   **Simulation Fundamentals:** Introduction to **Discrete Event Simulation (DES)** using the **SimPy** framework.
*   **Case Study:** Evaluating City Bus No. 56 route adjustments using simulation.
*   **Modeling Randomness:** Identifying and modeling random components using **Normal, Poisson, and Binomial Distributions**.
*   **Project Workflow:** Updates on team folders (Google Drive) and emphasis on documenting contributions.

---

## Main Discussion Points

### 1. Technical Setup and AI Access (Simon Wang)

*   **API Key Requirement:** Students must log in with HKBU credentials to generate an **API key** from the ITO platform. This key grants access to pre-purchased Microsoft Azure tokens for using the LLM services via a custom platform built for the course.
*   **API vs. GUI:** API (Application Programming Interface) allows programs to communicate with systems (like LLMs) via code protocols, contrasting with the conventional Graphical User Interface (GUI).

### 2. Reflective Essay and AI Integration (Simon Wang)

*   The **Reflective Essay** (20% of grade, 3 required) allows the use of AI chatbots, facilitated by the API key setup.
*   Students are instructed to use the provided AI tutor to reflect on the past four weeks (regression, simulation) and how these tools apply to their group projects.
*   **Criticality:** Students are warned that AI can **hallucinate**; critical evaluation of AI output is a required skill.
*   **Submission:** Essays are submitted via Moodle reply, and students must save/email their chat history before closing the browser, as the platform is new and may have bugs.

### 3. Project Management Updates (Simon Wang)

*   Google Drive folders have been created for the six teams. Students must ensure they have access.
*   Folders contain templates for **Meeting Notes**, **Data Collection Plan**, a **Worksheet** (spreadsheet), and a **Project Report/Outreach Document**.
*   **Documentation:** Students must document their contributions clearly in these shared documents for fair grading (50% of course grade is group-based).
*   The goal is to prepare inquiries to the government around the following week.

### 4. Data Visualization Review (Tian Wu)

*   **Categorical vs. Continuous Data:**
    *   When visualizing relationships between two **categorical variables** (like perceived fairness vs. support level), **Bar Charts showing percentages** across categories are more informative than scatter plots.
    *   **Scatter Plots** are best for visualizing relationships between two **continuous variables**.
*   **Box and Whisker Plot Deep Dive:**
    *   Used to show the **distribution of a continuous variable**.
    *   Detailed explanation of the **five-point summary**: Minimum, **Q1** (25th percentile), **Median** (Q2, 50th percentile), **Q3** (75th percentile), and Maximum.
    *   The box height represents the **Interquartile Range (IQR)** ($Q3 - Q1$).
    *   **Outliers** are data points falling outside the **inner fences** ($Q1 - 1.5 \times IQR$ and $Q3 + 1.5 \times IQR$).
    *   The plot helps infer distribution shape (e.g., right-skewed distributions have a mean pulled toward the right/larger values, unlike the median).

### 5. Regression Model Limitations (Tian Wu)

*   Linear regression is inappropriate when the response variable (Y) is **categorical** (like the 1-5 support scale), as it violates assumptions about the error term distribution.
*   For binary responses (0/1), **Logistic Regression** is used.
*   For ordinal categorical responses (like support levels), **Ordinal Regression** is more appropriate.

### 6. Simulation Case Study: Bus Route 56 (Tian Wu)

*   **Background:** Bus companies annually propose route adjustments to the Transport Department (TD). The case focuses on City Bus No. 56 in the North District.
*   **Criteria vs. Reality:** The criteria for increasing frequency (e.g., 90% load factor) seemed inconsistent with the reported 32% load factor for Bus 56, raising policy inquiry questions.
*   **Objective:** Develop and analyze a simulation of Bus 56 operations (before and after adjustments) using field data to predict the **Seat Utilization Rate (KPI)**.
*   **Simulation Design (DES):** Simulation mimics complex systems over time using logic, math, and computers. Events are processed chronologically.
*   **Random Components Modeled:**
    1.  **Travel Time between Stops:** Modeled using a **Normal Distribution**, parameterized by mean and standard deviation estimated from **ETA data**.
    2.  **Waiting Passengers at Stop:** Modeled using a **Poisson Distribution**, parameterized by $\lambda$ (average arrival rate per unit time, estimated from field data).
    3.  **Passengers Alighting:** Modeled using a **Binomial Distribution**, where the probability ($p$) of alighting is estimated from field observations at each stop.
*   **Implementation:** The **SimPy** library is used for Discrete Event Simulation. The process involves defining an environment, creating a generator function (which uses `yield` to pause time between events), adding the process to the environment, and running the simulation.
*   **Results Interpretation:** Simulation results (e.g., 1000 runs) were visualized using Box and Whisker Plots to compare the median seat utilization rate *before* and *after* the route adjustment. The analysis suggested the adjustment *reduced* utilization but increased operational costs.
*   **Policy Inquiries:** The simulation results lead to specific questions for the TD regarding data collection methods, evaluation criteria, and data availability/release.

---

## Important Concepts

*   **API (Application Programming Interface):** A set of rules and protocols allowing different software components to communicate.
*   **Token:** A unit of computation cost associated with using LLMs; tokens are not free.
*   **Reflective Essay:** An assessment component requiring critical thought on course concepts and project application, with AI assistance permitted.
*   **Box and Whisker Plot:** A standardized way of displaying the distribution of data based on a five-number summary (Min, Q1, Median, Q3, Max).
*   **IQR (Interquartile Range):** The range spanned by the middle 50% of the data ($Q3 - Q1$).
*   **Discrete Event Simulation (DES):** A modeling technique where the system state changes only at discrete points in time (events).
*   **SimPy:** A Python library framework for implementing DES.
*   **Normal Distribution:** A symmetric, bell-shaped distribution used here to model continuous random variables like **travel time**.
*   **Poisson Distribution:** A discrete distribution used to model the number of events occurring in a fixed interval of time or space, used here for **waiting passengers**.
*   **Binomial Distribution:** A discrete distribution modeling the number of successes in a fixed number of independent Bernoulli trials, used here for the **number of passengers alighting**.
*   **Seat Utilization Rate:** The Key Performance Indicator (KPI) for the bus simulation, calculated as (Passengers on Bus / Seat Capacity).

---

## Student Activities/Interactions

*   **API Key Generation:** Students were tasked with generating and securing their personal API keys during the start of the lecture.
*   **Reflective Essay Setup:** Students were guided on how to access the AI writing assistance platform using their keys and begin drafting their essay by discussing their project focus with the tutor.
*   **Data Visualization Review:** Tian Wu used examples from the municipal solid waste dataset to illustrate the correct application of Bar Charts and Box Plots.
*   **In-Class Exercise (Part 2):** Students were directed to work on the second in-class exercise, focusing on generating random variables (Normal and Poisson distributions) using NumPy and practicing the use of **Ghost Text** in GitHub Copilot for faster coding.
*   **Breakout Rooms:** Breakout rooms were set up for students to work on the exercise and discuss their group projects with teaching staff available for consultation.

---

## Key Takeaways

*   Securing and using the **API key** is crucial for accessing AI tools that support course assessments and learning.
*   Data visualization choices (Bar Chart vs. Box Plot) must align with the **type of data** being analyzed (categorical vs. continuous).
*   When modeling real-world systems where outcomes are uncertain (like bus travel times or passenger counts), **Simulation** is a powerful quantitative tool.
*   Effective simulation requires identifying **random components** and fitting them to appropriate **probability distributions** (Normal, Poisson, Binomial).
*   The simulation case study demonstrates how quantitative modeling can generate **evidence-based policy inquiries** by comparing predicted outcomes under different scenarios.
*   Students must actively document their contributions in shared team folders as they move toward project execution.

---

## Questions Raised

*   **API Access Issues:** A student reported being ineligible to use the API service; Simon Wang advised logging out and back in, or emailing him if the issue persists, confirming all names were submitted to ITO.
*   **Deadline Update:** Simon Wang noted he needed to update the Moodle page regarding the deadline for the Reflective Essay (suggested extension to October 5th).
*   **GitHub Education:** A student asked about the GitHub Education application process (Tian Wu confirmed the process and estimated 5-day processing time).
*   **Simulation Code Modification:** Students were advised on how to use the "Apply to this notebook" feature in the AI assistant to modify existing code snippets rather than copying and pasting.