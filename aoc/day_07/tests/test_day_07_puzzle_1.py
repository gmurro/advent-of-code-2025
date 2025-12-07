from day_07.puzzle_1.solver import solve


def test_puzzle_1_solve(puzzle_input):
    """Test puzzle 1 solver."""
    result = solve(puzzle_input)
    assert result == 21
