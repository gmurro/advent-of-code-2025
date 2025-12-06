.PHONY: install
install: ## Install dependencies and pre-commit hooks
	@echo "📦 Installing dependencies..."
	uv sync --all-packages
	@echo "🪝 Installing pre-commit hooks..."
	uv run pre-commit install
	@echo "✅ Installation complete!"

.PHONY: sync
sync: ## Sync all workspace packages
	@echo "🔄 Syncing all workspace packages..."
	uv sync --all-packages
	@echo "✅ Sync complete!"

.PHONY: sync-day
sync-day: ## Sync specific day package
	@if [ -z "$(DAY)" ]; then \
		echo "❌ Error: DAY parameter is required"; \
		echo "Usage: make sync-day DAY=XX"; \
		exit 1; \
	fi
	@echo "🔄 Syncing day $(DAY) package..."
	uv sync --package day-$(DAY)
	@echo "✅ Day $(DAY) synced!"

.PHONY: check-all
check-all: ## Run ruff + mypy on all packages from root
	@echo "🔍 Running code quality checks on all packages..."
	@echo ""
	@echo "📋 Running ruff check..."
	uv run ruff check aoc
	@echo ""
	@echo "🔎 Running mypy..."
	uv run mypy aoc
	@echo ""
	@echo "✅ All checks passed!"

.PHONY: format-all
format-all: ## Format all packages with ruff
	@echo "✨ Formatting all packages..."
	uv run ruff format aoc
	@echo "✅ Formatting complete!"

.PHONY: test-all
test-all: ## Run pytest on all packages
	@echo "🧪 Running tests on all packages..."
	@for dir in aoc/day_*; do \
		if [ -d "$$dir" ]; then \
			day=$$(basename $$dir); \
			echo ""; \
			echo "Testing $$day..."; \
			uv run --package $$day pytest $$dir/tests; \
		fi; \
	done
	@echo "✅ All tests complete!"

.PHONY: check
check:	 ## Run ruff + mypy on specific day package
	@if [ -z "$(DAY)" ]; then \
		echo "❌ Error: DAY parameter is required"; \
		echo "Usage: make check DAY=XX"; \
		exit 1; \
	fi
	@if [ ! -d "aoc/day_$(DAY)" ]; then \
		echo "❌ Error: Directory aoc/day_$(DAY) does not exist"; \
		exit 1; \
	fi
	@echo "🔍 Running code quality checks on day $(DAY)..."
	@echo ""
	@echo "📋 Running ruff check..."
	uv run --package day-$(DAY) ruff check aoc/day_$(DAY)
	@echo ""
	@echo "🔎 Running mypy..."
	uv run --package day-$(DAY) mypy aoc/day_$(DAY)/src
	@echo ""
	@echo "✅ Day $(DAY) checks passed!"

.PHONY: format
format: ## Format specific day package with ruff
	@if [ -z "$(DAY)" ]; then \
		echo "❌ Error: DAY parameter is required"; \
		echo "Usage: make format DAY=XX"; \
		exit 1; \
	fi
	@if [ ! -d "aoc/day_$(DAY)" ]; then \
		echo "❌ Error: Directory aoc/day_$(DAY) does not exist"; \
		exit 1; \
	fi
	@echo "✨ Formatting day $(DAY)..."
	uv run --package day-$(DAY) ruff format aoc/day_$(DAY)
	@echo "✅ Day $(DAY) formatted!"

.PHONY: test
test: ## Run pytest on specific day package
	@if [ -z "$(DAY)" ]; then \
		echo "❌ Error: DAY parameter is required"; \
		echo "Usage: make test DAY=XX"; \
		exit 1; \
	fi
	@if [ ! -d "aoc/day_$(DAY)" ]; then \
		echo "❌ Error: Directory aoc/day_$(DAY) does not exist"; \
		exit 1; \
	fi
	@echo "🧪 Running tests for day $(DAY)..."
	uv run --package day-$(DAY) pytest aoc/day_$(DAY)/tests
	@echo "✅ Day $(DAY) tests complete!"

