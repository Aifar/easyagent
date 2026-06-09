<div align="center" dir="rtl">

# EasyAgent: وكيل ReAct للحساب بلغة Python الخالصة

<p align="center">
  <a href="../../README.md"><img alt="English" height="40" src="https://img.shields.io/badge/English-CDCFD4"></a>&nbsp;
  <a href="README_CN.md"><img alt="简体中文" height="40" src="https://img.shields.io/badge/简体中文-CDCFD4"></a>&nbsp;
  <a href="README_TW.md"><img alt="繁體中文" height="40" src="https://img.shields.io/badge/繁體中文-CDCFD4"></a>&nbsp;
  <a href="README_JA.md"><img alt="日本語" height="40" src="https://img.shields.io/badge/日本語-CDCFD4"></a>&nbsp;
  <a href="README_ES.md"><img alt="Español" height="40" src="https://img.shields.io/badge/Español-CDCFD4"></a>&nbsp;
  <a href="README_FR.md"><img alt="Français" height="40" src="https://img.shields.io/badge/Français-CDCFD4"></a>&nbsp;
  <a href="README_AR.md"><img alt="Arabic" height="40" src="https://img.shields.io/badge/Arabic-BCDCF7"></a>&nbsp;
  <a href="README_RU.md"><img alt="Русский" height="40" src="https://img.shields.io/badge/Русский-CDCFD4"></a>&nbsp;
  <a href="README_HI.md"><img alt="Hindi" height="40" src="https://img.shields.io/badge/Hindi-CDCFD4"></a>&nbsp;
  <a href="README_PT.md"><img alt="Português" height="40" src="https://img.shields.io/badge/Português-CDCFD4"></a>&nbsp;
  <a href="README_TH.md"><img alt="Thai" height="40" src="https://img.shields.io/badge/Thai-CDCFD4"></a>&nbsp;
  <a href="README_PL.md"><img alt="Polski" height="40" src="https://img.shields.io/badge/Polski-CDCFD4"></a>
</p>

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)

</div>

---

وكيل **ReAct** (Reasoning and Acting) مبني من الصفر بلغة Python دون إطارات عمل مثل LangChain. يتضمن أداة **calculator** للحساب.

## 🔄 حلقة ReAct

```
Thought → Action → Action Input → Observation → ... → Final Answer
```

## 🚀 البدء السريع

يتطلب مفتاح API متوافقًا مع OpenAI (`OPENAI_API_KEY`).

```bash
cd easyagent
uv venv
uv sync

cp .env.example .env
# عيّن OPENAI_API_KEY في .env

uv run python main.py
uv run python main.py "Calculate (100 + 25) * 3"
```

## 📁 هيكل المشروع

```
easyagent/
├── main.py
├── react_agent/
│   ├── agent.py      # الحلقة الرئيسية ReAct
│   ├── tools.py      # أداة calculator
│   └── llm.py        # عميل متوافق مع OpenAI
└── .env.example
```

## 💻 الاستخدام في الكود

```python
from react_agent import run_react_agent

answer = run_react_agent("What is 123 * 456?")
print(answer)
```

## 🔧 إضافة أدوات

1. أضف دالة في `react_agent/tools.py` وسجّلها في `TOOLS`
2. حدّث الوصف في `react_agent/prompts.py`
