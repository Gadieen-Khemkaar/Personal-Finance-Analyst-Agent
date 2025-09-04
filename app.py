import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Personal Finance Analyst", layout="wide")

st.title("💰 Personal Finance Analyst")

# Upload CSV
uploaded_file = st.file_uploader("📂 Upload your transactions CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Ensure columns exist
    if {"Date", "Description", "Amount"}.issubset(df.columns):
        # Convert Date column
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df = df.dropna(subset=["Date"])

        # Show raw data
        st.header("📑 Raw Transactions")
        st.dataframe(df)

        # Quick stats
        total_transactions = len(df)
        total_spend = df["Amount"].sum()

        st.header("📊 Quick Stats")
        col1, col2 = st.columns(2)
        col1.metric("Total Transactions", total_transactions)
        col2.metric("Total Spend", f"₹{total_spend}")

        # --- Categorization Logic ---
        def categorize(desc):
            desc = str(desc).lower()
            if "zomato" in desc or "swiggy" in desc:
                return "Food"
            elif "uber" in desc or "ola" in desc:
                return "Transport"
            elif "amazon" in desc or "flipkart" in desc or "myntra" in desc:
                return "Shopping"
            elif "salary" in desc:
                return "Income"
            else:
                return "Other"

        df["Category"] = df["Description"].apply(categorize)

        # Category breakdown
        # Category breakdown
        st.header("📂 Category Breakdown")
        cat_summary = df.groupby("Category")["Amount"].sum().abs()  # take absolute values

        fig1, ax1 = plt.subplots()
        ax1.pie(cat_summary, labels=cat_summary.index, autopct="%1.1f%%", startangle=90)
        ax1.axis("equal")
        st.pyplot(fig1)

        # Spend over time
        st.header("📈 Spend Trend")
        trend = df.groupby("Date")["Amount"].sum().abs()  # use abs for visualization

        fig2, ax2 = plt.subplots()
        trend.plot(kind="bar", ax=ax2)
        ax2.set_ylabel("Amount (₹)")
        ax2.set_title("Daily Spend")
        st.pyplot(fig2)

        # Category summary table
        st.subheader("📋 Category Summary")
        cat_df = cat_summary.reset_index()
        cat_df.columns = ["Category", "Total Spend (₹)"]
        cat_df["% of Total"] = (cat_df["Total Spend (₹)"] / cat_df["Total Spend (₹)"].sum() * 100).round(2)

        st.dataframe(cat_df)



    else:
        st.error("CSV must contain 'Date', 'Description', 'Amount' columns")
