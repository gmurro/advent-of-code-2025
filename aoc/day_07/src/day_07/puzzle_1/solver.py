from day_07.utils import Symbol, load_input


def solve(diagram: list[list[Symbol]]) -> int:
    count_beam_split = 0

    # Starting position of the beam
    current_beams_idx = {
        idx for idx, cell in enumerate(diagram[0]) if cell == Symbol.START
    }
    for line in diagram[1:]:
        next_beams_idx = set()
        for beam_idx in current_beams_idx:
            if line[beam_idx] == Symbol.SPLITTER:
                # add two new beams to the left and right
                count_beam_split += 1
                next_beams_idx.add(beam_idx - 1)
                next_beams_idx.add(beam_idx + 1)
            elif line[beam_idx] == Symbol.EMPTY_SPACE:
                # Beam continues straight
                next_beams_idx.add(beam_idx)

        current_beams_idx = next_beams_idx
    return count_beam_split


def main():
    diagram = load_input()
    result = solve(diagram)
    print(f"🎄📆 Day 07 - Puzzle 1 📆🎄\n✅ Solution:\n{result}")


if __name__ == "__main__":
    main()
