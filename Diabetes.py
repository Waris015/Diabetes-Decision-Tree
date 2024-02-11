import streamlit as st

# ข้อความหัวข้อ
st.title("แบบทดสอบ")

# ข้อความอธิบาย
st.markdown("ชื่อ-นามสกุล ผู้ทำข้อสอบ")
st.text_input("ชื่อ-นามสกุล")

# ข้อ 1
q1_options = ["will", "can", "is", "are"]
q1_answer = st.radio("she ___ run", q1_options, index=0)


# ปุ่มส่งคำตอบ
if st.button("ส่งคำตอบ"):
    # ตรวจสอบคำตอบ
    if q1_answer == "is":
        st.success("ตอบถูก")
    else:
        st.error("ตอบผิด")