import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
page_title="Tips Dashboard",
initial_sidebar_state='expanded',
layout='wide',
page_icon='🤑',
)


st.title("Tips Dashbord")

df = pd.read_csv('tip.csv')
# Explore The Data
st.write(df.head())

# Side Bar
with st.sidebar:
    st.image("4_tips._nutcd32.jpg")
    st.title("Tips Filtering")
    st.subheader("This Project is Dashborad for tibs and Total_bills by Sex and Smoker")

    Categorical = st.selectbox("Categorical Filter",[None,'sex','day','smoker'])
    Numerical = st.selectbox("Numerical Filter",[None,'total_bill','tip'])

    rowfilter = st.selectbox("Row Filter",[None,'sex','day','smoker'])
    colfilter = st.selectbox("Columns Filter",[None,'sex','day','smoker'])
    st.write("")
    st.write("This Project By ENG('Youssef Eissa😍')")


# Body And Visualization
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Max Total_bill",df['total_bill'].max())
with col2:
    st.metric("Min Total_bill",df['total_bill'].min())
with col3:
    st.metric("Max Tip",df['tip'].max())
with col4:
    st.metric("Min Tip",df['tip'].min())


# Scatter Plot
st.subheader("Tips VS Total_bills")
fig = px.scatter(df,x='tip',y='total_bill',color=Categorical,size=Numerical,facet_col=colfilter,facet_row=rowfilter)
st.plotly_chart(fig,use_container_width=True)


col5, col6, col7 = st.columns(3)
with col5:
    st.subheader("Total bill VS Sex")
    fig = px.bar(df, x='sex',y='total_bill', title="Distribution of total_bill by Sex",color=Categorical)
    st.plotly_chart(fig, use_container_width=True)
with col6:
    st.subheader("Male VS Female")
    fig = px.pie(data_frame=df, names='sex', title="Distribution of Sex")
    st.plotly_chart(fig, use_container_width=True)
with col7:
    st.subheader("Sex VS Tips")
    fig = px.bar(df, x='sex',y='tip', title="Distribution of Tips by Sex",color=Categorical)
    st.plotly_chart(fig, use_container_width=True)


col8, col9 = st.columns(2)
with col8: 
    st.subheader("Smoker VS Not Smoker")
    fig = px.pie(data_frame=df, names='smoker', title="Distribution of Sex")
    st.plotly_chart(fig, use_container_width=True)
with col9:
    st.subheader("Male VS Female")
    fig = px.pie(data_frame=df, names='day',values='tip', title="Tips for Days",hole=0.4)
    st.plotly_chart(fig, use_container_width=True)


col10, col11 = st.columns(2)
with col10:
    st.subheader("Total bill Distribution")
    fig = px.histogram(df, x='total_bill', title="Distribution of total_bill")
    st.plotly_chart(fig, use_container_width=True)
with col11:
    st.subheader("Total bill Distribution")
    fig = px.histogram(df, x='total_bill', title="Distribution of total_bill")
    st.plotly_chart(fig, use_container_width=True)
