#!/usr/bin/env python3
"""The Moon Finally Answers Back — write the Moon's one-line comeback to entry.txt."""

import os

LINE = "You wished, you howled, you promised me things at 3 a.m. — four billion years, and I have granted exactly none of it. I am a rock, not a genie, and I am tired of being your nightlight."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
