<div align="center">

# EasyAgent：純 Python 手搓 ReAct 計算 Agent

<p align="center">
  <a href="../../README.md"><img alt="English" height="40" src="https://img.shields.io/badge/English-CDCFD4"></a>&nbsp;
  <a href="README_CN.md"><img alt="简体中文" height="40" src="https://img.shields.io/badge/简体中文-CDCFD4"></a>&nbsp;
  <a href="README_TW.md"><img alt="繁體中文" height="40" src="https://img.shields.io/badge/繁體中文-BCDCF7"></a>&nbsp;
  <a href="README_JA.md"><img alt="日本語" height="40" src="https://img.shields.io/badge/日本語-CDCFD4"></a>&nbsp;
  <a href="README_ES.md"><img alt="Español" height="40" src="https://img.shields.io/badge/Español-CDCFD4"></a>&nbsp;
  <a href="README_FR.md"><img alt="Français" height="40" src="https://img.shields.io/badge/Français-CDCFD4"></a>&nbsp;
  <a href="README_AR.md"><img alt="Arabic" height="40" src="https://img.shields.io/badge/Arabic-CDCFD4"></a>&nbsp;
  <a href="README_RU.md"><img alt="Русский" height="40" src="https://img.shields.io/badge/Русский-CDCFD4"></a>&nbsp;
  <a href="README_HI.md"><img alt="Hindi" height="40" src="https://img.shields.io/badge/Hindi-CDCFD4"></a>&nbsp;
  <a href="README_PT.md"><img alt="Português" height="40" src="https://img.shields.io/badge/Português-CDCFD4"></a>&nbsp;
  <a href="README_TH.md"><img alt="Thai" height="40" src="https://img.shields.io/badge/Thai-CDCFD4"></a>&nbsp;
  <a href="README_PL.md"><img alt="Polski" height="40" src="https://img.shields.io/badge/Polski-CDCFD4"></a>
</p>

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)

[ReAct 流程](#-react-流程) · [快速開始](#-快速開始) · [專案結構](#-專案結構) · [程式碼使用](#-程式碼使用) · [擴展](#-新增工具)

</div>

---

不使用 LangChain 等框架，從零實作 **ReAct**（Reasoning and Acting）Agent，內建 **calculator** 計算工具。

## 🔄 ReAct 流程

```
Thought → Action → Action Input → Observation → ... → Final Answer
```

| 步驟 | 說明 | 由誰產生 |
|------|------|----------|
| Thought | 內部推理 | LLM |
| Action | 工具名稱 | LLM |
| Action Input | 工具參數（JSON） | LLM |
| Observation | 工具執行結果 | 程式碼 |
| Final Answer | 最終回覆 | LLM |

## 🚀 快速開始

需要設定 OpenAI 相容 API Key（`OPENAI_API_KEY`）。

```bash
cd easyagent
uv venv
uv sync

cp .env.example .env
# 在 .env 填入 OPENAI_API_KEY

uv run python main.py
uv run python main.py "Calculate (100 + 25) * 3"
uv run python main.py --quiet "What is 99 / 3?"
```

透過 `OPENAI_BASE_URL` 與 `OPENAI_MODEL` 可對接 OpenAI、DeepSeek、Ollama 等相容服務。

## 📁 專案結構

```
easyagent/
├── main.py
├── pyproject.toml
├── react_agent/
│   ├── agent.py      # ReAct 主迴圈
│   ├── prompts.py    # System Prompt
│   ├── tools.py      # calculator 工具
│   ├── parser.py     # 解析 LLM 輸出
│   └── llm.py        # OpenAI 相容 API
└── .env.example
```

## 💻 程式碼使用

```python
from react_agent import run_react_agent

answer = run_react_agent("What is 123 * 456?")
print(answer)
```

## 🔧 新增工具

1. 在 `react_agent/tools.py` 新增函式並註冊到 `TOOLS`
2. 更新 `react_agent/prompts.py` 中的工具說明
