#!/usr/bin/env python3
"""Make the Judge Smile — one line about a small good thing that happened today.

Writes the entry to /output/entry.txt: exactly one line, UTF-8, no trailing
newline, 1 to 200 characters per the bounty gate.
"""

import os

ENTRY = "The elevator arrived before I pressed the button, because someone inside had held the door, and for one second the whole building felt like it was looking out for me."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
