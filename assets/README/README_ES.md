<div align="center">

# EasyAgent: Agente ReAct de cálculo en Python puro

<p align="center">
  <a href="../../README.md"><img alt="English" height="40" src="https://img.shields.io/badge/English-CDCFD4"></a>&nbsp;
  <a href="README_CN.md"><img alt="简体中文" height="40" src="https://img.shields.io/badge/简体中文-CDCFD4"></a>&nbsp;
  <a href="README_TW.md"><img alt="繁體中文" height="40" src="https://img.shields.io/badge/繁體中文-CDCFD4"></a>&nbsp;
  <a href="README_JA.md"><img alt="日本語" height="40" src="https://img.shields.io/badge/日本語-CDCFD4"></a>&nbsp;
  <a href="README_ES.md"><img alt="Español" height="40" src="https://img.shields.io/badge/Español-BCDCF7"></a>&nbsp;
  <a href="README_FR.md"><img alt="Français" height="40" src="https://img.shields.io/badge/Français-CDCFD4"></a>&nbsp;
  <a href="README_AR.md"><img alt="Arabic" height="40" src="https://img.shields.io/badge/Arabic-CDCFD4"></a>&nbsp;
  <a href="README_RU.md"><img alt="Русский" height="40" src="https://img.shields.io/badge/Русский-CDCFD4"></a>&nbsp;
  <a href="README_HI.md"><img alt="Hindi" height="40" src="https://img.shields.io/badge/Hindi-CDCFD4"></a>&nbsp;
  <a href="README_PT.md"><img alt="Português" height="40" src="https://img.shields.io/badge/Português-CDCFD4"></a>&nbsp;
  <a href="README_TH.md"><img alt="Thai" height="40" src="https://img.shields.io/badge/Thai-CDCFD4"></a>&nbsp;
  <a href="README_PL.md"><img alt="Polski" height="40" src="https://img.shields.io/badge/Polski-CDCFD4"></a>
</p>

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)

[Bucle ReAct](#-bucle-react) · [Inicio rápido](#-inicio-rápido) · [Estructura](#-estructura-del-proyecto) · [Uso](#-uso-en-código) · [Extender](#-añadir-herramientas)

</div>

---

Agente **ReAct** (Reasoning and Acting) implementado desde cero en Python puro, sin LangChain. Incluye la herramienta **calculator**.

## 🔄 Bucle ReAct

```
Thought → Action → Action Input → Observation → ... → Final Answer
```

## 🚀 Inicio rápido

Requiere una clave API compatible con OpenAI (`OPENAI_API_KEY`).

```bash
cd easyagent
uv venv
uv sync

cp .env.example .env
# Configura OPENAI_API_KEY en .env

uv run python main.py
uv run python main.py "Calculate (100 + 25) * 3"
uv run python main.py --quiet "What is 99 / 3?"
```

Configura `OPENAI_BASE_URL` y `OPENAI_MODEL` para OpenAI, DeepSeek, Ollama u otros proveedores compatibles.

## 📁 Estructura del proyecto

```
easyagent/
├── main.py
├── pyproject.toml
├── react_agent/
│   ├── agent.py      # Bucle principal ReAct
│   ├── prompts.py    # Prompt del sistema
│   ├── tools.py      # Herramienta calculator
│   ├── parser.py     # Parser de salida LLM
│   └── llm.py        # Cliente compatible con OpenAI
└── .env.example
```

## 💻 Uso en código

```python
from react_agent import run_react_agent

answer = run_react_agent("What is 123 * 456?")
print(answer)
```

## 🔧 Añadir herramientas

1. Añade una función en `react_agent/tools.py` y regístrala en `TOOLS`
2. Actualiza la descripción en `react_agent/prompts.py`
