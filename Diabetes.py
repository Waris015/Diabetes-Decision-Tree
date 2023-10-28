import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

st.title("Index Price Prediction")
st.header("Index Price Prediction from NPRU")

# อ่านข้อมูลจากไฟล์ CSV
df = pd.read_csv("./data/Diabetes_Classification.csv")
st.write (df.head(10))

x1 = st.number_input("กรุณาป้อนข้อมูล Age:")
x2 = st.number_input("กรุณาป้อนข้อมูล Gender (เพศชาย 1, เพศหญิง 2):")
x3 = st.number_input("กรุณาป้อนข้อมูล BMI:")
x4 = st.number_input("กรุณาป้อนข้อมูล Pressure:")
x5 = st.number_input("กรุณาป้อนข้อมูล FBS:")
x6 = st.number_input("กรุณาป้อนข้อมูล HbA1c:")

if st.button("พยากรณ์ข้อมูล"):
    # สร้างโมเดล Linear Regression
    modelRegress = LinearRegression()

    # ทำการตรวจสอบข้อมูลและเตรียมข้อมูลสำหรับการพยากรณ์
    X = df[['Age', 'Gender', 'BMI', 'Pressure', 'FBS', 'HbA1c']]
    y = df['target']

    # แบ่งข้อมูลเป็นชุดข้อมูลการฝึกอบรมและการทดสอบ
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # ฝึกโมเดล
    modelRegress.fit(X_train, y_train)

    # พยากรณ์ค่า
    x_input = [[x1, x2, x3, x4, x5, x6]]
    y_predict = modelRegress.predict(x_input)
    st.write("ผลลัพธ์การพยากรณ์:", y_predict[0])
else:
    st.button("ไม่พยากรณ์ข้อมูล")
