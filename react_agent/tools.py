import ast
import operator
from typing import Any

_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}


def _eval(node: ast.AST) -> float:
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return float(node.value)
    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPERATORS:
        return _OPERATORS[type(node.op)](_eval(node.operand))
    if isinstance(node, ast.BinOp) and type(node.op) in _OPERATORS:
        return _OPERATORS[type(node.op)](_eval(node.left), _eval(node.right))
    raise ValueError(f"unsupported expression: {ast.dump(node)}")


def calculator(args: dict[str, Any]) -> str:
    expression = args.get("expression", "").strip()
    if not expression:
        return "Error: expression is required."
    try:
        result = _eval(ast.parse(expression, mode="eval").body)
        return str(int(result)) if result == int(result) else str(result)
    except (SyntaxError, ValueError) as exc:
        return f"Error: {exc}"


TOOLS = {"calculator": calculator}
