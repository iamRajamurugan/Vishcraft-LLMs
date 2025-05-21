# main.py

import streamlit as st
from resume_enhance_chain import get_enhanced_resume_section

st.set_page_config(page_title="AI Resume Enhancer", layout="centered")

st.title("📄 AI Resume Section Enhancer (Vishcraft's LLM product)")
st.markdown("Enhance parts of your resume using AI. Provide details below:")

# Input form
with st.form("resume_form"):
    resume_section = st.text_area(" Paste the section of your resume you want to enhance (e.g., Project, Experience)", height=200)
    target_title = st.text_input(" Target Job Title", placeholder="e.g., Data Scientist")
    key_skills = st.text_input(" Key Skills", placeholder="e.g., Python, Machine Learning, SQL")
    achievement = st.text_area(" Proudest Achievement", placeholder="e.g., Deployed an ML model that increased revenue by 10%")
    tone = st.selectbox(" Preferred Tone", ["Formal", "Concise", "Creative", "Persuasive"])
    focus_area = st.text_input(" Focus Area", placeholder="e.g., Experience section, Projects, Summary")
    keywords = st.text_input(" ATS Keywords", placeholder="e.g., Deep Learning, NLP, TensorFlow")

    submitted = st.form_submit_button("✨ Enhance Resume Section")

if submitted:
    if not resume_section.strip():
        st.warning("Please paste a resume section before submitting.")
    else:
        with st.spinner("Our AI is curating excellence from your data...."):
            enhanced = get_enhanced_resume_section(
                resume_section=resume_section,
                target_title=target_title,
                key_skills=key_skills,
                achievement=achievement,
                tone=tone,
                focus_area=focus_area,
                keywords=keywords,
            )
        st.success("✅ Resume section enhanced!")
        st.subheader("🚀 Enhanced Output")
        st.code(enhanced, language="markdown")
