# 💰 Personal Finance Analyst Agent

## 📌 Overview

The **Personal Finance Analyst Agent** is an **AI-powered tool** that helps users analyze their bank statements with ease.
It automatically:

* Categorizes transactions (Food, Travel, Shopping, Bills, Salary, etc.).
* Detects anomalies and unusual spending patterns.
* Generates interactive **dashboards and charts**.
* Answers **natural language questions** like:

  * *“How much did I spend on Zomato last month?”*
  * *“Which category had the highest expenses in July?”*
  * *“Show me suspicious transactions > ₹10,000.”*

This project demonstrates **agentic AI**, **data analysis**, and **automation** — making it a practical resume-ready project.

---

## ✨ Features

* 📂 Upload CSV/Excel bank statements.
* 🧾 Automatic expense categorization (rule-based + LLM-powered).
* 📊 Interactive dashboard with charts (Streamlit + Plotly/Matplotlib).
* 🤖 AI-powered financial assistant (LangChain + LLMs).
* ⚠️ Anomaly detection for unusual spending.
* 📑 Exportable monthly PDF financial report.

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Data Handling:** Pandas, SQLite (optional)
* **AI Agent:** LangChain + OpenAI/Groq API
* **Frontend:** Streamlit
* **Visualization:** Matplotlib / Plotly
* **Reporting:** FPDF / ReportLab

---

## 📂 Project Structure

```
├── data/               # Sample bank statement CSVs
├── src/                # Source code
│   ├── preprocessing.py
│   ├── categorization.py
│   ├── agent.py
│   ├── dashboard.py
│   └── report_generator.py
├── app.py              # Streamlit main app
├── requirements.txt    # Dependencies
├── ROADMAP.md          # Project execution plan
└── README.md           # Project documentation
```

---

## ⚡ Quick Start

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/personal-finance-analyst.git
cd personal-finance-analyst
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App

```bash
streamlit run app.py
```

---

## 🗓️ Project Roadmap

Check out the detailed [ROADMAP.md](./ROADMAP.md) to see how this project was planned and executed step by step.

---

## 🎥 Demo

🚧 *Coming soon – add a GIF or video demo here once the app is functional.*

---

## 📌 Resume Pitch

> *Built an agentic AI Personal Finance Analyst that processes bank statements, auto-categorizes transactions using LLMs, detects anomalies, generates interactive dashboards, and answers natural language queries about spending trends. Deployed as a Streamlit app with PDF report generation.*

