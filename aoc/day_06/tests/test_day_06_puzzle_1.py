from day_06.puzzle_1.solver import solve


def test_puzzle_1_solve(puzzle_1_input):
    """Test puzzle 1 solver."""
    result = solve(puzzle_1_input)
    assert result == 4277556
