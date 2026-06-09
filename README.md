<div align="center">

# EasyAgent: Hand-Rolled ReAct Calculator Agent

<p align="center">
  <a href="README.md"><img alt="English" height="40" src="https://img.shields.io/badge/English-BCDCF7"></a>&nbsp;
  <a href="assets/README/README_CN.md"><img alt="简体中文" height="40" src="https://img.shields.io/badge/简体中文-CDCFD4"></a>&nbsp;
  <a href="assets/README/README_TW.md"><img alt="繁體中文" height="40" src="https://img.shields.io/badge/繁體中文-CDCFD4"></a>&nbsp;
  <a href="assets/README/README_JA.md"><img alt="日本語" height="40" src="https://img.shields.io/badge/日本語-CDCFD4"></a>&nbsp;
  <a href="assets/README/README_ES.md"><img alt="Español" height="40" src="https://img.shields.io/badge/Español-CDCFD4"></a>&nbsp;
  <a href="assets/README/README_FR.md"><img alt="Français" height="40" src="https://img.shields.io/badge/Français-CDCFD4"></a>&nbsp;
  <a href="assets/README/README_AR.md"><img alt="Arabic" height="40" src="https://img.shields.io/badge/Arabic-CDCFD4"></a>&nbsp;
  <a href="assets/README/README_RU.md"><img alt="Русский" height="40" src="https://img.shields.io/badge/Русский-CDCFD4"></a>&nbsp;
  <a href="assets/README/README_HI.md"><img alt="Hindi" height="40" src="https://img.shields.io/badge/Hindi-CDCFD4"></a>&nbsp;
  <a href="assets/README/README_PT.md"><img alt="Português" height="40" src="https://img.shields.io/badge/Português-CDCFD4"></a>&nbsp;
  <a href="assets/README/README_TH.md"><img alt="Thai" height="40" src="https://img.shields.io/badge/Thai-CDCFD4"></a>&nbsp;
  <a href="assets/README/README_PL.md"><img alt="Polski" height="40" src="https://img.shields.io/badge/Polski-CDCFD4"></a>
</p>

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)

[ReAct Loop](#-react-loop) · [Quick Start](#-quick-start) · [Project Structure](#-project-structure) · [Usage](#-usage-in-code) · [Extend](#-adding-tools)

</div>

---

A minimal **ReAct** (Reasoning and Acting) agent built in pure Python — no LangChain, no CrewAI. It ships with one tool: **calculator**.

## 🔄 ReAct Loop

```
Thought → Action → Action Input → Observation → ... → Final Answer
```

| Step | Description | Produced by |
|------|-------------|-------------|
| Thought | Internal reasoning | LLM |
| Action | Tool name | LLM |
| Action Input | Tool arguments (JSON) | LLM |
| Observation | Tool result | Your code |
| Final Answer | Response to the user | LLM |

## 🚀 Quick Start

Requires an OpenAI-compatible API key (`OPENAI_API_KEY`).

```bash
cd easyagent
uv venv
uv sync

cp .env.example .env
# Set OPENAI_API_KEY in .env

uv run python main.py
uv run python main.py "Calculate (100 + 25) * 3"
uv run python main.py --quiet "What is 99 / 3?"
```

Configure `OPENAI_BASE_URL` and `OPENAI_MODEL` for OpenAI, DeepSeek, Ollama, or any compatible provider.

## 📁 Project Structure

```
easyagent/
├── main.py
├── pyproject.toml
├── react_agent/
│   ├── agent.py      # ReAct main loop
│   ├── prompts.py    # System prompt
│   ├── tools.py      # calculator tool
│   ├── parser.py     # LLM output parser
│   └── llm.py        # OpenAI-compatible client
└── .env.example
```

## 💻 Usage in Code

```python
from react_agent import run_react_agent

answer = run_react_agent("What is 123 * 456?")
print(answer)
```

## 🔧 Adding Tools

1. Add a function in `react_agent/tools.py` and register it in `TOOLS`
2. Update the tool description in `react_agent/prompts.py`
