import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def require_api_key() -> str:
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is required. Copy .env.example to .env and set your API key.")
    return api_key


def call_llm(messages: list[dict[str, str]]) -> str:
    client = OpenAI(
        api_key=require_api_key(),
        base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1"),
    )
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content or ""
