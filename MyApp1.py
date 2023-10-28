import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split

# สร้างหน้าเว็บแอป
st.title("การพยากรณ์ราคาดัชนี")
st.header("การพยากรณ์ราคาดัชนีจาก NPRU")

# โหลดชุดข้อมูลของคุณ (แทนที่ด้วยเส้นทางไฟล์ที่ถูกต้อง)
df = pd.read_csv("./data/your_dataset.csv")

st.write(df.head(10))

st.header("กราฟการพยากรณ์ราคาดัชนี")
st.line_chart(df['interest_rate', 'unemployment_rate', 'Diabetes_Classification'][:100])

x = df[['interest_rate', 'unemployment_rate']]
y = df['Diabetes_Classification']
pf = PolynomialFeatures(degree=3)
x_poly = pf.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x_poly, y, random_state=0)

modelRegress = LinearRegression()
modelRegress.fit(x_train, y_train)

x1 = st.number_input("ป้อนอัตราดอกเบี้ย:")
x2 = st.number_input("ป้อนอัตราว่างงาน:")

if st.button("พยากรณ์"):
    x_input = [[x1, x2]]
    y_predict = modelRegress.predict(pf.transform(x_input))
    st.write(f"ราคาดัชนีที่พยากรณ์: {y_predict[0]}")
else:
    st.write("โปรดป้อนค่าและคลิก 'พยากรณ์'.")

# ตามต้องการ คุณสามารถแสดงค่ามาตรฐานเช่น R^2 และค่าข้อผิดพลาดเฉลี่ย
y_test_pred = modelRegress.predict(x_test)
r2 = r2_score(y_test, y_test_pred)
mse = mean_squared_error(y_test, y_test_pred)
st.write(f"คะแนน R^2: {r2}")
st.write(f"ค่าข้อผิดพลาดเฉลี่ย: {mse}")
