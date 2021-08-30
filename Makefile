PYTHON=python3.10
ENV_NAME=freecad_env
PYTHON_ENV=./$(ENV_NAME)/bin/python

.PHONY: setup_system setup_env install_in_env clean_env


setup_system:
	sudo -v -A
	#sudo apt update
	sudo apt -y install $(PYTHON) $(PYTHON)-dev $(PYTHON)-venv

setup_env:
	$(PYTHON) -m venv $(ENV_NAME)

install_in_env:
	$(PYTHON_ENV) -m pip install --upgrade pip
	$(PYTHON_ENV) -m pip install PyQt5
	$(PYTHON_ENV) -m pip install -e .

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
