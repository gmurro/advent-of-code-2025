import pytest


@pytest.fixture
def puzzle_input():
    """Puzzle input fixture."""
    data = """987654321111111
811111111111119
234234234234278
818181911112111
"""
    return [[int(battery) for battery in list(bank)] for bank in data.splitlines()]
