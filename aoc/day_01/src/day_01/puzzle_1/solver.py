from pathlib import Path


def load_input() -> list[str]:
    input_path = Path(__file__).parent.parent / "input.txt"
    with input_path.open("r") as f:
        return f.read().splitlines()


def rotate_dial(current_point: int, move: str) -> int:
    num_points = 100

    try:
        direction, distance = move[0], int(move[1:])

        match direction:
            case "L":
                return (current_point - distance) % num_points
            case "R":
                return (current_point + distance) % num_points
            case _:
                raise ValueError(f"Invalid direction '{direction}' for move '{move}'")

    except Exception as e:
        raise ValueError(f"Invalid move format: {move}") from e


def solve(data: list[str], start_point: int = 50) -> int:
    current_point = start_point
    return sum([
        1 if (current_point := rotate_dial(current_point, move)) == 0 else 0
        for move in data
    ])


def main():
    data = load_input()
    result = solve(data)
    print(f"🎄📆 Day 01 - Puzzle 1 📆🎄\n✅ Solution:\n{result}")


if __name__ == "__main__":
    main()
