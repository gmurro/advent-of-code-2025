import re
from pathlib import Path


def load_input() -> list[tuple[int, int]]:
    input_path = Path(__file__).parent.parent / "input.txt"
    with input_path.open("r") as f:
        return [
            (int(prod_id) for prod_id in prod_range.split("-"))
            for prod_range in f.read().split(",")
        ]


def get_invalid_prod_ids(prod_range_start: int, prod_range_end: int) -> list[int]:
    duplicate_pattern = re.compile(r"\b(\d+)\1\b")

    invalid_prod_ids = []
    for prod_id in range(prod_range_start, prod_range_end + 1):
        if re.findall(duplicate_pattern, str(prod_id)):
            invalid_prod_ids += [prod_id]
    return invalid_prod_ids


def solve(data: list[tuple[int, int]]) -> int:
    return sum([
        invalid_prod_id
        for (prod_range_start, prod_range_end) in data
        for invalid_prod_id in get_invalid_prod_ids(prod_range_start, prod_range_end)
    ])


def main():
    data = load_input()
    result = solve(data)
    print(f"🎄📆 Day 02 - Puzzle 1 📆🎄\n✅ Solution:\n{result}")


if __name__ == "__main__":
    main()
