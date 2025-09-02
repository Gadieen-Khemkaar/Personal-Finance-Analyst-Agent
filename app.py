import streamlit as st
import pandas as pd

st.set_page_config(page_title="Personal Finance Analyst", page_icon="💰", layout="wide")

st.title("💰 Personal Finance Analyst Agent")
st.write("Upload your bank statement CSV and get insights about your spending.")

# File uploader
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)
    st.subheader("📂 Raw Transactions")
    st.dataframe(df.head())

    # Basic stats
    st.subheader("📊 Quick Stats")
    st.write("Total Transactions:", len(df))
    if "Amount" in df.columns:
        st.write("Total Spend:", df["Amount"].sum())
    else:
        st.warning("No 'Amount' column found in CSV. Please check your data format.")
else:
    st.info("👆 Upload a CSV file to begin analysis.")
