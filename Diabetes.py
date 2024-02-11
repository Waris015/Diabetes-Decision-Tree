import streamlit as st

# ข้อความหัวข้อ
with st.container():
    st.form("แบบทดสอบ")
    st.markdown("""
        ---
        """)

# ข้อความอธิบาย
name = st.text_input("ชื่อ-นามสกุล ผู้ทำข้อสอบ")

# ข้อ 1
q1_options = ["will", "can", "is", "are"]
q1_answer = st.radio("She ___ run ", q1_options, index=0)

# ปุ่มส่งคำตอบ
if st.button("ส่งคำตอบ"):
    # ตรวจสอบคำตอบ
    if q1_answer == "can":
        st.success("ตอบถูก")
    else:
        st.error("ตอบผิด")


