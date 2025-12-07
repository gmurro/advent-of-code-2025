from functools import reduce
from operator import mul
from pathlib import Path

from day_06.utils import Operation, parse_worksheet_horizontally


def load_input() -> list[tuple[list[int], Operation]]:
    """Load and parse the math worksheet from input file."""
    input_path = Path(__file__).parent.parent / "input.txt"
    with input_path.open("r") as f:
        worksheet_data = f.read()
    return parse_worksheet_horizontally(worksheet_data)


def solve(problems: list[tuple[list[int], Operation]]) -> int:
    """Calculate the grand total by solving all problems and summing the results.

    Args:
        problems: List of (numbers, operation) tuples representing math problems

    Returns:
        Grand total of all problem solutions
    """
    return sum([
        sum(numbers) if operation == Operation.ADD else reduce(mul, numbers)
        for numbers, operation in problems
    ])


def main():
    homeworks = load_input()
    result = solve(homeworks)
    print(f"🎄📆 Day 06 - Puzzle 1 📆🎄\n✅ Solution:\n{result}")


if __name__ == "__main__":
    main()
