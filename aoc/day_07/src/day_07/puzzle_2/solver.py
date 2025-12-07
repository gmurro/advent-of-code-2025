from day_07.utils import Symbol, load_input


def solve(diagram: list[list[Symbol]]) -> int:
    # Track number of paths leading to each beam position
    # Key: column index, Value: number of distinct paths to that position
    current_beam_paths = {}

    # Starting position of the beam
    for idx, cell in enumerate(diagram[0]):
        if cell == Symbol.START:
            current_beam_paths[idx] = 1

    for line in diagram[1:]:
        next_beam_paths = {}

        for beam_idx, path_count in current_beam_paths.items():
            if line[beam_idx] == Symbol.SPLITTER:
                # Beam splits into two, each inheriting the path count
                left_idx = beam_idx - 1
                right_idx = beam_idx + 1

                # Add paths to left beam
                next_beam_paths[left_idx] = (
                    next_beam_paths.get(left_idx, 0) + path_count
                )
                # Add paths to right beam
                next_beam_paths[right_idx] = (
                    next_beam_paths.get(right_idx, 0) + path_count
                )

            elif line[beam_idx] == Symbol.EMPTY_SPACE:
                # Beam continues straight, keeping its path count
                next_beam_paths[beam_idx] = (
                    next_beam_paths.get(beam_idx, 0) + path_count
                )

        current_beam_paths = next_beam_paths

    # Sum all the paths that reached the bottom
    return sum(current_beam_paths.values())


def main():
    diagram = load_input()
    result = solve(diagram)
    print(f"🎄📆 Day 07 - Puzzle 2 📆🎄\n✅ Solution:\n{result}")


if __name__ == "__main__":
    main()
