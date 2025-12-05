import pytest


@pytest.fixture
def puzzle_input() -> tuple[list[range], list[int]]:
    """Puzzle input fixture."""
    data = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""
    fresh_ranges, ingredient_ids = data.split("\n\n", maxsplit=2)
    return [
        range(int(r.split("-", maxsplit=2)[0]), int(r.split("-", maxsplit=2)[1]) + 1)
        for r in fresh_ranges.splitlines()
    ], [int(ingredient_id) for ingredient_id in ingredient_ids.splitlines()]
