<div align="center">

# EasyAgent: ReAct-агент для вычислений на чистом Python

<p align="center">
  <a href="../../README.md"><img alt="English" height="40" src="https://img.shields.io/badge/English-CDCFD4"></a>&nbsp;
  <a href="README_CN.md"><img alt="简体中文" height="40" src="https://img.shields.io/badge/简体中文-CDCFD4"></a>&nbsp;
  <a href="README_TW.md"><img alt="繁體中文" height="40" src="https://img.shields.io/badge/繁體中文-CDCFD4"></a>&nbsp;
  <a href="README_JA.md"><img alt="日本語" height="40" src="https://img.shields.io/badge/日本語-CDCFD4"></a>&nbsp;
  <a href="README_ES.md"><img alt="Español" height="40" src="https://img.shields.io/badge/Español-CDCFD4"></a>&nbsp;
  <a href="README_FR.md"><img alt="Français" height="40" src="https://img.shields.io/badge/Français-CDCFD4"></a>&nbsp;
  <a href="README_AR.md"><img alt="Arabic" height="40" src="https://img.shields.io/badge/Arabic-CDCFD4"></a>&nbsp;
  <a href="README_RU.md"><img alt="Русский" height="40" src="https://img.shields.io/badge/Русский-BCDCF7"></a>&nbsp;
  <a href="README_HI.md"><img alt="Hindi" height="40" src="https://img.shields.io/badge/Hindi-CDCFD4"></a>&nbsp;
  <a href="README_PT.md"><img alt="Português" height="40" src="https://img.shields.io/badge/Português-CDCFD4"></a>&nbsp;
  <a href="README_TH.md"><img alt="Thai" height="40" src="https://img.shields.io/badge/Thai-CDCFD4"></a>&nbsp;
  <a href="README_PL.md"><img alt="Polski" height="40" src="https://img.shields.io/badge/Polski-CDCFD4"></a>
</p>

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)

[Цикл ReAct](#-цикл-react) · [Быстрый старт](#-быстрый-старт) · [Структура](#-структура-проекта) · [Код](#-использование-в-коде) · [Расширение](#-добавление-инструментов)

</div>

---

**ReAct**-агент (Reasoning and Acting), написанный с нуля на чистом Python без LangChain. Встроенный инструмент: **calculator**.

## 🔄 Цикл ReAct

```
Thought → Action → Action Input → Observation → ... → Final Answer
```

## 🚀 Быстрый старт

Требуется API-ключ, совместимый с OpenAI (`OPENAI_API_KEY`).

```bash
cd easyagent
uv venv
uv sync

cp .env.example .env
# Укажите OPENAI_API_KEY в .env

uv run python main.py
uv run python main.py "Calculate (100 + 25) * 3"
```

Настройте `OPENAI_BASE_URL` и `OPENAI_MODEL` для OpenAI, DeepSeek, Ollama и др.

## 📁 Структура проекта

```
easyagent/
├── main.py
├── react_agent/
│   ├── agent.py      # Основной цикл ReAct
│   ├── tools.py      # Инструмент calculator
│   └── llm.py        # Клиент OpenAI-совместимый
└── .env.example
```

## 💻 Использование в коде

```python
from react_agent import run_react_agent

answer = run_react_agent("What is 123 * 456?")
print(answer)
```

## 🔧 Добавление инструментов

1. Добавьте функцию в `react_agent/tools.py` и зарегистрируйте в `TOOLS`
2. Обновите описание в `react_agent/prompts.py`
