# AI Web Apps

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq_API-F55036?style=flat&logoColor=white)
![Model](https://img.shields.io/badge/LLaMA_3.3--70B-0467DF?style=flat&logoColor=white)
![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=flat)

Three AI-powered web apps built with Python, Streamlit, and the Groq API (LLaMA 3.3-70B). Each app demonstrates a different real-world use case for large language models.

---

## Apps

### Essay Checker
[![Live App](https://img.shields.io/badge/Live_App-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://navedh121-ai-projects-essay-checker-56julk.streamlit.app)

Paste any essay and get structured feedback: grammar issues, clarity problems, argument strength, and three specific improvements. Acts as an experienced writing teacher — tells you what to fix and why.

**How the AI part works:**
```
User pastes essay -> Streamlit text area
     |
System prompt + essay text -> Groq API (LLaMA 3.3-70B)
     |
Model returns structured critique -> displayed in Streamlit
```

---

### YouTube Script Generator
[![Live App](https://img.shields.io/badge/Live_App-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://ai-projects-xqrftqlbzndy9zzspfu5x9.streamlit.app)

Fill in topic, target audience, video length, and tone. Generates a full script with hook, main sections, and a call to action. The output quality depends almost entirely on how specific the prompt is — this was where I learned practical prompt engineering.

---

### Resume Analyser
[![Live App](https://img.shields.io/badge/Live_App-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://ai-projects-cqvvpa7pk928xajp5wlbzp.streamlit.app)

Upload your resume as a text file and enter the role you are targeting. Scores your resume out of 10 and gives actionable feedback: what is working, what is missing, and what to fix.

---

## What Makes These Different

All three apps use structured system prompts to force the LLM to return consistent, formatted output.

| App | System Prompt Goal |
|---|---|
| Essay Checker | Return feedback in fixed sections; always include 3 specific improvements |
| Resume Analyser | Respond as an HR consultant; always include a score out of 10 |
| Script Generator | Return sections in exact order: Hook -> Intro -> 3 sections -> CTA |

---

## How to Run

```bash
git clone https://github.com/Navedh121/ai-projects.git
cd ai-projects
pip install -r requirements.txt
```

Create a `.env` file:
```
GROQ_API_KEY=your_key_here
```

Run any app:
```bash
streamlit run essay_checker.py
streamlit run resume_analyser.py
streamlit run yt_script_generator.py
```

---

## Repo Structure

```
ai-projects/
├── essay_checker.py
├── resume_analyser.py
├── yt_script_generator.py
└── requirements.txt
```

---

> Part of a learning series: [CLI tools](https://github.com/Navedh121/python-beginner-projects) -> AI web apps -> [Automation bots](https://github.com/Navedh121/python-automation-bots)