.PHONY: run
run: ## Run a specific puzzle (Usage: make run DAY=XX PUZZLE=Y)
	@if [ -z "$(DAY)" ]; then \
		echo "❌ Error: DAY parameter is required"; \
		echo "Usage: make run DAY=XX PUZZLE=Y"; \
		exit 1; \
	fi
	@if [ -z "$(PUZZLE)" ]; then \
		echo "❌ Error: PUZZLE parameter is required"; \
		echo "Usage: make run DAY=XX PUZZLE=Y"; \
		exit 1; \
	fi
	@if [ ! -d "aoc/day_$(DAY)" ]; then \
		echo "❌ Error: Directory aoc/day_$(DAY) does not exist"; \
		exit 1; \
	fi
	@if [ ! -f "aoc/day_$(DAY)/src/day_$(DAY)/puzzle_$(PUZZLE)/solver.py" ]; then \
		echo "❌ Error: Puzzle $(PUZZLE) solver not found for day $(DAY)"; \
		exit 1; \
	fi
	@echo "🎄 Running Day $(DAY) - Puzzle $(PUZZLE)..."
	@uv run python aoc/day_$(DAY)/src/day_$(DAY)/puzzle_$(PUZZLE)/solver.py

.PHONY: test-puzzle
test-puzzle: ## Run tests for a specific puzzle (Usage: make test-puzzle DAY=XX PUZZLE=Y)
	@if [ -z "$(DAY)" ]; then \
		echo "❌ Error: DAY parameter is required"; \
		echo "Usage: make test-puzzle DAY=XX PUZZLE=Y"; \
		exit 1; \
	fi
	@if [ -z "$(PUZZLE)" ]; then \
		echo "❌ Error: PUZZLE parameter is required"; \
		echo "Usage: make test-puzzle DAY=XX PUZZLE=Y"; \
		exit 1; \
	fi
	@if [ ! -d "aoc/day_$(DAY)" ]; then \
		echo "❌ Error: Directory aoc/day_$(DAY) does not exist"; \
		exit 1; \
	fi
	@if [ ! -f "aoc/day_$(DAY)/tests/test_day_$(DAY)_puzzle_$(PUZZLE).py" ]; then \
		echo "❌ Error: Test file for puzzle $(PUZZLE) not found for day $(DAY)"; \
		exit 1; \
	fi
	@echo "🧪 Running tests for Day $(DAY) - Puzzle $(PUZZLE)..."
	@uv run pytest aoc/day_$(DAY)/tests/test_day_$(DAY)_puzzle_$(PUZZLE).py -vv

# Version management
.PHONY: bump
bump: ## Bump version, update changelog, and create git tag (BUMP=PATCH|MINOR|MAJOR)
	@echo "🔨 Building release with commitizen..."
	@if [ -n "$(BUMP)" ]; then \
		echo "Bumping version: $(BUMP)"; \
		uv run cz bump --increment $(BUMP); \
	else \
		echo "Auto-detecting version bump from commits..."; \
		uv run cz bump; \
	fi
	@echo "✅ Build complete!"

.PHONY: bump-dry
bump-dry: ## Dry run of version bump (BUMP=PATCH|MINOR|MAJOR)
	@echo "🔍 Dry run of version bump..."
	@if [ -n "$(BUMP)" ]; then \
		echo "Bumping version: $(BUMP)"; \
		uv run cz bump --increment $(BUMP) --dry-run; \
	else \
		echo "Auto-detecting version bump from commits..."; \
		uv run cz bump --dry-run; \
	fi

# Cleanup
.PHONY: clean
clean: ## Remove cache files and build artifacts
	@echo "🧹 Cleaning up cache files and build artifacts..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "dist" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "build" -exec rm -rf {} + 2>/dev/null || true
	@echo "✅ Cleanup complete!"

.PHONY: help
help:
	@uv run python -c "import re; \
	[[print(f'\033[36m{m[0]:<20}\033[0m {m[1]}') for m in re.findall(r'^([a-zA-Z_-]+):.*?## (.*)$$', open(makefile).read(), re.M)] for makefile in ('$(MAKEFILE_LIST)').strip().split()]"

.DEFAULT_GOAL := help
