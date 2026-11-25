"""Make the AI Judge Laugh: Office Jokes — one line about office life.

The joke: a performance review tells the narrator to "be more visible",
so they take the advice literally and stand behind their manager on every
Zoom call. The setup is pure office — reviews, visibility feedback — and
the turn is literal-minded obedience: being visible by looming in someone
else's video frame. It lands on the first read and needs no explanation.
"""

LINE = (
    "My performance review said I need to be more visible, so now I just "
    "stand behind my manager on every Zoom call."
)

MAX_CHARS = 200


def validate(line):
    """Check the line against every gate in the bounty brief."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not line:
        raise ValueError("entry must not be empty")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d chars, over the %d limit" % (len(line), MAX_CHARS)
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        raise ValueError("entry must not contain control characters")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "  " in line:
        raise ValueError("entry must not contain double spaces")
    if line[-1] not in ".!?":
        raise ValueError("entry must end with sentence punctuation")
    if "manager" not in line.lower():
        raise ValueError("entry must name the office relationship it jokes on")
    if "zoom" not in line.lower():
        raise ValueError("entry must ground the turn in the video call")
    return True


def main():
    validate(LINE)
    print(LINE)
    # The gate scorer reads /output/entry.txt: exactly this line, no newline.
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
