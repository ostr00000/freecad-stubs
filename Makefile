PYTHON=python3.12
ENV_NAME=freecad_env
PYTHON_ENV=./$(ENV_NAME)/bin/python

.PHONY: setup_system setup_env install_in_env prepare_freecad clean_env prepare_build build_and_upload


setup_system:
	sudo -v -A
	#sudo apt update
	sudo apt -y install $(PYTHON) $(PYTHON)-dev $(PYTHON)-venv

setup_env:
	$(PYTHON) -m venv $(ENV_NAME)

install_in_env:
	$(PYTHON_ENV) -m pip install --upgrade pip
	$(PYTHON_ENV) -m pip install PyQt5
	$(PYTHON_ENV) -m pip install -e .[generate,check]

prepare_freecad:
	git -C FreeCAD pull || git clone https://github.com/FreeCAD/FreeCAD FreeCAD

clean_env:
	rm -r $(ENV_NAME)


prepare_build:
	$(PYTHON_ENV) -m pip install --upgrade pip
	$(PYTHON_ENV) -m pip install --upgrade build
	$(PYTHON_ENV) -m pip install --upgrade twine

build_and_upload:
	rm -rf ./dist
	$(PYTHON_ENV) -m build
	$(PYTHON_ENV) -m twine upload dist/*

check_by_mypy:
	$(PYTHON_ENV) -m mypy

check_by_pylint:
	$(PYTHON_ENV) -m pylint ./lib/
