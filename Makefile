PYTHONPATH := .
VENV := venv
REQUIREMENTS := -r requirements.txt

BIN := $(VENV)/bin
PIP := $(BIN)/pip
PYTHON := $(BIN)/python
FLASK := $(BIN)/flask

bootstrap: venv \
	requirements

run:
	$(FLASK) run --no-reload

venv:
	python3 -m venv $(VENV)

requirements:
	$(PIP) install $(REQUIREMENTS)

clean:
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type d -name '*pytest_cache*' -exec rm -rf {} +

clean-all: clean
	@rm -r $(VENV)

