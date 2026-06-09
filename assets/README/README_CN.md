<div align="center">

# EasyAgent：纯 Python 手搓 ReAct 计算 Agent

<p align="center">
  <a href="../../README.md"><img alt="English" height="40" src="https://img.shields.io/badge/English-CDCFD4"></a>&nbsp;
  <a href="README_CN.md"><img alt="简体中文" height="40" src="https://img.shields.io/badge/简体中文-BCDCF7"></a>&nbsp;
  <a href="README_TW.md"><img alt="繁體中文" height="40" src="https://img.shields.io/badge/繁體中文-CDCFD4"></a>&nbsp;
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

[ReAct 流程](#-react-流程) · [快速开始](#-快速开始) · [项目结构](#-项目结构) · [代码使用](#-代码使用) · [扩展](#-新增工具)

</div>

---

不使用 LangChain 等框架，从零实现 **ReAct**（Reasoning and Acting）Agent，内置 **calculator** 计算器工具。

## 🔄 ReAct 流程

```
Thought → Action → Action Input → Observation → ... → Final Answer
```

| 步骤 | 说明 | 由谁产生 |
|------|------|----------|
| Thought | 内部推理 | LLM |
| Action | 工具名称 | LLM |
| Action Input | 工具参数（JSON） | LLM |
| Observation | 工具执行结果 | 代码 |
| Final Answer | 最终回复 | LLM |

## 🚀 快速开始

需要配置 OpenAI 兼容 API Key（`OPENAI_API_KEY`）。

```bash
cd easyagent
uv venv
uv sync

cp .env.example .env
# 在 .env 中填入 OPENAI_API_KEY

uv run python main.py
uv run python main.py "Calculate (100 + 25) * 3"
uv run python main.py --quiet "What is 99 / 3?"
```

通过 `OPENAI_BASE_URL` 和 `OPENAI_MODEL` 可对接 OpenAI、DeepSeek、Ollama 等兼容服务。

## 📁 项目结构

```
easyagent/
├── main.py
├── pyproject.toml
├── react_agent/
│   ├── agent.py      # ReAct 主循环
│   ├── prompts.py    # System Prompt
│   ├── tools.py      # calculator 工具
│   ├── parser.py     # 解析 LLM 输出
│   └── llm.py        # OpenAI 兼容 API
└── .env.example
```

## 💻 代码使用

```python
from react_agent import run_react_agent

answer = run_react_agent("What is 123 * 456?")
print(answer)
```

## 🔧 新增工具

1. 在 `react_agent/tools.py` 中新增函数并注册到 `TOOLS`
2. 更新 `react_agent/prompts.py` 中的工具说明
