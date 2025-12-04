from copy import deepcopy
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


def remove_roll_papers(
    grid: list[list[int]], removed_rolls: int
) -> tuple[list[list[int]], int]:
    max_adjacent_rolls = 4

    new_grid = deepcopy(grid)
    new_removed_rolls = 0
    for i in range(len(new_grid)):
        for j in range(len(new_grid[0])):
            if (
                _is_roll(grid[i][j])
                and count_adjacent_rolls(grid, (i, j)) < max_adjacent_rolls
            ):
                new_grid[i][j] = "x"
                new_removed_rolls += 1
            else:
                new_grid[i][j] = grid[i][j]
    if new_removed_rolls == 0:
        return new_grid, removed_rolls
    else:
        return remove_roll_papers(new_grid, removed_rolls + new_removed_rolls)


def solve(grid: list[list[int]]) -> int:
    _, removed_roll_papers = remove_roll_papers(grid, 0)
    return removed_roll_papers


def main():
    data = load_input()
    result = solve(data)
    print(f"🎄📆 Day 04 - Puzzle 2 📆🎄\n✅ Solution:\n{result}")


if __name__ == "__main__":
    main()
