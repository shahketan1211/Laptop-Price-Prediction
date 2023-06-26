import streamlit as st
import pickle
import numpy as np

#importing dataframe and model 
model=pickle.load(open('model.pkl','rb'))
df=pickle.load(open('df.pkl','rb')) 

#background image
page_bg_img = '''
<style>
.stApp {
background-image: url("https://coolbackgrounds.io/images/backgrounds/index/compute-ea4c57a4.png");
background-repeat: no-repeat;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
   
st.title("Laptop Price Prediction".upper())

#select the Brand
Company=st.selectbox(label='Brand',options=df['Company'].unique())

#select type of laptop
TypeName=st.selectbox(label='TypeName',options=df['TypeName'].unique())

#select RAM
Ram=st.selectbox(label='RAM(In GB)',options=[2,4,6,8,10,12,16,32])

#Enter Weight
Weight=st.number_input('Weight')

#select TouchScreen
TouchScreen=st.selectbox(label='TouchScreen',options=['Yes','No'])

#select IPS
IPS=st.selectbox(label='IPS',options=['Yes','No'])

#Enter ScreenSize
inches=st.number_input('ScreenSize',min_value=0.1)

#select Resolution
resolution=st.selectbox(label='Resolution',options=['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

#calculating PPI

ppi=((int(resolution.split('x')[0])**2)+(int(resolution.split('x')[1])**2))**0.5/inches

# Extracting Touch Screen and IPS

TouchScreen=1 if TouchScreen=='Yes' else 0
IPS=1 if IPS=='Yes' else 0

#enter Speed
Speed=st.number_input("Speed")

#select Cpu
Cpu_Processor=st.selectbox('Cpu Processor',df['Cpu Processor'].unique())

#select SSD
ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

#select HDD
hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

#select GPU
gpu = st.selectbox('GPU',df['Gpu Brand'].unique())

#select OS
OS = st.selectbox('OS',df['OS'].unique())

if st.button('Predict Price'):
    query = [[Company,TypeName,Ram,Weight,TouchScreen,IPS,ppi,Speed,Cpu_Processor,ssd,hdd,gpu,OS]]
    st.title("The predicted price of this laptop is Rs. " + str(int(np.exp(model.predict(query)[0])))+"/-")
