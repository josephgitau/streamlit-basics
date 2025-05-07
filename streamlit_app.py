# import Libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Start of our app
st.title("Introduction to Streamlit Web App")

# Add a header
st.header("Basic Of Text (Header)")
st.subheader("Just basic text (Subheader)")

# Add a text
st.text("My name is Joseph And I am a Data Scientist")

# Add a markdown
st.markdown("## This is a markdown text")

## Add markdown with a list
st.markdown("""
## This is a sample list
- Python Basics
- Machine Learning
- Deep Learning
- Model Deplyment 
""")

st.write("Once installed, run Streamlit using the command `streamlit hello`")

st.latex(r"s \left ( t \right ) = ut + \dfrac{1}{2} at^2")
st.caption("This is a sample equation")

# Dipsplay Dataframes
st.header("Iris Dataset")
st.subheader("Iris Dataset Dataframe Sample")

# Load the iris dataset
df = sns.load_dataset("iris")

# Display the first 5 rows of the dataset
st.dataframe(df.head())

# Tables
st.subheader("Iris Dataset Table Sample")
st.table(df.head())

