import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

@st.cache_data

def cache(file):
    return pd.read_csv(file)

file = st.file_uploader("Upload CSV file",type=['csv'])

if file is not None:
    df = cache(file)

    n_row = st.slider('Choose Number of Rows',min_value=1,max_value=len(df),step=1)
    columns = st.multiselect('Columns Show',df.columns.to_list(),default=df.columns.to_list())
    numcol = df.select_dtypes(include=np.number).columns.to_list()
    st.write(df[:n_row][columns])
    col1, col2, col3 = st.columns(3)
    with col1:
        Xaxis = st.selectbox('Select on X Axis : ' , numcol)
    with col2:
        yaxis = st.selectbox('Select on Y Axis : ' , numcol)
    with col3:
        color = st.selectbox('Color Columns ', df.columns)
    
    tab1, tab2 = st.tabs(["Scatter", "Histogram"])
    with tab1:
        Scatter = px.scatter(df,x=Xaxis,y=yaxis,color=color)
        st.plotly_chart(Scatter)
        st.plotly_chart(Scatter)
    with tab2:
        hist_feature = st.selectbox("Select Features :",numcol)
        fig_hist = px.histogram(df,x=hist_feature)
        st.plotly_chart(fig_hist)
