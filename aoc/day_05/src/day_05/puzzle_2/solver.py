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


def overlap(range_a: range, range_b: range) -> bool:
    """ "Check if two ranges overlap"""
    return range_a.stop >= range_b.start and range_b.stop >= range_a.start


def sort_ingredient_ranges(ranges: list[range]) -> list[range]:
    """Sort ranges by their start value"""
    return sorted(ranges, key=lambda r: r.start)


def solve(fresh_ingredient_ranges: list[range]) -> int:
    """Count all of the IDs that the fresh ingredient ID ranges consider to be fresh"""
    sorted_ranges = sort_ingredient_ranges(fresh_ingredient_ranges)
    max_stop = 0
    count = sorted_ranges[0].stop - sorted_ranges[0].start
    for i in range(1, len(sorted_ranges)):
        current_range = sorted_ranges[i]
        previous_range = sorted_ranges[i - 1]

        # Update the max stop seen so far
        max_stop = max(max_stop, previous_range.stop)
        if overlap(current_range, range(previous_range.start, max_stop)):
            # Ranges overlap, only add the non-overlapping part
            if current_range.stop > max_stop:
                count += current_range.stop - max_stop
        else:
            # No overlap, add the entire range
            count += current_range.stop - current_range.start
    return count


def main():
    fresh_ingredient_ranges, _ = load_input()
    result = solve(fresh_ingredient_ranges)
    print(f"🎄📆 Day 04 - Puzzle 2 📆🎄\n✅ Solution:\n{result}")


if __name__ == "__main__":
    main()
