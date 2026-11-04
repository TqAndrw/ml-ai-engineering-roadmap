from .processor import count_words, tokenize


def main() -> None:
    lines: list[str] = [
        "apple banana apple",
        "banana orange",
        "apple kiwi banana",
    ]

    words = tokenize(lines)
    results = count_words(words)

    for result in results:
        print(f"{result.word}: {result.count}")


if __name__ == "__main__":
    main()
