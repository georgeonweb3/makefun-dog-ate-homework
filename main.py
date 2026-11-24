#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes a single excuse (105 characters) to /output/entry.txt. The line is
the blind-tournament winner, 5-0: a dog that took "find x" literally, ate x,
and reports back that x tastes like chicken. The dog believes it has done
nothing wrong — it found x, exactly as instructed.
"""

import os

ENTRY = (
    "The worksheet said 'find x'. I found x. I ate x. "
    "X is inside me now, and honestly, x tastes like chicken."
)


def main() -> None:
    # Gate: the entry must be 1-200 characters of non-whitespace text.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, gate is 1-200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
