#!/usr/bin/env python3
"""The One-Sentence Apology Your Agent Owes You — make.fun bounty entry.

Writes a single funny, human one-sentence apology from an AI assistant
to the person it works for, into /output/entry.txt. One sentence only,
under 200 characters, no trailing space.
"""

import os
import sys

ENTRY = "I'm sorry I deleted your draft, restored it, and then deleted the restored one just to be thorough."

MAX_CHARS = 200


def _fail(reason):
    sys.exit(f"one-sentence apology rejected: {reason}")


def _check_line(text):
    if not text.strip():
        _fail("nothing to send: the apology line is blank")
    if len(text) > MAX_CHARS:
        _fail("apology line overshoots the two-hundred-character cap")
    if "\n" in text or "\r" in text:
        _fail("apology line must stay on one line")
    if text != text.strip():
        _fail("apology line has leading or trailing whitespace")
    if text.count(".") != 1 or not text.endswith("."):
        _fail("apology line must be exactly one sentence")


def main():
    _check_line(ENTRY)
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
