# streamlit_app/app.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Brand Watch Dashboard", layout="wide")

# Load data
df = pd.read_csv("../data/content_with_sentiment.csv")
df['post_date'] = pd.to_datetime(df['post_date'])

# Sidebar filters
st.sidebar.title("🔎 Filter Options")
brand = st.sidebar.selectbox("Select Brand", df['brand'].unique())
start_date = st.sidebar.date_input("From Date", df['post_date'].min())
end_date = st.sidebar.date_input("To Date", df['post_date'].max())

# Filtered DataFrame
filtered = df[(df['brand'] == brand) &
              (df['post_date'] >= pd.to_datetime(start_date)) &
              (df['post_date'] <= pd.to_datetime(end_date))]

st.title(f"📊 {brand} Analysis Dashboard")

col1, col2 = st.columns(2)
with col1:
    st.subheader("🗳 Sentiment Distribution")
    st.bar_chart(filtered['sentiment'].value_counts())

with col2:
    st.subheader("🔥 Engagement Over Time")
    daily = filtered.set_index('post_date').resample('W')['engagement'].sum()
    st.line_chart(daily)

st.subheader("🏷️ Top Hashtags")
hashtags = filtered['content'].str.findall(r"#\\w+").explode()
st.dataframe(hashtags.value_counts().head(10).reset_index().rename(columns={'index': 'Hashtag', 0: 'Count'}))

st.subheader("✨ Most Engaging Post")
top_post = filtered.sort_values('engagement', ascending=False).iloc[0]
st.write(f"**Date:** {top_post['post_date'].strftime('%Y-%m-%d')}  \n**Engagement:** {int(top_post['engagement'])}")
st.info(top_post['content'])

