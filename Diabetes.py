import pandas as pd
import streamlit as st
import seaborn as sns
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error

st.title("hart axtex")
st.header("Hart NPRU")

df=pd.read_csv('./data/Diabetes_Classification.csv')
st.write(df.head(10))

#st.line_chart(df)
#st.line_chart(df, x="interest_rate", y="unemployment_rate", color="stock_index_price")

x=df.iloc[:, 0:6]
y=y = df['Dagnossis']

x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.3,random_state=1)

sc = StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)

DTmodel = DecisionTreeClassifier(criterion='gini')
DTmodel.fit(x_train, y_train)

x1=st.number_input("กรุณาป้อนข้อมูล อายุ:")
x2=st.number_input("กรุณาป้อนข้อมูล เพศ (เพศชาย 1, เพศหญิง 2):")
x3=st.number_input("กรุณาป้อนข้อมูล BMI:")
x4=st.number_input("กรุณาป้อนข้อมูล ความดันโลหิต:")
x5=st.number_input("กรุณาป้อนข้อมูล ค่าน้ำตาลในเลือด:")
x6=st.number_input("กรุณาป้อนข้อมูล ค่าน้ำตาลสะสม:")


if st.button("พยากรณ์ข้อมูล"):
    x_input=[[x1,x2,x3,x4,x5,x6,]]
    y_predict=DTmodel.predict(x_input)
    st.write(y_predict)
    st.button("ไม่พยากรณ์ข้อมูล")
else:
    st.button("ไม่พยากรณ์ข้อมูล")