import streamlit as st
from utils import extract_text_from_pdf, analyze_resume

st.title("Resume Analyzer with Job Matching")

uploaded_file = st.file_uploader("Upload your resume as PDF", type="pdf")
if uploaded_file:
    with st.spinner("Analyzing Resume..."):
        text = extract_text_from_pdf(uploaded_file)
        result = analyze_resume(text)

    st.subheader("Analysis result")
    st.markdown(result)
