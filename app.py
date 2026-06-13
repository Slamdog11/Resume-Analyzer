import streamlit as st
from parser import extract_text
from ats_score import calculate_score
from analyzer import find_missing_keywords

st.title("AI Resume Analyzer")

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

jd = st.text_area(
    "Paste Job Description"
)

if resume and jd:

    resume_text = extract_text(resume)

    score = calculate_score(
        resume_text,
        jd
    )

    missing = find_missing_keywords(
        resume_text,
        jd
    )

    st.subheader("ATS Score")
    st.success(f"{score}%")

    st.subheader("Missing Keywords")

    for word in missing:
        st.write(word)