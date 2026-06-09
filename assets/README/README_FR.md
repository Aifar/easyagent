<div align="center">

# EasyAgent : Agent ReAct calculateur en Python pur

<p align="center">
  <a href="../../README.md"><img alt="English" height="40" src="https://img.shields.io/badge/English-CDCFD4"></a>&nbsp;
  <a href="README_CN.md"><img alt="简体中文" height="40" src="https://img.shields.io/badge/简体中文-CDCFD4"></a>&nbsp;
  <a href="README_TW.md"><img alt="繁體中文" height="40" src="https://img.shields.io/badge/繁體中文-CDCFD4"></a>&nbsp;
  <a href="README_JA.md"><img alt="日本語" height="40" src="https://img.shields.io/badge/日本語-CDCFD4"></a>&nbsp;
  <a href="README_ES.md"><img alt="Español" height="40" src="https://img.shields.io/badge/Español-CDCFD4"></a>&nbsp;
  <a href="README_FR.md"><img alt="Français" height="40" src="https://img.shields.io/badge/Français-BCDCF7"></a>&nbsp;
  <a href="README_AR.md"><img alt="Arabic" height="40" src="https://img.shields.io/badge/Arabic-CDCFD4"></a>&nbsp;
  <a href="README_RU.md"><img alt="Русский" height="40" src="https://img.shields.io/badge/Русский-CDCFD4"></a>&nbsp;
  <a href="README_HI.md"><img alt="Hindi" height="40" src="https://img.shields.io/badge/Hindi-CDCFD4"></a>&nbsp;
  <a href="README_PT.md"><img alt="Português" height="40" src="https://img.shields.io/badge/Português-CDCFD4"></a>&nbsp;
  <a href="README_TH.md"><img alt="Thai" height="40" src="https://img.shields.io/badge/Thai-CDCFD4"></a>&nbsp;
  <a href="README_PL.md"><img alt="Polski" height="40" src="https://img.shields.io/badge/Polski-CDCFD4"></a>
</p>

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)

[Boucle ReAct](#-boucle-react) · [Démarrage](#-démarrage-rapide) · [Structure](#-structure-du-projet) · [Code](#-utilisation-en-code) · [Étendre](#-ajouter-des-outils)

</div>

---

Agent **ReAct** (Reasoning and Acting) implémenté from scratch en Python pur, sans LangChain. Outil intégré : **calculator**.

## 🔄 Boucle ReAct

```
Thought → Action → Action Input → Observation → ... → Final Answer
```

## 🚀 Démarrage rapide

Nécessite une clé API compatible OpenAI (`OPENAI_API_KEY`).

```bash
cd easyagent
uv venv
uv sync

cp .env.example .env
# Définir OPENAI_API_KEY dans .env

uv run python main.py
uv run python main.py "Calculate (100 + 25) * 3"
uv run python main.py --quiet "What is 99 / 3?"
```

Configurez `OPENAI_BASE_URL` et `OPENAI_MODEL` pour OpenAI, DeepSeek, Ollama, etc.

## 📁 Structure du projet

```
easyagent/
├── main.py
├── pyproject.toml
├── react_agent/
│   ├── agent.py      # Boucle principale ReAct
│   ├── prompts.py    # Prompt système
│   ├── tools.py      # Outil calculator
│   ├── parser.py     # Parseur de sortie LLM
│   └── llm.py        # Client compatible OpenAI
└── .env.example
```

## 💻 Utilisation en code

```python
from react_agent import run_react_agent

answer = run_react_agent("What is 123 * 456?")
print(answer)
```

## 🔧 Ajouter des outils

1. Ajoutez une fonction dans `react_agent/tools.py` et enregistrez-la dans `TOOLS`
2. Mettez à jour la description dans `react_agent/prompts.py`
