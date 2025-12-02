from pathlib import Path


def load_input() -> list[str]:
    input_path = Path(__file__).parent.parent / "input.txt"
    with input_path.open("r") as f:
        return f.read().splitlines()


def rotate_dial(current_point: int, move: str) -> tuple[int, int]:
    """
    Rotate the dial based on the move instruction.
    """
    num_points = 100

    try:
        direction, distance = move[0], int(move[1:])

        match direction:
            case "L":
                new_pos = (current_point - distance) % num_points
                # Count zeros: we hit 0 at clicks i where (P - i) % 100 == 0
                # This happens at i = P, P+100, P+200, ... (for P > 0)
                # or i = 100, 200, 300, ... (for P == 0)
                if current_point > 0:
                    zero_count = (
                        (1 + (distance - current_point) // num_points)
                        if distance >= current_point
                        else 0
                    )
                else:  # current_point == 0
                    zero_count = distance // num_points
                return new_pos, zero_count
            case "R":
                new_pos = (current_point + distance) % num_points
                zero_count = (current_point + distance) // num_points
                return new_pos, zero_count
            case _:
                raise ValueError(f"Invalid direction '{direction}' for move '{move}'")

    except Exception as e:
        raise ValueError(f"Invalid move: {move}") from e


def solve(data: list[str], start_point: int = 50) -> int:
    count_zero = 0
    current_point = start_point
    for move in data:
        current_point, zero_rotations = rotate_dial(current_point, move)
        count_zero += zero_rotations
    return count_zero


def main():
    data = load_input()
    result = solve(data)
    print(f"🎄📆 Day 01 - Puzzle 2 📆🎄\n✅ Solution:\n{result}")


if __name__ == "__main__":
    main()
