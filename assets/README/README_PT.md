<div align="center">

# EasyAgent: Agente ReAct de cálculo em Python puro

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
  <a href="README_PT.md"><img alt="Português" height="40" src="https://img.shields.io/badge/Português-BCDCF7"></a>&nbsp;
  <a href="README_TH.md"><img alt="Thai" height="40" src="https://img.shields.io/badge/Thai-CDCFD4"></a>&nbsp;
  <a href="README_PL.md"><img alt="Polski" height="40" src="https://img.shields.io/badge/Polski-CDCFD4"></a>
</p>

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)

[Loop ReAct](#-loop-react) · [Início rápido](#-início-rápido) · [Estrutura](#-estrutura-do-projeto) · [Código](#-uso-em-código) · [Estender](#-adicionar-ferramentas)

</div>

---

Agente **ReAct** (Reasoning and Acting) implementado do zero em Python puro, sem LangChain. Ferramenta integrada: **calculator**.

## 🔄 Loop ReAct

```
Thought → Action → Action Input → Observation → ... → Final Answer
```

## 🚀 Início rápido

Requer chave API compatível com OpenAI (`OPENAI_API_KEY`).

```bash
cd easyagent
uv venv
uv sync

cp .env.example .env
# Defina OPENAI_API_KEY no .env

uv run python main.py
uv run python main.py "Calculate (100 + 25) * 3"
```

Configure `OPENAI_BASE_URL` e `OPENAI_MODEL` para OpenAI, DeepSeek, Ollama, etc.

## 📁 Estrutura do projeto

```
easyagent/
├── main.py
├── react_agent/
│   ├── agent.py      # Loop principal ReAct
│   ├── tools.py      # Ferramenta calculator
│   └── llm.py        # Cliente compatível com OpenAI
└── .env.example
```

## 💻 Uso em código

```python
from react_agent import run_react_agent

answer = run_react_agent("What is 123 * 456?")
print(answer)
```

## 🔧 Adicionar ferramentas

1. Adicione uma função em `react_agent/tools.py` e registre em `TOOLS`
2. Atualize a descrição em `react_agent/prompts.py`
