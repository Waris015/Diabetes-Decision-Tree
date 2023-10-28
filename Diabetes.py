import pandas as pd
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error

st.title("Index Price Prediction")
st.header("Index Price Prediction from NPRU")

df=pd.read_csv("./data/Diabetes_Classification.csv")
st.write(df.head(10))

x1=st.number_input("กรุณาป้อนข้อมูล อายุ:")
x2=st.number_input("กรุณาป้อนข้อมูล เพศ (เพศชาย 1, เพศหญิง 2):")
x3=st.number_input("กรุณาป้อนข้อมูล BMI:")
x4=st.number_input("กรุณาป้อนข้อมูล ความดันโลหิต:")
x5=st.number_input("กรุณาป้อนข้อมูล ค่าน้ำตาลในเลือด:")
x6=st.number_input("กรุณาป้อนข้อมูล ค่าน้ำตาลสะสม:")

if st.button("พยากรณ์ข้อมูล"):
    x_input=[[x1,x2,x3,x4,x5,x6]]
    y_predict=modelRegress.predict(pf.fit_transform(x_input))
    st.write(y_predict)
    st.button("ไม่พยากรณ์ข้อมูล")
else:
    st.button("ไม่พยากรณ์ข้อมูล")