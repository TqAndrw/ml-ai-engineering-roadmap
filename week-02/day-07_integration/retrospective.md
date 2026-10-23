# Week 2 Retrospective

## What I learned
- Python names bind to objects.
- Mutable objects can expose aliasing side effects.
- Functions use local bindings and LEGB name lookup.
- Lists, tuples, sets and dictionaries serve different data-model needs.
- Iterators maintain iteration state; generators provide lazy iteration.
- Modules and packages help separate responsibilities and expose clean APIs.
- Exceptions should distinguish recoverable failures from programming bugs.
- Context managers safely manage resources such as files.

## Integration lesson
The mini-app separates:
- I/O and file errors in `io.py`
- text processing in `processor.py`
- orchestration in `main.py`

Generators allow lines and words to flow through the pipeline lazily.

## Design improvement
`unique_words()` is currently unused and should either be removed or integrated deliberately rather than left as dead code.
