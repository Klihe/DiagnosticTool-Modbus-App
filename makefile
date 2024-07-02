UNAME_S := $(shell uname -s)
PYTHON := python3

ifeq ($(UNAME_S), Linux)
    OS := Linux
    VENV := .venv
endif

ifeq ($(UNAME_S), Darwin)
    OS := MacOS
    VENV := .venv
endif

ifeq ($(UNAME_S), Windows_NT)
    OS := Windows
    PYTHON := py -3
    VENV := .venv
endif

all: install

venv:
	@echo "Creating virtual environment for $(OS)..."
	$(PYTHON) -m venv $(VENV)
	@echo "Virtual environment created."

install: venv
	@echo "Installing requirements..."
	$(VENV)/bin/pip3 install -r requirements.txt
	@echo "Requirements installed."

run:
	@echo "Running the application..."
	$(VENV)/bin/python3 src/run.py
	@echo "Application running."

clean:
	@echo "Cleaning up..."
	rm -rf $(VENV)
	@echo "Cleaned up."

.PHONY: all venv install run clean