# W03D1 — Typing, Dataclasses & Pythonic Interfaces

## Core ideas

- Type hints help humans, IDEs, and static type checkers.
- Type hints do **not** automatically enforce types at runtime.
- `str | None` means a value may be either `str` or `None`.
- `@dataclass` can generate useful methods such as `__init__`, `__repr__`, and `__eq__`.
- `frozen=True` prevents field reassignment, but nested mutable objects may still change.
- Duck typing focuses on behavior rather than concrete class inheritance.
- `Protocol` describes an expected interface for static type checking.
- Generics preserve relationships between input and output types.
- Prefer abstract capabilities such as `Iterable[str]` when a function only needs to iterate, instead of requiring a concrete type like `list[str]`.

## Typed pipeline

```python
def tokenize(lines: Iterable[str]) -> Iterator[str]:
    ...

def count_words(words: Iterable[str]) -> list[WordCount]:
    ...
```

This makes the function contracts explicit while keeping the pipeline flexible.
