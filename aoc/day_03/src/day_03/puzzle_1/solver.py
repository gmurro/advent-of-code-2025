from pathlib import Path

import numpy as np


def load_input() -> list[list[int]]:
    input_path = Path(__file__).parent.parent / "input.txt"
    with input_path.open("r") as f:
        return [
            [int(battery) for battery in list(bank)] for bank in f.read().splitlines()
        ]


def calculate_max_bank_joltage(
    battery_bank: list[int], batteries_remaining: int
) -> int:
    """
    Calculate maximum joltage by selecting batteries from the bank.

    Args:
        battery_bank: List of battery joltage ratings (1-9)
        batteries_remaining: Number of batteries still to select

    Returns:
        Maximum joltage achievable by concatenating selected battery digits
    """
    if batteries_remaining <= 0:
        return max(battery_bank)
    else:
        # Find the position of the highest joltage battery in the valid range
        best_battery_position = np.argmax(battery_bank[:-batteries_remaining]).tolist()
        # Concatenate this battery with the best choice from remaining batteries
        return int(
            f"{battery_bank[best_battery_position]}{calculate_max_bank_joltage(battery_bank[best_battery_position + 1 :], batteries_remaining - 1)}"
        )


def solve(battery_banks: list[list[int]]) -> int:
    batteries_to_select = 2
    return sum([
        calculate_max_bank_joltage(bank, batteries_remaining=batteries_to_select - 1)
        for bank in battery_banks
    ])


def main():
    data = load_input()
    result = solve(data)
    print(f"🎄📆 Day 03 - Puzzle 1 📆🎄\n✅ Solution:\n{result}")


if __name__ == "__main__":
    main()
