# AI Web Apps

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq_API-F55036?style=flat&logoColor=white)
![Model](https://img.shields.io/badge/LLaMA_3.3--70B-0467DF?style=flat&logoColor=white)
![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=flat)

Three AI-powered web apps built with Python, Streamlit, and the Groq API (LLaMA 3.3-70B). Each app demonstrates a different use case for large language models in a clean, usable interface.

---

## Apps

### Essay Checker
Paste any essay and get structured feedback in seconds: grammar issues, clarity problems, argument strength, and three specific improvements. The grader acts as an experienced writing teacher — it doesn't just say "good job," it tells you what to fix and why.

### Resume Analyser
Upload a `.txt` resume, enter the job role you're targeting, and get a full recruiter-style breakdown: what stands out, what's missing, which keywords to add, and an overall score out of 10. Built this after noticing most resume tools just flag spelling — this one reads it like a hiring manager.

### YouTube Script Generator
Enter a topic, target audience, video length (3/5/10 min), and tone (casual/professional/funny/educational). The app generates a complete script with a hook, three content sections, and a call to action — actual lines you can read, not just an outline.

---

## What Makes These Different

All three apps use **structured system prompts** to force the LLM to return consistent, formatted output. The difference between a useful AI tool and a frustrating one is almost entirely in how the prompt is written. These apps show that.

| App | System Prompt Goal |
|---|---|
| Essay Checker | Return feedback in fixed sections; always include 3 specific improvements |
| Resume Analyser | Respond as an HR consultant; always include a score out of 10 |
| Script Generator | Return sections in exact order: Hook → Intro → 3 sections → CTA |

---

## Tech Stack

- **Streamlit** — turns a Python script into a web app with no frontend code
- **Groq API** — runs LLaMA 3.3-70B inference at very fast speeds
- **LLaMA 3.3-70B** — the model powering all three apps
- **python-dotenv** — keeps API keys out of the source code

---

## How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Add your Groq API key to .env
# Get one free at https://console.groq.com
echo "GROQ_API_KEY=your_key_here" > .env

# Launch any app
streamlit run essay_checker.py
streamlit run resume_analyser.py
streamlit run yt_script_generator.py
```

---

## Repo Structure

```
ai-projects/
├── essay_checker.py        # AI writing feedback tool
├── resume_analyser.py      # Resume scorer and advisor
├── yt_script_generator.py  # Full YouTube script generator
├── requirements.txt
└── .env                    # Not committed — add your own key
```

---

> Part of a learning series: [CLI tools](https://github.com/Navedh121/python-projects) → AI web apps → [Automation bots](https://github.com/Navedh121/python-automation-bots)
