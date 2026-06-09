<div align="center">

# EasyAgent: เอเจนต์ ReAct คำนวณตัวเลขด้วย Python ล้วน

<p align="center">
  <a href="../../README.md"><img alt="English" height="40" src="https://img.shields.io/badge/English-CDCFD4"></a>&nbsp;
  <a href="README_CN.md"><img alt="简体中文" height="40" src="https://img.shields.io/badge/简体中文-CDCFD4"></a>&nbsp;
  <a href="README_TW.md"><img alt="繁體中文" height="40" src="https://img.shields.io/badge/繁體中文-CDCFD4"></a>&nbsp;
  <a href="README_JA.md"><img alt="日本語" height="40" src="https://img.shields.io/badge/日本語-CDCFD4"></a>&nbsp;
  <a href="README_ES.md"><img alt="Español" height="40" src="https://img.shields.io/badge/Español-CDCFD4"></a>&nbsp;
  <a href="README_FR.md"><img alt="Français" height="40" src="https://img.shields.io/badge/Français-CDCFD4"></a>&nbsp;
  <a href="README_AR.md"><img alt="Arabic" height="40" src="https://img.shields.io/badge/Arabic-CDCFD4"></a>&nbsp;
  <a href="README_RU.md"><img alt="Русский" height="40" src="https://img.shields.io/badge/Русский-CDCFD4"></a>&nbsp;
  <a href="README_HI.md"><img alt="Hindi" height="40" src="https://img.shields.io/badge/Hindi-CDCFD4"></a>&nbsp;
  <a href="README_PT.md"><img alt="Português" height="40" src="https://img.shields.io/badge/Português-CDCFD4"></a>&nbsp;
  <a href="README_TH.md"><img alt="Thai" height="40" src="https://img.shields.io/badge/Thai-BCDCF7"></a>&nbsp;
  <a href="README_PL.md"><img alt="Polski" height="40" src="https://img.shields.io/badge/Polski-CDCFD4"></a>
</p>

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)

</div>

---

เอเจนต์ **ReAct** (Reasoning and Acting) ที่เขียนด้วย Python ล้วน ไม่ใช้ LangChain เครื่องมือในตัว: **calculator**

## 🔄 ลูป ReAct

```
Thought → Action → Action Input → Observation → ... → Final Answer
```

## 🚀 เริ่มต้นอย่างรวดเร็ว

ต้องมี API key ที่รองรับ OpenAI (`OPENAI_API_KEY`)

```bash
cd easyagent
uv venv
uv sync

cp .env.example .env
# ตั้งค่า OPENAI_API_KEY ใน .env

uv run python main.py
```

## 💻 ใช้งานในโค้ด

```python
from react_agent import run_react_agent

answer = run_react_agent("What is 123 * 456?")
print(answer)
```

## 🔧 เพิ่มเครื่องมือ

1. เพิ่มฟังก์ชันใน `react_agent/tools.py` และลงทะเบียนใน `TOOLS`
2. อัปเดตคำอธิบายใน `react_agent/prompts.py`
