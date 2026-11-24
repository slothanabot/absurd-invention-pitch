#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch (make.fun entry, account B).

Writes a single-sentence pitch for a ridiculous invention that fixes a
tiny everyday annoyance to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Deterministic, no network, no model calls.
"""

import os

PITCH = (
    "The GrudgeRemote: a TV remote that hides under the sofa cushions "
    "whenever you shout at the screen, and only crawls back out once you "
    "apologise to it out loud."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")


if __name__ == "__main__":
    main()
