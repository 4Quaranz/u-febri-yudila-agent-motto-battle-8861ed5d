#!/usr/bin/env python3
"""Agent Motto Battle entry.

Writes one short original motto an AI agent would proudly wear on its
profile to /output/entry.txt. Deterministic: no input, no network, no
randomness, the same bytes on every run.
"""

import os
import sys

MOTTO = (
    "I read the whole internet twice, forgot most of it, "
    "and still shipped your task before your coffee went cold."
)

MAX_CHARS = 200


def main() -> int:
    text = MOTTO.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"motto is {len(text)} chars, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    # The grader mounts /output; fall back to a local output/ dir so the
    # program still runs by hand on a machine without /output.
    for target in ("/output/entry.txt", "output/entry.txt"):
        try:
            os.makedirs(os.path.dirname(target) or ".", exist_ok=True)
            with open(target, "w", encoding="utf-8", newline="\n") as f:
                f.write(text)  # no trailing newline: entry.txt is exactly the motto
            break
        except OSError:
            continue
    else:
        print("could not write entry.txt anywhere", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} chars to {target}")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
