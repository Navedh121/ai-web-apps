# AI Projects

Three small web apps I built while learning how to connect AI models to real interfaces. Each one solves a different everyday problem and takes less than a minute to use.

All three are built with Python and Streamlit, and use the Groq API to run the Llama 3.3 70B language model.

---

## Projects

### 1. AI Essay Checker
Paste any essay and get feedback on grammar, clarity, argument strength, and specific things to improve.

I built this first because it was the simplest way to understand how sending a prompt to an AI model works and how to display the response in a clean UI.

Live app: https://navedh121-ai-projects-essay-checker-56julk.streamlit.app

---

### 2. YouTube Script Generator
Fill in a topic, target audience, video length, and tone. The app writes a full script with a hook, main sections, and a call to action.

This one taught me prompt engineering. The quality of the output completely depends on how well you structure the instructions you give the model.

Live app: https://ai-projects-xqrftqlbzndy9zzspfu5x9.streamlit.app

---

### 3. Resume Analyser
Upload your resume as a text file and enter the job role you are applying for. The app scores your resume out of 10 and tells you what is working, what is missing, and what to fix.

This introduced me to file handling in Streamlit and how to pass document content into a prompt.

Live app: https://ai-projects-cqvvpa7pk928xajp5wlbzp.streamlit.app

---

## How to run locally

1. Clone the repo
```
git clone https://github.com/Navedh121/ai-projects.git
cd ai-projects
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. Create a `.env` file and add your Groq API key
```
GROQ_API_KEY=your-key-here
```

4. Run any app
```
streamlit run essay_checker.py
streamlit run yt_script_generator.py
streamlit run resume_analyser.py
```

---

## Stack

- Python
- Streamlit
- Groq API
- Llama 3.3 70B

---

## About

I am a second year Electronics Engineering student from Kerala. These projects are part of my journey learning to build real things with AI, not just study it.
