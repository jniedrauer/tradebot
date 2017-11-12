# vim: set noet
VENV=venv
PYTHON=python3
VENV=venv
PIP=$(VENV)/bin/pip

PKG=tradebot

help:
	@echo "Targets:"
	@echo "venv: Create virtualenv for development"
	@echo "test: Run unit tests"
	@echo "build: Compile package installers"

$(PIP):
	$(PYTHON) -m venv $(VENV)

venv: $(VENV)/bin/activate

$(VENV)/bin/activate: requirements.txt
	test -d $(VENV) || $(PYTHON) -m venv $(VENV)
	$(PIP) install -Ur requirements.txt

test:
	$(PYTHON) -m unittest discover -v --start-directory=tests/ --pattern=*_test.py

rpm:
	$(PYTHON) setup.py bdist_rpm

tgz:
	$(PYTHON) setup.py sdist

wheel:
	$(PYTHON) setup.py bdist_wheel

build: test tgz wheel rpm

.PHONY: help test rpm tgz wheel build
