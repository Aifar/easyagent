#!/usr/bin/env python3

import argparse
import sys

from react_agent import run_react_agent


def main() -> int:
    parser = argparse.ArgumentParser(description="ReAct calculator agent")
    parser.add_argument("query", nargs="?", default="What is 123 * 456?")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    answer = run_react_agent(args.query, verbose=not args.quiet)
    if args.quiet:
        print(answer)
    return 1 if answer.startswith("Error:") else 0


if __name__ == "__main__":
    sys.exit(main())
