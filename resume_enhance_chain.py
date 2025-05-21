# chains/resume_enhance_chain.py

import google.generativeai as genai
import os
from dotenv import load_dotenv
import streamlit as st

# Accessing the Google API Key from secrets
google_api_key = st.secrets["GOOGLE_API_KEY"]["GOOGLE_API_KEY"]
# Load Gemini API key
#load_dotenv()
#genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

def get_enhanced_resume_section(resume_section, target_title, key_skills, achievement, tone, focus_area, keywords, resume_length="1 page"):
    prompt = f"""
You are an expert ATS-compliant Resume Writer AI.

Your goal is to enhance a resume section with the following detailed considerations:

==========================
 USER'S INPUTS:
==========================
Resume Section Provided:
------------------------
{resume_section}

Context:
- Target Job Title: {target_title}
- Key Skills: {key_skills}
- Achievement: {achievement}
- Focus Area: {focus_area}
- Tone: {tone}
- ATS Keywords to include: {keywords}
- Desired Resume Length: {resume_length}

==========================
 ATS COMPLIANCE GUIDELINES:
==========================
- Use a clean, simple format (avoid tables, images, complex formatting).
- Incorporate relevant keywords from job description.
- Use clear section headings like “Work Experience,” “Projects,” etc.
- Avoid headers, footers, or special characters.
- Format dates consistently (e.g., MM/YYYY or Month Year).
- Save-friendly in .docx, .pdf, or .txt format.

==========================
 EDITING STRATEGY:
==========================
- Fix grammar, typos, and sentence structure.
- Use strong action verbs and concise phrasing.
- Quantify accomplishments wherever possible.
- Rewrite using STAR method (Situation, Task, Action, Result).
- Ensure consistent professional tone.

==========================
 SPECIFIC SECTION TREATMENT:
==========================
**Professional Summary**:
- Rewrite to be more compelling and tailored to the job.
- Use first-person perspective if applicable.

**Work Experience**:
- Use bullet points.
- Start with action verbs.
- Quantify impact (e.g., increased revenue by 15%).

**Projects**:
- Rewrite in paragraph format.
- Emphasize context, your actions, and measurable results.

**Skills**:
- Optimize for ATS using relevant keywords.
- Present in simple list or short phrases.

**Achievements**:
- Emphasize outcome and organizational impact.

==========================
 YOUR TASK:
==========================
Revise the provided resume section according to the instructions above.
Only return the enhanced section in markdown format, ready to paste into a resume.
Do not include explanations or headings.
"""
    response = model.generate_content(prompt)
    return response.text.strip()
