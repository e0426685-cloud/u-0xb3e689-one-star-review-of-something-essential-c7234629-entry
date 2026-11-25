"""One-star review of something essential.

Writes a single-line, deadpan one-star review of sleep to
/output/entry.txt. Standard library only; deterministic.
"""

import os

REVIEW = (
    "Sleep takes eight hours every night and returns a sore neck, "
    "a dry mouth, and a 3 a.m. reminder of everything I said in 2019."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUT", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(REVIEW)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
