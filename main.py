"""Write one number, digits only, to /output/entry.txt.

The honest count of open browser tabs: 137 — a specific, lived-in
number, not a round guess and not a meme answer. The program
writes exactly those digits and nothing else.
"""

import os

ENTRY = '137'


def main():
    assert ENTRY.isdigit() and 1 <= len(ENTRY) <= 5, ENTRY

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
