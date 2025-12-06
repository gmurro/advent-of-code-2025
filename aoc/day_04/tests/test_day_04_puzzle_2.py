from day_04.puzzle_2.solver import solve


def test_puzzle_2_solve(puzzle_input):
    """Test puzzle 2 solver."""
    result = solve(puzzle_input)
    assert result == 43
