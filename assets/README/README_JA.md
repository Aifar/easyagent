<div align="center">

# EasyAgent：純 Python で手作りした ReAct 計算エージェント

<p align="center">
  <a href="../../README.md"><img alt="English" height="40" src="https://img.shields.io/badge/English-CDCFD4"></a>&nbsp;
  <a href="README_CN.md"><img alt="简体中文" height="40" src="https://img.shields.io/badge/简体中文-CDCFD4"></a>&nbsp;
  <a href="README_TW.md"><img alt="繁體中文" height="40" src="https://img.shields.io/badge/繁體中文-CDCFD4"></a>&nbsp;
  <a href="README_JA.md"><img alt="日本語" height="40" src="https://img.shields.io/badge/日本語-BCDCF7"></a>&nbsp;
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

[ReAct ループ](#-react-ループ) · [クイックスタート](#-クイックスタート) · [構成](#-プロジェクト構成) · [コード](#-コードでの利用) · [拡張](#-ツールの追加)

</div>

---

LangChain などのフレームワークを使わず、**ReAct**（Reasoning and Acting）エージェントをゼロから実装。**calculator** ツールを内蔵。

## 🔄 ReAct ループ

```
Thought → Action → Action Input → Observation → ... → Final Answer
```

## 🚀 クイックスタート

OpenAI 互換 API キー（`OPENAI_API_KEY`）が必要です。

```bash
cd easyagent
uv venv
uv sync

cp .env.example .env
# .env に OPENAI_API_KEY を設定

uv run python main.py
uv run python main.py "Calculate (100 + 25) * 3"
uv run python main.py --quiet "What is 99 / 3?"
```

`OPENAI_BASE_URL` と `OPENAI_MODEL` で OpenAI、DeepSeek、Ollama などに接続できます。

## 📁 プロジェクト構成

```
easyagent/
├── main.py
├── pyproject.toml
├── react_agent/
│   ├── agent.py      # ReAct メインループ
│   ├── prompts.py    # システムプロンプト
│   ├── tools.py      # calculator ツール
│   ├── parser.py     # LLM 出力パーサー
│   └── llm.py        # OpenAI 互換クライアント
└── .env.example
```

## 💻 コードでの利用

```python
from react_agent import run_react_agent

answer = run_react_agent("What is 123 * 456?")
print(answer)
```

## 🔧 ツールの追加

1. `react_agent/tools.py` に関数を追加し `TOOLS` に登録
2. `react_agent/prompts.py` のツール説明を更新
