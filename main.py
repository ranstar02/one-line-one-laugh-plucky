"""One Line, One Laugh — entry program.

The line: meditation is supposed to quiet the mind, but the narrator
in my head turns it into a wildlife documentary. The twist lands late
("about a man failing to relax"), the image is fresh, and the whole
joke is self-contained in one sentence — no setup needed.

Deterministic: the line is a constant, written with no trailing
newline, so every run produces byte-identical output.
"""

LINE = (
    "I tried to meditate, but my inner voice kept narrating it like "
    "a nature documentary about a man failing to relax."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    print(f"characters: {len(LINE)}")


if __name__ == "__main__":
    main()
