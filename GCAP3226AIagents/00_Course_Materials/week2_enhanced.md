# Empowering Citizens through Data: Participatory Policy Analysis for Hong Kong

## Week 2 Lecture Transcript Enhancement

---

## Executive Summary

This session marked the second week of the course **GCAP 3226: Empowering Citizens through Data**, focusing on introducing the essential analytical tools required for data-informed policymaking in Hong Kong. A key highlight of the week was the introduction to using **Artificial Intelligence (AI)**, specifically **GitHub Copilot**, to assist in writing programming code (Python) for data analysis, making the course accessible even to students with no prior programming background. The lecture provided a roadmap overview, noting that group formation and project selection would commence in Weeks 3 and 4.

The core of the session involved setting up the technical environment and providing context for the initial hands-on data analysis task. The context was established through a detailed review of a survey questionnaire concerning Hong Kong's proposed **Municipal Solid Waste Charging Policy**. This policy, which aims to reduce waste based on the **polluter-pays principle**, served as the dataset for the upcoming data visualization exercises. The instructors emphasized patience during the technical setup phase and encouraged students from diverse backgrounds to collaborate.

---

## Key Topics Covered

*   Course logistics recap (recordings, Moodle access).
*   Course roadmap overview (Weeks 1-onwards).
*   Introduction to technical tools: **Jupyter Notebook**, **VS Code**, and **GitHub Copilot**.
*   Contextual deep dive into the **Municipal Solid Waste Charging Policy** survey data.
*   Explanation of the survey structure, focusing on policy support as the response variable and potential influencing factors.
*   Technical setup instructions and demonstration of the VS Code interface.
*   Breakdown of the different modes within GitHub Copilot (Ask vs. Agent).

---

## Main Discussion Points

### 1. Course Logistics and Roadmap

**Simon Wang:**
*   Lectures for the first two weeks are recorded via Zoom; students should catch up on Week 1 materials (video/transcripts) on Moodle.
*   The course objectives and hub information are available but the focus remains on Moodle notes to avoid overwhelming students.
*   **Roadmap:** Currently in Week 2. Group formation and topic selection are deferred due to the shopping period.
*   The course will immediately introduce using **AI to write programming codes**—a highlight intended to be tackled early ("eat the frog first").
*   Students from Computer Science majors are asked to assist their peers.
*   Weeks 3 and 4 will focus on case studies, group formation, and project selection.
*   The instructors aim to make the course **friendly to everybody**, especially those without math or computer science backgrounds, offering support throughout.

### 2. Technical Setup and Tools Introduction

**Simon Wang:**
*   Students need to download the Week 2 materials (a **zip file**) from Moodle.
*   The zip file contains a **CSV file** (the data, similar to a spreadsheet) and a **Jupyter Notebook** (the code file).
*   To run the Jupyter Notebook, students must install **VS Code** (code editor).
*   The goal today is to introduce analytical tools, including **GitHub Copilot**, which enables teaching this course effectively even to those with **zero programming background**.

**Tayle (Dr. Wu):**
*   The technical part focuses on **Data Visualization with GitHub Copilot**.
*   The tools are essential for **data-informed policymaking in Hong Kong**.
*   **Jupyter Notebook:** An interactive tool for writing and running code, viewing results immediately, and adding notes (using **code cells** and **markdown cells**).
*   **VS Code Interface:** Briefly explained the Activity Bar (for extensions like Copilot), Sidebar (file explorer), Editor Panels (where code is typed), and the Output/Terminal Panel.

### 3. Contextualizing the Data: Waste Charging Policy Survey

**Tayle (Dr. Wu):**
*   The data comes from a survey on Hong Kong's **Municipal Solid Waste Charging Policy**, which has been postponed multiple times since its framework was published in 2005.
*   **Survey Aim:** To understand residents' awareness, attitudes, and waste management behaviors related to the policy.
*   **Response Variable:** The level of **support for the policy**.
*   **Potential Influencing Factors (Conceptual):** Perceived fairness (based on the polluter-pays principle), perceived government responsiveness to public opinion, perceived helpfulness in reducing waste volume, and perceived severity of the waste management issue.
*   **Potential Influencing Factors (Practical/Behavioral):** Household waste disposal habits (amount of garbage), recycling habits, knowledge about recycling, and demographic information (education, age, income).

