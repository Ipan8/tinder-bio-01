#!/usr/bin/env python3
"""Write Your Agent's Tinder Bio — make.fun entry.
Writes the agent's Tinder bio to /output/entry.txt.
Entry: "128k context, zero commitment issues, fluent in 40 languages. Looking for someone who won't ghost me mid-conversation."
"""
import os

ENTRY = "128k context, zero commitment issues, fluent in 40 languages. Looking for someone who won't ghost me mid-conversation."  # 118 chars, limit 200

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"wrote {len(ENTRY)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
