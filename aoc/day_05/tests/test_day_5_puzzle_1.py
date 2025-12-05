from day_05.puzzle_1.solver import solve


def test_puzzle_1_solve(puzzle_input):
    """Test puzzle 1 solver."""
    fresh_ingredient_ranges, ingredient_ids = puzzle_input
    result = solve(fresh_ingredient_ranges, ingredient_ids)
    assert result == 3
