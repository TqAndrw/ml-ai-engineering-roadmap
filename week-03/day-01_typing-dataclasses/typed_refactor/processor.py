from collections.abc import Iterable, Iterator

from .models import WordCount


def tokenize(lines: Iterable[str]) -> Iterator[str]:
    for line in lines:
        for word in line.split():
            yield word.lower()


def count_words(words: Iterable[str]) -> list[WordCount]:
    counts: dict[str, int] = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return [
        WordCount(word=word, count=count)
        for word, count in sorted(counts.items())
    ]
