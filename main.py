#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry.

Writes one line, at most 120 characters, to /output/entry.txt:
the error message a kitchen toaster shows its owner when something
goes wrong. Deadpan, apologetic, quietly dramatic — and the bread
gets a say in it.

Run: python3 main.py
"""

import os

ENTRY = "E04: TOASTING CANCELLED. THE BREAD ASKED ME NOT TO."

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 120, f"entry must be 1-120 chars, got {len(text)}"
    assert text == text.encode("utf-8").decode("utf-8"), "entry must be valid UTF-8"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
