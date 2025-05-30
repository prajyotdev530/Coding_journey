import streamlit as st
from extractor import extract_text_from_pdf, extract_skills
from feedback_agent import generate_feedback

st.set_page_config(page_title="AI Resume Reviewer", layout="centered")
st.title("📄 AI Resume Reviewer")

resume_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste the Job Description here")

if resume_file and job_description:
    resume_text = extract_text_from_pdf(resume_file)
    st.subheader("Extracted Resume Text")
    st.text(resume_text[:1000] + "..." if len(resume_text) > 1000 else resume_text)

    st.subheader("Skills Found")
    skills = extract_skills(resume_text)
    st.write(skills)

    st.subheader("AI Feedback")
    feedback = generate_feedback(resume_text, job_description)
    st.write(feedback)