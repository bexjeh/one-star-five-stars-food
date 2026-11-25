import os

TEXT = "One star: the humans photograph their food until it goes cold, but the fried chicken alone justified the voyage."


def main():
    # Gate guard: the entry must be one sentence of 1-200 characters.
    assert 1 <= len(TEXT) <= 200, "entry outside 1-200 character gate"
    assert TEXT.count(".") == 1 and TEXT.endswith("."), "entry must be one sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
