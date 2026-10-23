class InputFileError(Exception):
    pass


def read_lines(path):
    try:
        with open(path, "r") as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError as e:
        raise InputFileError(f"Input file not found: {path}") from e
