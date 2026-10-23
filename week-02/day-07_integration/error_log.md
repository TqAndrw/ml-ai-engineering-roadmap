# Week 2 Error Log

## Iterators and generators
- Initially described iterable as an item being looped.
- Correct model: an iterable can produce an iterator; an iterator stores iteration state and supports `next()`.
- Forgot that generators are one-shot and become exhausted after consumption.

## Modules
- Initially reversed direct execution vs import behavior of `__name__`.
- Correct model: directly executed module has `__name__ == "__main__"`.

## Exceptions
- Initially guessed invalid `int()` conversion raised `InvalidType`.
- Correct exception: `ValueError`.
- JSON parsing errors use `json.JSONDecodeError`.

## Integration
- Initially assumed `read_lines()` opens the file when the generator is created.
- Correct model: generator body begins execution only when iteration starts.
