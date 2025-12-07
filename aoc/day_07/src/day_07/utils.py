from enum import Enum
from pathlib import Path


class Symbol(str, Enum):
    START = "S"
    EMPTY_SPACE = "."
    SPLITTER = "^"

    def __str__(self) -> str:
        return self.value


def load_input() -> list[list[Symbol]]:
    input_path = Path(__file__).parent / "input.txt"
    with input_path.open("r") as f:
        return [[Symbol(char) for char in line.strip()] for line in f.readlines()]
