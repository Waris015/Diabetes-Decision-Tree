import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

st.title("Diabetes Decision")
st.header("Diabetes Classification Dataset")

# อ่านข้อมูลจากไฟล์ CSV
df = pd.read_csv('./data/Diabetes Classification.csv')
st.write(df.head(10))

# แบ่งข้อมูลเป็น features (x) และ target (y)
x = df.iloc[:, :-1]  # ใช้ทุกคอลัมน์ยกเว้นคอลัมน์สุดท้าย
y = df.iloc[:, -1]   # ใช้คอลัมน์สุดท้ายเป็น target

# แบ่งข้อมูลเป็นชุดการฝึกอบรมและชุดทดสอบ
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

DTmodel = DecisionTreeClassifier(criterion='gini')
DTmodel.fit(x_train, y_train)

x1 = st.number_input("กรุณาป้อนข้อมูล อายุ:")
x2 = st.number_input("กรุณาป้อนข้อมูล เพศ (เพศชาย 1, เพศหญิง 2):")
x3 = st.number_input("กรุณาป้อนข้อมูล BMI:")
x4 = st.number_input("กรุณาป้อนข้อมูล ความดันโลหิต:")
x5 = st.number_input("กรุณาป้อนข้อมูล ค่าน้ำตาลในเลือด:")
x6 = st.number_input("กรุณาป้อนข้อมูล ค่าน้ำตาลสะสม:")

if st.button("พยากรณ์ข้อมูล"):
    x_input = [[x1, x2, x3, x4, x5, x6]]
    y_predict = DTmodel.predict(x_input)
    st.write(y_predict)
    st.button("ไม่พยากรณ์ข้อมูล")
else:
    st.button("ไม่พยากรณ์ข้อมูล")
