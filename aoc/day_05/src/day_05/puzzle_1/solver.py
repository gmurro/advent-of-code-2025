from pathlib import Path


def load_input() -> tuple[list[range], list[int]]:
    input_path = Path(__file__).parent.parent / "input.txt"
    with input_path.open("r") as f:
        fresh_ranges, ingredient_ids = f.read().split("\n\n", maxsplit=2)
        return [
            range(
                int(r.split("-", maxsplit=2)[0]), int(r.split("-", maxsplit=2)[1]) + 1
            )
            for r in fresh_ranges.splitlines()
        ], [int(ingredient_id) for ingredient_id in ingredient_ids.splitlines()]


def solve(fresh_ingredient_ranges: list[range], ingredient_ids: list[int]) -> int:
    return sum([
        1
        for ingredient_id in ingredient_ids
        if any(ingredient_id in r for r in fresh_ingredient_ranges)
    ])


def main():
    fresh_ingredient_ranges, ingredient_ids = load_input()
    result = solve(fresh_ingredient_ranges, ingredient_ids)
    print(f"🎄📆 Day 04 - Puzzle 1 📆🎄\n✅ Solution:\n{result}")


if __name__ == "__main__":
    main()
