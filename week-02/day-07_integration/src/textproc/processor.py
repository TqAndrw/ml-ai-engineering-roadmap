def tokenize(lines):
    for line in lines:
        for word in line.split():
            yield word.lower()


def count_words(words):
    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts


def unique_words(words):
    return set(words)
