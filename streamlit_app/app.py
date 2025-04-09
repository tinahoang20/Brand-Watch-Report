import streamlit as st
import pandas as pd
import plotly.express as px
import os

# ----------------------------
# Configurations
# ----------------------------
st.set_page_config(page_title="Brand Watch Dashboard", layout="wide")
st.title("📊 Brand Watch Report – Coke, Pepsi & Fanta")

# ----------------------------
# Load Data
# ----------------------------
data_path = os.path.join("..", "data", "combined_cleaned_data.csv")

if not os.path.exists(data_path):
    st.error("❌ Data file not found at ../data/combined_cleaned_data.csv")
    st.stop()

# Read and process data
df = pd.read_csv(data_path)
df['time'] = pd.to_datetime(df['time'], errors='coerce')
df.dropna(subset=['time'], inplace=True)

# ----------------------------
# Sidebar Filters
# ----------------------------
st.sidebar.header("🔎 Filter Options")
brands = st.sidebar.multiselect("Select Brand(s):", df['brand'].unique(), default=df['brand'].unique())
platforms = st.sidebar.multiselect("Select Platform(s):", df['platform'].unique(), default=df['platform'].unique())

filtered_df = df[df['brand'].isin(brands) & df['platform'].isin(platforms)]

# ----------------------------
# Monthly Post Volume
# ----------------------------
st.subheader("🗓️ Monthly Posting Activity")
monthly = filtered_df.copy()
monthly['month'] = monthly['time'].dt.to_period("M").astype(str)
monthly_grouped = monthly.groupby(['month', 'brand']).size().reset_index(name='post_count')
fig1 = px.bar(monthly_grouped, x='month', y='post_count', color='brand', barmode='group',
              labels={'month': 'Month', 'post_count': 'Number of Posts'}, height=400)
st.plotly_chart(fig1, use_container_width=True)

# ----------------------------
# Average Engagement by Brand
# ----------------------------
st.subheader("📈 Average Engagement by Brand")
engage = filtered_df.groupby('brand')[['likes', 'comments', 'shares']].mean().round(1).reset_index()
st.dataframe(engage)

# ----------------------------
# Sentiment Distribution (if available)
# ----------------------------
if 'sentiment' in filtered_df.columns:
    st.subheader("😊 Sentiment Distribution")
    sentiment_counts = filtered_df.groupby(['brand', 'sentiment']).size().reset_index(name='count')
    fig2 = px.bar(sentiment_counts, x='brand', y='count', color='sentiment', barmode='group', height=400)
    st.plotly_chart(fig2, use_container_width=True)

# ----------------------------
# Display Raw Data
# ----------------------------
with st.expander("🔍 Show Raw Data"):
    st.dataframe(filtered_df.reset_index(drop=True))
