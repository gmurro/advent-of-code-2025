from pathlib import Path


def load_input() -> list[list[str]]:
    input_path = Path(__file__).parent.parent / "input.txt"
    with input_path.open("r") as f:
        return [list(row) for row in f.read().splitlines()]


def _is_roll(value: str) -> bool:
    return value == "@"


def _is_invalid_position(
    position: tuple[int, int], max_rows: int, max_cols: int
) -> bool:
    position_x = position[0]
    position_y = position[1]
    return (
        position_x < 0
        or position_x >= max_rows
        or position_y < 0
        or position_y >= max_cols
    )


def count_adjacent_rolls(grid: list, position: tuple[int, int]) -> int:
    max_rows = len(grid)
    max_cols = len(grid[0])

    position_x = position[0]
    position_y = position[1]

    adjacent_positions = [
        (position_x - 1, position_y),  # Up
        (position_x + 1, position_y),  # Down
        (position_x, position_y - 1),  # Left
        (position_x, position_y + 1),  # Right
        (position_x - 1, position_y - 1),  # Up-Left
        (position_x - 1, position_y + 1),  # Up-Right
        (position_x + 1, position_y - 1),  # Down-Left
        (position_x + 1, position_y + 1),  # Down-Right
    ]

    # Filter out invalid positions
    adjacent_positions = [
        pos
        for pos in adjacent_positions
        if not _is_invalid_position(pos, max_rows, max_cols)
    ]

    # Count rolls in adjacent positions
    return sum([1 if _is_roll(grid[p[0]][p[1]]) else 0 for p in adjacent_positions])


def solve(grid: list[list[int]]) -> int:
    max_adjacent_rolls = 4
    roll_positions = [
        (i, j)
        for i in range(len(grid))
        for j in range(len(grid[0]))
        if _is_roll(grid[i][j])
    ]

    return sum(
        1
        for pos in roll_positions
        if count_adjacent_rolls(grid, pos) < max_adjacent_rolls
    )


def main():
    data = load_input()
    result = solve(data)
    print(f"🎄📆 Day 04 - Puzzle 1 📆🎄\n✅ Solution:\n{result}")


if __name__ == "__main__":
    main()
