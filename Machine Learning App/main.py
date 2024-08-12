import streamlit as st
import pandas as pd
import plotly.express as pt




st.title("Hello To my Model")

df = pd.read_csv(r'https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
st.write(df)