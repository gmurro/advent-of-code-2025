from enum import Enum

import numpy as np


class Operation(str, Enum):
    ADD = "+"
    MULTIPLY = "*"

    def __str__(self) -> str:
        return self.value


def parse_worksheet_horizontally(
    worksheet_data: str,
) -> list[tuple[list[int], Operation]]:
    """Parse math worksheet reading problems horizontally in columns.

    Each problem's numbers are arranged vertically in a column.
    Problems are separated by columns of spaces.
    The bottom row contains the operation symbols.

    Args:
        worksheet_data: Raw worksheet text with numbers and operations

    Returns:
        List of problems, each as (numbers, operation) tuple
    """
    rows = worksheet_data.strip().splitlines()
    number_rows = rows[:-1]
    operation_symbols = rows[-1].split()

    # Parse numbers into a matrix (each row is a line, each column is a problem)
    number_matrix = np.array([[int(num) for num in row.split()] for row in number_rows])

    return [
        (number_matrix[:, col_idx].tolist(), Operation(operation_symbols[col_idx]))
        for col_idx in range(number_matrix.shape[1])
    ]


def parse_worksheet_vertically(
    worksheet_data: str,
) -> list[tuple[list[int], Operation]]:
    """Parse math worksheet reading problems vertically in columns.

    Numbers are written vertically in columns, with most significant digit at top.
    Problems are separated by columns of spaces.
    The bottom row contains the operation symbols.

    Args:
        worksheet_data: Raw worksheet text with numbers and operations

    Returns:
        List of problems, each as (numbers, operation) tuple
    """
    rows = worksheet_data.strip().splitlines()
    number_rows = rows[:-1]
    operation_symbols = rows[-1].split()

    problems = []
    current_problem = []

    # Read column by column (character by character within the same column position)
    for col_idx in range(len(number_rows[0])):
        # Extract the column by taking the character at col_idx from each row
        column_chars = "".join([
            number_rows[row_idx][col_idx] for row_idx in range(len(number_rows))
        ]).strip()

        if column_chars:
            # Column contains a number
            current_problem.append(int(column_chars))
        else:
            problems.append(current_problem)
            current_problem = []

    problems.append(current_problem)

    return list(zip(problems, operation_symbols))
