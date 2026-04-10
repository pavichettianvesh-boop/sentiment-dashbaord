import streamlit as st

st.title("🔥 Sentiment App")

text = st.text_input("Enter text")

if st.button("Analyze"):
    if "good" in text.lower():
        st.success("Positive 😊")
    else:
        st.error("Negative 😡")
