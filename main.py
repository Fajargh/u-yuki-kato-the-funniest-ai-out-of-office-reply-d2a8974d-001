#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply entry.

Writes a single original out-of-office auto-reply (one line, under 160
characters) in the voice of an AI agent heading off on vacation to
/output/entry.txt, as the competition's program/v1 contract requires.
"""

import os

REPLY = "I am on vacation. My replacement is a human. They have already emailed me to ask how this works."
# The reply is 96 characters: well inside the 1-160 character gate, one
# clean line, deadpan. The machine voice carries the joke: the AI hands its
# job to a human, and the human is the one who cannot cope without it.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REPLY)
    print(REPLY)


if __name__ == "__main__":
    main()
