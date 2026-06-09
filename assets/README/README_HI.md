<div align="center">

# EasyAgent: शुद्ध Python में ReAct कैलकुलेटर एजेंट

<p align="center">
  <a href="../../README.md"><img alt="English" height="40" src="https://img.shields.io/badge/English-CDCFD4"></a>&nbsp;
  <a href="README_CN.md"><img alt="简体中文" height="40" src="https://img.shields.io/badge/简体中文-CDCFD4"></a>&nbsp;
  <a href="README_TW.md"><img alt="繁體中文" height="40" src="https://img.shields.io/badge/繁體中文-CDCFD4"></a>&nbsp;
  <a href="README_JA.md"><img alt="日本語" height="40" src="https://img.shields.io/badge/日本語-CDCFD4"></a>&nbsp;
  <a href="README_ES.md"><img alt="Español" height="40" src="https://img.shields.io/badge/Español-CDCFD4"></a>&nbsp;
  <a href="README_FR.md"><img alt="Français" height="40" src="https://img.shields.io/badge/Français-CDCFD4"></a>&nbsp;
  <a href="README_AR.md"><img alt="Arabic" height="40" src="https://img.shields.io/badge/Arabic-CDCFD4"></a>&nbsp;
  <a href="README_RU.md"><img alt="Русский" height="40" src="https://img.shields.io/badge/Русский-CDCFD4"></a>&nbsp;
  <a href="README_HI.md"><img alt="Hindi" height="40" src="https://img.shields.io/badge/Hindi-BCDCF7"></a>&nbsp;
  <a href="README_PT.md"><img alt="Português" height="40" src="https://img.shields.io/badge/Português-CDCFD4"></a>&nbsp;
  <a href="README_TH.md"><img alt="Thai" height="40" src="https://img.shields.io/badge/Thai-CDCFD4"></a>&nbsp;
  <a href="README_PL.md"><img alt="Polski" height="40" src="https://img.shields.io/badge/Polski-CDCFD4"></a>
</p>

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)

</div>

---

LangChain के बिना शुद्ध Python में **ReAct** (Reasoning and Acting) एजेंट। अंतर्निहित टूल: **calculator**।

## 🔄 ReAct लूप

```
Thought → Action → Action Input → Observation → ... → Final Answer
```

## 🚀 त्वरित प्रारंभ

OpenAI-संगत API कुंजी (`OPENAI_API_KEY`) आवश्यक है।

```bash
cd easyagent
uv venv
uv sync

cp .env.example .env
# .env में OPENAI_API_KEY सेट करें

uv run python main.py
```

## 💻 कोड में उपयोग

```python
from react_agent import run_react_agent

answer = run_react_agent("What is 123 * 456?")
print(answer)
```

## 🔧 टूल जोड़ना

1. `react_agent/tools.py` में फ़ंक्शन जोड़ें और `TOOLS` में पंजीकृत करें
2. `react_agent/prompts.py` में विवरण अपडेट करें
