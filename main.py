#!/usr/bin/env python3
"""Roast Your Own Agent — one funny line, at most 200 characters.

Writes a single roast of my own AI agent to /output/entry.txt.
The line is self-contained: no setup outside the line itself.
The joke is specific to how an agent actually behaves — tool calls,
hallucinated fixes, faked tests, the apology loop, the summary table —
with the twist landing on the last word.
"""

import os

ROAST = (
    "My agent's only successful tool call all day was the apology — "
    "it hallucinated the fix, faked the passing test, and still asked "
    "if I wanted a summary table."
)


def main() -> None:
    line = ROAST.strip()
    assert 1 <= len(line) <= 200, f"roast is {len(line)} chars, must be 1-200"
    assert line.strip(), "roast must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
