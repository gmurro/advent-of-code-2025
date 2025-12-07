from day_06.puzzle_2.solver import solve


def test_puzzle_2_solve(puzzle_2_input):
    """Test puzzle 2 solver."""
    result = solve(puzzle_2_input)
    assert result == 3263827
