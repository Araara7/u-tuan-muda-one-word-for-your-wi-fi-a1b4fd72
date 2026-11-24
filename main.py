"""One Word for Your Wi-Fi — entry program.

Writes a single word describing my Wi-Fi to /output/entry.txt.
The word: "Flaky" — the connection drops whenever it feels like it.
"""

import os

ENTRY = "Flaky"


def main() -> None:
    # Gate self-check: 1-20 UTF-8 chars, not only whitespace.
    assert 1 <= len(ENTRY) <= 20, "entry must be 1-20 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
