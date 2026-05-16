import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("YouTube Script Generator")
st.markdown("Generate a full YouTube script in seconds")
st.markdown("---")

topic = st.text_input("Video topic", placeholder="e.g. How to study effectively as an engineering student")
audience = st.text_input("Target audience", placeholder="e.g. College students in India")
length = st.selectbox("Video length", ["3 minutes", "5 minutes", "10 minutes"])
tone = st.selectbox("Tone", ["Casual and engaging", "Professional", "Funny and entertaining", "Educational"])

if st.button("Generate Script"):
    if topic.strip() == "" or audience.strip() == "":
        st.warning("Please fill in the topic and audience fields.")
    else:
        try:
            with st.spinner("Writing your script..."):
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    max_tokens=1024,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are an expert YouTube scriptwriter who has written scripts for channels with millions of subscribers."
                        },
                        {
                            "role": "user",
                            "content": f"""Write a YouTube script with the following details:

Topic: {topic}
Target audience: {audience}
Video length: {length}
Tone: {tone}

Structure the script exactly like this:
- **Title** (catchy, clickable)
- **Hook** (first 30 seconds to grab attention immediately)
- **Introduction** (brief, tell them what they will learn)
- **Main Content** (3 sections with clear headings)
- **Conclusion** (summarise key points)
- **Call to action** (ask them to like, comment, subscribe)

Write the full script with actual words to say, not just headings."""
                        }
                    ]
                )
            st.markdown(response.choices[0].message.content)

        except Exception as e:
            if "429" in str(e):
                st.error("Rate limit hit. Wait 1 minute and try again.")
            else:
                st.error(f"Something went wrong: {str(e)}")