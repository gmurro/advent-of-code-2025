from day_01.puzzle_2.solver import solve, rotate_dial


def test_puzzle_2_solve(puzzle_input):
    """Test puzzle 2 solver."""
    result = solve(puzzle_input, start_point=50)
    assert result == 6


def test_rotate_dial():
    assert rotate_dial(current_point=50, move="R1000") == (50, 10)
