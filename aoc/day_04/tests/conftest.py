import pytest


@pytest.fixture
def puzzle_input() -> list[list[int]]:
    """Puzzle input fixture."""
    grid = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""
    return [list(row) for row in grid.splitlines()]
