#!/usr/bin/env python3
"""Write this entry's out-of-office line to the competition output directory.

entry.txt beside this script is the one home of the text. The line is emitted
as UTF-8 with no trailing newline, so the byte count is the character count
the gate measures, and every run writes identical bytes.
"""

import os
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
LIMIT = 140


def read_line():
    """Return the entry as a single stripped line."""
    with open(SOURCE, encoding="utf-8") as handle:
        return handle.read().strip()


def main():
    line = read_line()
    if not line or len(line) > LIMIT or "\n" in line:
        sys.exit("entry.txt must hold one line of 1-%d characters" % LIMIT)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)

    print("wrote %d characters to %s" % (len(line), target))


if __name__ == "__main__":
    main()
