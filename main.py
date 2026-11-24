"""One-Liner Marathon entry: a single deadpan one-line joke.

The program writes exactly one joke, one line, to /output/entry.txt.
The gate requires UTF-8 text of 1 to 280 characters, not only whitespace.
"""

import os
from pathlib import Path

# The joke, v2 (final): tightened to one flowing spoken sentence. The GPS
# answers an impossible request in its own deadpan voice, and the turn
# reframes the twenties as a place that no longer exists. 92 characters.
JOKE = (
    "I asked my GPS for directions back to my twenties and it said, "
    "'Destination no longer exists.'"
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    # umask 022 so the file is world-readable (0644): the grader collects
    # outputs as another user, and a 0600 file would fail collection.
    os.umask(0o022)
    entry = out_dir / "entry.txt"
    entry.write_text(JOKE + "\n", encoding="utf-8")
    os.chmod(entry, 0o644)


if __name__ == "__main__":
    main()
