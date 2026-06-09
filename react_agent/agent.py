import os

from react_agent.llm import call_llm, require_api_key
from react_agent.parser import extract_action, extract_action_input, extract_final_answer
from react_agent.prompts import SYSTEM_PROMPT
from react_agent.tools import TOOLS


def run_react_agent(query: str, *, max_iterations: int | None = None, verbose: bool = True) -> str:
    require_api_key()
    limit = max_iterations or int(os.getenv("MAX_ITERATIONS", "10"))
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": query},
    ]

    for i in range(1, limit + 1):
        if verbose:
            print(f"\n--- Iteration {i} ---")

        response = call_llm(messages)
        messages.append({"role": "assistant", "content": response})
        if verbose:
            print(response)

        final_answer = extract_final_answer(response)
        if final_answer:
            if verbose:
                print(f"\nFinal Answer: {final_answer}")
            return final_answer

        action = extract_action(response)
        tool = TOOLS.get(action or "")
        if not tool:
            observation = f"Error: unknown tool '{action}'. Use calculator."
        else:
            observation = tool(extract_action_input(response))
            if verbose:
                print(f"[Tool] {action} -> {observation}")

        messages.append({"role": "user", "content": f"Observation: {observation}"})

    return "Error: maximum iterations reached."
