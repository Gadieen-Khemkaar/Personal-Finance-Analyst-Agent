# 🗺️ Project Roadmap – Personal Finance Analyst Agent

## 📌 Overview

This project builds an **AI-powered Personal Finance Analyst Agent** that processes bank statements, auto-categorizes transactions, detects anomalies, generates insights with visualizations, and answers natural language queries about personal spending.

The end goal is a **Streamlit web app** where users can upload their statements, view dashboards, and chat with an AI assistant about their finances.

---

## 🗓️ Roadmap

### ✅ **Day 1 — Data Foundation**

* [ ] Collect or generate sample bank statement data (CSV/Excel).
* [ ] Preprocess transactions using **Pandas** (date parsing, clean descriptions).
* [ ] Implement basic rule-based **expense categorization** (Food, Travel, Shopping, Bills, Salary, Misc).
* [ ] Store processed data in Pandas DataFrame (optionally SQLite for querying).

**Deliverable:**
A script that takes a CSV and outputs categorized transactions.

---

### ✅ **Day 2 — Agentic AI Layer**

* [ ] Integrate **LLM (OpenAI/Groq)** with **LangChain**.
* [ ] Create tools for the agent:

  * `query_data`: fetch specific spend data.
  * `summarize`: explain spending trends.
* [ ] Implement **function-calling** so the agent can answer finance questions:

  * “How much did I spend on Zomato last month?”
  * “Which category had the highest expenses in July?”
  * “Show me suspicious transactions > ₹10,000.”
* [ ] Build a **CLI prototype** for Q\&A.

**Deliverable:**
A command-line chatbot that can answer queries about CSV transactions.

---

### ✅ **Day 3 — Insights & Dashboards**

* [ ] Implement **anomaly detection** (e.g., high-value transactions, unusual spending patterns).
* [ ] Build **visualizations** using Matplotlib/Plotly:

  * Category-wise spending (Pie Chart).
  * Monthly expense trend (Line Chart).
  * Savings vs Expenses trend.
* [ ] Create a **Streamlit app**:

  * File uploader (upload CSV).
  * Dashboard with charts + summary.
  * Chatbox for agent queries.

**Deliverable:**
Interactive **Streamlit dashboard** + agent chatbot.

---

### ✅ **Day 4 — Advanced Features & Polish**

* [ ] Upgrade expense categorization with **LLM-powered classification**.
* [ ] Add **smart financial insights**:

  * “Top 3 merchants this month are …”
  * “Cutting food delivery by 20% saves you ₹X/year.”
* [ ] Export **PDF Monthly Report** with charts + insights.
* [ ] Polish UI (Streamlit cards, icons).
* [ ] Add **README, demo video/GIF, and deployment link**.

**Deliverable:**
Production-ready **AI Personal Finance Analyst Web App**.

---

## 🛠️ Tech Stack

* **Data Handling:** Python, Pandas, SQLite (optional).
* **AI Agent:** LangChain, OpenAI/Groq API.
* **Frontend:** Streamlit.
* **Visualization:** Matplotlib / Plotly.
* **Reporting:** ReportLab / FPDF.

---

## 🎯 Final Outcome

A **resume-ready project** demonstrating:

* End-to-end data processing.
* Agentic AI (tool use + reasoning).
* Interactive dashboards.
* Real-world financial insights.

