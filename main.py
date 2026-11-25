"""The Internet in One Word.

Writes a single word to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt). Pure stdlib only.

The word: Oops

Why this word: the whole internet, in one beat, is one long accident.
Every viral post, every leaked screenshot, every reply sent to the
wrong group chat, every typo that became a meme, every "delete this"
that was already screenshotted — the internet runs on oops. It is
funny by itself with no explanation needed, it says something true
about the internet as a whole rather than one app or one mood, it is
not the first obvious word anyone reaches for (doomscrolling,
brainrot, buffering), and at four letters it lands before the reader
has time to think. It makes you laugh, then nod.
"""

import os
import sys

WORD = "Oops"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may be a directory or a full file path.
    if out_dir.endswith(".txt"):
        path = out_dir
        directory = os.path.dirname(path) or "."
    else:
        directory = out_dir
        path = os.path.join(directory, "entry.txt")
    os.makedirs(directory, exist_ok=True)

    # Gate: /output/entry.txt must be UTF-8 text of 1 to 30 characters,
    # not only white space, a single word.
    if not (1 <= len(WORD) <= 30):
        print("gate fail: word must be 1-30 chars, got %d" % len(WORD),
              file=sys.stderr)
        return 1
    if not WORD.strip() or len(WORD.split()) != 1:
        print("gate fail: entry must be a single word", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)

    # Byte-exact read-back verification.
    with open(path, "rb") as f:
        raw = f.read()
    if raw.decode("utf-8") != WORD:
        print("gate fail: read-back mismatch", file=sys.stderr)
        return 1
    print("wrote %d chars (%d bytes) to %s" % (len(WORD), len(raw), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