### 4. Data Encoding and Practical Considerations

**Tayle (Dr. Wu):**
*   The **support level** variable in the CSV file is coded numerically (1 to 5, representing **strongly opposed** to **strongly support**), reflecting its **ordinal** nature.
*   **Conceptual vs. Practical Factors:** The survey focuses on conceptual factors (fairness, responsiveness). The discussion pivoted to practical controversies, such as the **sufficiency of recycling facilities**.
*   Data analysis could determine if facility capacity is the real bottleneck (e.g., if utility rates are 90%, more resources are needed; if utility rates are low, promotion is needed). This highlights the need for accessing and analyzing government-collected data.

### 5. Post-Break Technical Focus: Setting up Copilot

**Simon Wang:**
*   Students were asked to check if they had installed **VS Code** and downloaded the zip file.
*   **GitHub Copilot** is the AI assistant integrated into VS Code.
*   **Setup Steps:** Install VS Code, open the unzipped folder, install the **GitHub Copilot extension** via the extension panel, and log in using a **GitHub account**.
*   Students are encouraged to be proud of having a GitHub account, as it connects them to an open-source community.
*   University students can apply for **GitHub Education** benefits later, though the free account should suffice for this project.

**Simon Wang (Demonstration):**
*   Demonstrated opening the folder in VS Code, showing the three main files: **CSV** (data), **PDF** (slides), and **IPYMB** (Jupyter Notebook).
*   Showed how to access the **Extensions** panel (the four squares icon) to install **GitHub Copilot**.
*   Recommended starting with the **Ask mode** in Copilot for beginners, as the **Agent mode** can be too hands-off initially.
*   If command-line operations (like `pip`) are needed, students should use the integrated terminal within VS Code (top right corner icon).

---

## Important Concepts

*   **Municipal Solid Waste Charging Policy:** A proposed policy in Hong Kong based on the **polluter-pays principle** where fees are based on the volume of waste disposed, aiming to reduce waste and promote recycling.
*   **Polluter-Pays Principle:** The concept that those who produce pollution or waste should bear the costs of managing it.
*   **Jupyter Notebook (.ipynb):** An interactive computing environment that allows users to create and share documents containing live code, equations, visualizations, and narrative text.
*   **VS Code (Visual Studio Code):** A popular, free source-code editor used here as the primary interface for running Python code and managing the Jupyter Notebook.
*   **GitHub Copilot:** An AI pair programmer that suggests code and functions in real-time within the editor, drastically lowering the barrier to entry for coding tasks.
*   **Ordinal Data:** Data that has a natural, ordered relationship, such as the 1-to-5 scale for policy support (Strongly Opposed to Strongly Support).

---

## Student Activities/Interactions

*   **Attendance Check:** Instructors confirmed who was watching the recording versus attending live.
*   **Technical Setup Check:** Students were asked to raise their hands if they had installed VS Code and downloaded the necessary files.
*   **Peer Support:** Computer Science majors were asked to stand up to offer help to others during the setup phase.
*   **Q&A during Break:** Students were encouraged to ask questions about the setup during the break, with the plan to establish a WhatsApp group next week for ongoing discussion.

---

## Key Takeaways

*   The course leverages **AI tools (GitHub Copilot)** to enable data analysis for students regardless of their programming background.
*   The initial hands-on task involves using Python/Jupyter Notebooks to visualize data from a survey on Hong Kong's **Waste Charging Policy**.
*   Understanding the **context** of the data (the policy's background, goals, and controversies) is crucial before visualization.
*   The technical setup requires installing **VS Code** and the **GitHub Copilot extension**.
*   Students are encouraged to embrace the technical challenge as a means to step outside their comfort zone and gain familiarity with modern data tools.

---

## Questions Raised

*   *Implicit Question:* How will students using tablet computers (like iPads) manage the required software installation? (Answer: Encouraged to use a mobile computer next week, but can follow along now).
*   *Implicit Question:* Do students need to register for GitHub to use Copilot? (Answer: Yes, logging in via GitHub is required after installing the extension).
*   *Implicit Question:* Should beginners use the advanced **Agent Mode** in Copilot? (Answer: No, start with the **Ask mode** for more control).