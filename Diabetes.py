import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression

st.title("Diabetes Diagnosis Prediction")
st.header("Predicting Diabetes Diagnosis from Health Data")

# อ่านข้อมูลจากไฟล์ CSV
df = pd.read_csv("Diabetes_Classification.csv")
st.write(df.head(10))

x1 = st.number_input("กรุณาป้อนข้อมูลอายุ:")
x2 = st.number_input("กรุณาป้อนข้อมูลเพศ (เพศชาย 1, เพศหญิง 2):")
x3 = st.number_input("กรุณาป้อนข้อมูล BMI:")
x4 = st.number_input("กรุณาป้อนข้อมูลความดันโลหิต:")
x5 = st.number_input("กรุณาป้อนข้อมูลค่าน้ำตาลในเลือด:")
x6 = st.number_input("กรุณาป้อนข้อมูลค่า HbA1c:")

if st.button("พยากรณ์ข้อมูล"):
    # เตรียมข้อมูล
    X = df[['Age', 'Gender', 'BMI', 'Pressure', 'FBS', 'HbA1c']]
    y = df['Diagnosis']  # คอลัมน์ที่เราจะพยากรณ์

    # สร้างโมเดล Linear Regression
    model = LinearRegression()

    # ฝึกโมเดล
    model.fit(X, y)

    # ทำการพยากรณ์ผล
    x_input = [[x1, x2, x3, x4, x5, x6]]
    diagnosis = model.predict(x_input)[0]

    if diagnosis == "Yes":
        st.write("ผลลัพธ์การพยากรณ์: ผู้ป่วยเบาหวาน")
    else:
        st.write("ผลลัพธ์การพยากรณ์: ไม่เป็นผู้ป่วยเบาหวาน")

# เพิ่มเงื่อนไขอื่น ๆ ที่คุณต้องการแสดงผลหรือกระทำต่อไป
