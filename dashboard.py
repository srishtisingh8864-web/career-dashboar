import streamlit as st
import pandas as pd

# Title
st.title("📊 Career Progression Dashboard")

# Load data
df = pd.read_csv("final_output.csv")

# Sidebar filters
st.sidebar.header("Filters")

dept = st.sidebar.selectbox("Select Department", df['Department'].unique())
score = st.sidebar.selectbox("Promotion Gap Score", df['PromotionGapScore'].unique())

# Filter data
filtered_df = df[
    (df['Department'] == dept) &
    (df['PromotionGapScore'] == score)
]

# Show data
st.subheader("Filtered Employees")
st.dataframe(filtered_df)

# Cluster Distribution
st.subheader("Cluster Distribution")
st.bar_chart(filtered_df['Cluster'].value_counts())

# Retention Risk
st.subheader("High Retention Risk Employees")
risk_df = filtered_df[filtered_df['RetentionRisk'] == True]
st.dataframe(risk_df)

# KPIs
st.subheader("Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Total Employees", len(filtered_df))
col2.metric("High Risk", len(risk_df))
col3.metric("Avg Promotion Gap", round(filtered_df['PromotionGapRatio'].mean(), 2))