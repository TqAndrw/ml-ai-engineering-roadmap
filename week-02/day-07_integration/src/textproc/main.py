from textproc import InputFileError, count_words, read_lines, tokenize


def main():
    try:
        lines = read_lines("sample.txt")
        words = tokenize(lines)
        counts = count_words(words)

    except InputFileError as e:
        print("Error:", e)

    else:
        for word, count in sorted(counts.items()):
            print(f"{word}: {count}")


if __name__ == "__main__":
    main()
