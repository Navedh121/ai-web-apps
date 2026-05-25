# AI Web Apps

Three web apps that put AI models to practical use. All built with Python and Streamlit, all live and usable right now.

**Stack:** Python · Streamlit · Groq API · LLaMA 3.3 70B

Built by Navedh — second-year Electronics Engineering student from Kerala, India.

---

## Apps

### 1. AI Essay Checker
[![Live App](https://img.shields.io/badge/Live_App-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://navedh121-ai-projects-essay-checker-56julk.streamlit.app)

Paste any essay and get structured feedback: grammar, clarity, argument strength, and specific things to fix.

I built this first because it was the simplest way to understand how sending a prompt to a language model actually works — what you send in, what comes back, how you display it in a UI.

**How the AI part works:**
```
User pastes essay → Streamlit text area
     ↓
System prompt + essay text → Groq API (LLaMA 3.3 70B)
     ↓
Model returns structured critique → displayed in Streamlit
```

---

### 2. YouTube Script Generator
[![Live App](https://img.shields.io/badge/Live_App-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://ai-projects-xqrftqlbzndy9zzspfu5x9.streamlit.app)

Fill in topic, target audience, video length, and tone. The app writes a full script with a hook, main sections, and a call to action.

This one taught me prompt engineering. The quality of the output is almost entirely determined by how clearly you specify what you want — vague instructions give generic scripts.

**What I learned:**
- Structured prompts (with explicit labels like "Hook:", "Section 1:", "CTA:") produce far more usable output than open-ended requests
- Passing user inputs as variables into the prompt template gives the model enough context to write specifically, not generically

---

### 3. Resume Analyser
[![Live App](https://img.shields.io/badge/Live_App-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://ai-projects-cqvvpa7pk928xajp5wlbzp.streamlit.app)

Upload your resume as a text file and enter the role you are targeting. The app scores your resume out of 10 and tells you what is working, what is missing, and what to fix.

This introduced me to file handling in Streamlit — reading uploaded file content and injecting it into a prompt so the model can reason about the actual document.

---

## How to Run Locally

```bash
git clone https://github.com/Navedh121/ai-web-apps.git
cd ai-web-apps
pip install -r requirements.txt
```

Create a `.env` file:
```
GROQ_API_KEY=your-key-here
```

Run any app:
```bash
streamlit run essay_checker.py
streamlit run yt_script_generator.py
streamlit run resume_analyser.py
```

---

## About

I built these while learning how to connect AI models to real interfaces — not just call an API and print the response, but wrap it in something a person can actually use. The Groq API is fast enough that these feel snappy even for longer outputs.
