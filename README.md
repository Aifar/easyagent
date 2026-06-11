

# EasyAgent: Hand-Rolled ReAct Agent

                     

[Python 3.10+](https://www.python.org/downloads/)

[ReAct Loop](#-react-loop) · [Quick Start](#-quick-start) · [Project Structure](#-project-structure) · [Usage](#-usage-in-code) · [Extend](#-adding-tools)



---

A minimal **ReAct** (Reasoning and Acting) agent built in pure Python 

## 🔄 ReAct Loop

```
Thought → Action → Action Input → Observation → ... → Final Answer
```


| Step         | Description           | Produced by |
| ------------ | --------------------- | ----------- |
| Thought      | Internal reasoning    | LLM         |
| Action       | Tool name             | LLM         |
| Action Input | Tool arguments (JSON) | LLM         |
| Observation  | Tool result           | Your code   |
| Final Answer | Response to the user  | LLM         |


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

