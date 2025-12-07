import pytest

from day_06.utils import (
    Operation,
    parse_worksheet_horizontally,
    parse_worksheet_vertically,
)


@pytest.fixture
def example_worksheet() -> str:
    """Shared example worksheet data from puzzle description."""
    return """123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
"""


@pytest.fixture
def puzzle_1_input(example_worksheet: str) -> list[tuple[list[int], Operation]]:
    """Puzzle 1 input: worksheet parsed horizontally."""
    return parse_worksheet_horizontally(example_worksheet)


@pytest.fixture
def puzzle_2_input(example_worksheet: str) -> list[tuple[list[int], Operation]]:
    """Puzzle 2 input: worksheet parsed vertically."""
    return parse_worksheet_vertically(example_worksheet)
