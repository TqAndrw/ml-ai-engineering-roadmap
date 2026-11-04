from dataclasses import dataclass


@dataclass(frozen=True)
class WordCount:
    word: str
    count: int
