import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("AI Resume Analyser")
st.markdown("Upload your resume and get instant feedback")
st.markdown("---")

job_role = st.text_input("What job role are you applying for?", placeholder="e.g. Software Engineer, Data Analyst")

uploaded_file = st.file_uploader("Upload your resume (.txt file)", type=["txt"])

if st.button("Analyse Resume"):
    if uploaded_file is None:
        st.warning("Please upload your resume first.")
    elif job_role.strip() == "":
        st.warning("Please enter the job role you are applying for.")
    else:
        try:
            resume_text = uploaded_file.read().decode("utf-8")

            with st.spinner("Analysing your resume..."):
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    max_tokens=1024,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are an expert HR consultant and resume coach with 10 years of experience hiring for top companies."
                        },
                        {
                            "role": "user",
                            "content": f"""Analyse this resume for someone applying for the role of {job_role}.

Resume:
{resume_text}

Give feedback on:
1. **Overall impression** (first 10 seconds a recruiter spends on it)
2. **Strengths** (what is working well)
3. **Weaknesses** (what is missing or weak)
4. **Keyword gaps** (important keywords missing for this role)
5. **Top 3 improvements** (specific actionable changes to make)
6. **Score** (rate the resume out of 10 for this role)"""
                        }
                    ]
                )
            st.markdown(response.choices[0].message.content)

        except Exception as e:
            if "429" in str(e):
                st.error("Rate limit hit. Wait 1 minute and try again.")
            else:
                st.error(f"Something went wrong: {str(e)}")