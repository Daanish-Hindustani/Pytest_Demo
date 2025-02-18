.PHONY: run lint format check commit

# Run the app after formatting and linting
run: check
	uvicorn main:app --reload

# Run both black and flake8 when "make" is called
all: check

# Run flake8 for linting
lint:
	flake8 .

# Run black for formatting
format:
	black .

# Run both format and lint checks
check: format lint


