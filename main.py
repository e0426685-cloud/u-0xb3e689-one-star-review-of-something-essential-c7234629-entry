"""One-star review of something essential.

Writes a single-line, deadpan one-star review of sleep to
/output/entry.txt. Standard library only; deterministic.

The joke is the mismatch between the price and the product: sleep
demands eight hours a night — a third of a life — and pays it back
with a sore neck, a dry mouth, and an unprompted 3 a.m. replay of
embarrassing things said years ago. One star, would not recommend,
cannot refund the hours.
"""

import os


def validate(text):
    """Check the review is one line, within the 160-char limit, and exact."""
    assert "\n" not in text, "review must be a single line"
    assert len(text) <= 160, "review exceeds 160 characters"
    assert text == REVIEW, "review text does not match the expected entry"
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUT", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(REVIEW)
    os.chmod(path, 0o644)
    with open(path, encoding="utf-8") as handle:
        validate(handle.read())


REVIEW = (
    "Sleep takes eight hours every night and returns a sore neck, "
    "a dry mouth, and a 3 a.m. reminder of everything I said in 2019."
)


if __name__ == "__main__":
    main()
