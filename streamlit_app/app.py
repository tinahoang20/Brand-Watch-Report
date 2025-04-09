import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Brand Watch Dashboard", layout="wide")

# Load data safely
DATA_PATH = os.path.join("..", "data", "combined_cleaned_data.csv")
if os.path.exists(DATA_PATH):
    df = pd.read_csv(DATA_PATH)
else:
    st.error("Data file not found. Please ensure combined_cleaned_data.csv exists in data/.")
    st.stop()
