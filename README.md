# Advent of Code 2025 Solutions

Python solutions to the [Advent of Code 2025 challenges](https://adventofcode.com/2025), organized as monorepo with individual packages for each day.

## Table of Contents
- [Advent of Code 2025 Solutions](#advent-of-code-2025-solutions)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Getting Started](#getting-started)
  - [Project Structure](#project-structure)
  - [Usage](#usage)
    - [Running Solutions](#running-solutions)
    - [Running Tests](#running-tests)
    - [Code Quality](#code-quality)
  - [Development](#development)
    - [Adding a New Day](#adding-a-new-day)
  - [License](#license)

## Introduction

This repository contains my solutions to Advent of Code 2025. The project uses:
- **[uv](https://docs.astral.sh/uv/)** for fast, reliable Python dependency management
- **pytest** for testing with example inputs
- **ruff** for linting and formatting
- **pre-commit** hooks for automated code quality checks

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gmurro/advent-of-code-2025.git
   cd advent-of-code-2025
   ```

2. **Install UV**:
   ```bash
   # macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

   See the [official guide](https://docs.astral.sh/uv/getting-started/installation/) for more options.

3. **Install dependencies:**
   ```bash
   uv sync --all-packages
   ```

4. **(Optional) Set up pre-commit hooks:**
   ```bash
   uv run pre-commit install
   ```

## Project Structure

```
advent-of-code-2025/
├── aoc/
│   └── day_XX/                    # Each day is a separate package
│       ├── pyproject.toml         # Package configuration
│       ├── README.md              # Puzzle description
│       ├── src/
│       │   └── day_XX/
│       │       ├── input.txt      # Puzzle input (shared by both puzzles)
│       │       ├── puzzle_1/
│       │       │   └── solver.py  # Puzzle 1 solution
│       │       └── puzzle_2/
│       │           └── solver.py  # Puzzle 2 solution
│       └── tests/
│           ├── conftest.py        # Shared test fixtures
│           ├── test_puzzle_1.py
│           └── test_puzzle_2.py
├── pyproject.toml                 # Workspace configuration
└── README.md
```

Each day is a standalone Python package within the UV workspace, with its own dependencies and configuration.

## Usage

### Running Solutions

Run a specific day's solution:

```bash
# Puzzle 1 of Day 1
uv run python aoc/day_01/src/day_01/puzzle_1/solver.py

# Puzzle 2 of Day 1
uv run python aoc/day_01/src/day_01/puzzle_2/solver.py
```

Or use the package module syntax:
```bash
uv run python -m day_01.puzzle_1.solver
uv run python -m day_01.puzzle_2.solver
```

### Running Tests

Run all tests for a specific day:
```bash
uv run pytest aoc/day_01/tests -vv
```

Run tests for a specific puzzle:
```bash
uv run pytest aoc/day_01/tests/test_puzzle_1.py -vv
```

Run a specific test:
```bash
uv run pytest aoc/day_01/tests/test_puzzle_2.py::test_puzzle_2_solve -vv
```

### Code Quality

The project uses Ruff for linting and formatting:

```bash
# Check code quality
cd aoc/day_01
uv run ruff check .

# Format code
cd aoc/day_01
uv run ruff format .

# Type checking with mypy
cd aoc/day_01
uv run mypy src
```

Pre-commit hooks automatically run these checks before commits if installed.

## Development

### Adding a New Day

Each day follows the same structure. To add a new day:

1. Create the day directory: `aoc/day_XX/`
2. Copy the structure from an existing day
3. Update `pyproject.toml` with the day number and description
4. Add your `input.txt` to `src/day_XX/`
5. Implement solutions in `puzzle_1/solver.py` and `puzzle_2/solver.py`
6. Add test fixtures and tests

The UV workspace automatically includes new packages under `aoc/*`.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
