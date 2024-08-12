import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(
    page_icon='🤖',
    page_title='ML Model',
    initial_sidebar_state='expanded',
    layout='wide',
)

st.title("ML Model App")
st.title("This app builds a Macine Learning model!")

# Reading the Data
df = pd.read_csv(r'https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

# Explore the Data
with st.expander("Explore The Data"):
    st.subheader("All Data")
    st.write(df)
    st.subheader("X Data")
    X = df.drop('species',axis=1)
    st.write(X)
    st.subheader("Y Data")
    y_raws = df['species']
    st.write(y_raws)

# "species","island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"
with st.expander("Visualization the Data"):
    fig = px.scatter(data_frame=df,x='bill_length_mm',y='body_mass_g',color='species')
    st.plotly_chart(fig,use_container_width=True)

# Data preparation
with st.sidebar:
    st.header('Input Features')
    island = st.selectbox('Island : ', [None,'Torgersen','Biscoe','Dream'])
    gender = st.selectbox('Gender : ' , [None,'male','female'])
    bill_length_mm = st.slider('bill_length_mm : ',32.1,59.6,43.9)
    bill_depth_mm = st.slider('bill_depth_mm : ',13.1,21.5,17.2)
    flipper_length_mm = st.slider('flipper_length_mm : ',172.00,231.00,201.00)
    body_mass_g = st.slider('body_mass_g : ',2700.00,6300.00,4207.00)

    # Create Date frame for input Features
    data = {
        "island" : island,
        "bill_length_mm" : bill_length_mm,
        "bill_depth_mm" : bill_depth_mm,
        "flipper_length_mm" : flipper_length_mm,
        "body_mass_g" : body_mass_g,
        'sex' : gender
    }
    inputdf = pd.DataFrame(data,index=[0])
    inputpenguines = pd.concat([inputdf,X],axis=0)

     # Encoder X
    encode = ['island','sex']
    df_peuguines =pd.get_dummies(inputpenguines,prefix=encode)
    input_row = df_peuguines[:1]

    # Encoder Y 
    encodeY = {'Adelie':0,'Gentoo':1,'Chinstrap':2}
    def target_encode(val):
        return encodeY[val]
    
    y = y_raws.apply(target_encode)
    
    st.write("")
    st.write("Made By Eng: Youssef Eissa🤖")

with st.expander('Input Features'):
    st.write('Input Penguines')
    inputdf
    st.write('Date frame for input Features')
    inputpenguines
    st.write('Encoded Input')
    input_row
    st.write('Encoded Y')
    y

with st.expander('Data Preparation'):
    st.write('Encoded Input Penguies [X]')
    input_row
    st.write('Encoded Y')
    y


# Build The Model
## Train The Model
RFC = RandomForestClassifier()
RFC.fit(df_peuguines[1:],y)


## Apply Model to make Predtictions
predict = RFC.predict(input_row)
predict_prob = RFC.predict_proba(input_row)
newdf = pd.DataFrame(predict_prob)
newdf.columns=['Adelie',
                     'Chinstrap',
                     'Gentoo']


# Display Prediected Species

st.subheader('Prediected Species')
newdf

Prediected_Species=np.array(['Adelie',
                     'Chinstrap',
                     'Gentoo'])

st.success(str(Prediected_Species[predict][0]))