from day_05.puzzle_2.solver import solve


def test_puzzle_2_solve(puzzle_input):
    """Test puzzle 2 solver."""
    fresh_ingredient_ranges, _ = puzzle_input
    result = solve(fresh_ingredient_ranges)
    assert result == 14
