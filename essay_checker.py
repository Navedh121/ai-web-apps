import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("AI Essay Checker")
st.markdown("### Get instant AI feedback on your essays")
st.markdown("---")

with st.sidebar:
    st.markdown("### How to use")
    st.markdown("1. Paste your essay in the box")
    st.markdown("2. Click the button")
    st.markdown("3. Read your feedback")
    st.markdown("---")
    st.markdown("Built with Groq + Streamlit")
st.write("Paste your essay below and get instant feedback.")

essay = st.text_area("Your essay", height=250)

if st.button("Check my essay"):
    if essay.strip() == "":
        st.warning("Please paste an essay first.")
    else:
        try:
            with st.spinner("Analysing your essay..."):
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    max_tokens=1024,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are an essay coach. Give feedback on grammar, clarity, argument strength, and give 3 specific improvements."
                        },
                        {
                            "role": "user",
                            "content": f"Check this essay:\n\n{essay}"
                        }
                    ]
                )
            st.markdown(response.choices[0].message.content)

        except Exception as e:
            if "429" in str(e):
                st.error("Rate limit hit. Wait 1 minute and try again.")
            else:
                st.error(f"Something went wrong: {str(e)}")
