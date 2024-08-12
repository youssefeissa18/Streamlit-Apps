import streamlit as st

st.header("Hello Youssef")
st.sidebar.title('First Project')


Shape = st.selectbox("Chosse the Shape",['Circle','Rectangle'])


if Shape == 'Circle':
    radius = st.number_input('Radius ' , min_value=0,max_value=100,step=1)
    area = radius * radius * 3.14
    perimeter = radius * 2 * 3.14


if Shape == 'Rectangle':
    Height = st.number_input('Height ' , min_value=0,max_value=100,step=1)
    Width = st.number_input('Width ' , min_value=0,max_value=100,step=1)
    area = Width * Height
    perimeter = (Width+Height)*2

    
computebutton = st.button('Compute area and perimeter')
if computebutton:
    st.write('Area = ', area)
    st.write('perimeter = ' , perimeter)