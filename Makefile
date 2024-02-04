PYTHON=python3.12
ENV_NAME=freecad_env
PYTHON_ENV=./$(ENV_NAME)/bin/python
export TERM=ansi

# ######## env ########
.PHONY: setup_system setup_env install_in_env install_pre_commit prepare_freecad clean_env

setup_system:
	sudo -v -A
	#sudo apt update
	sudo apt -y install $(PYTHON) $(PYTHON)-dev $(PYTHON)-venv

setup_env:
	$(PYTHON) -m venv $(ENV_NAME)

install_in_env:
	$(PYTHON_ENV) -m pip install --upgrade pip
	$(PYTHON_ENV) -m pip install PyQt5
	$(PYTHON_ENV) -m pip install pre-commit
	$(PYTHON_ENV) -m pip install --editable .[generate,check]

install_pre_commit:
	$(PYTHON_ENV) -m pre_commit install

prepare_freecad:
	git -C FreeCAD pull || git clone https://github.com/FreeCAD/FreeCAD FreeCAD

clean_env:
	rm -r $(ENV_NAME)


# ######## packaging ########
.PHONY: prepare_build build_and_upload

prepare_build:
	$(PYTHON_ENV) -m pip install --upgrade pip
	$(PYTHON_ENV) -m pip install --upgrade build
	$(PYTHON_ENV) -m pip install --upgrade twine

build_and_upload:
	rm -rf ./dist
	$(PYTHON_ENV) -m build
	$(PYTHON_ENV) -m twine upload dist/*


# ######## checks ########
.PHONY: pre_commit pre_commit_install pre_commit_uninstall pre_commit_auto_update

pre_commit:
	$(PYTHON_ENV) -m pre_commit run --all-files

pre_commit_install:
	$(PYTHON_ENV) -m pre_commit install

pre_commit_uninstall:
	$(PYTHON_ENV) -m pre_commit uninstall

pre_commit_auto_update:
	$(PYTHON_ENV) -m pre_commit autoupdate


# ######## checks ########
.PHONY: check_by_mypy check_by_pyright check_by_pylint

check_by_mypy:
	$(PYTHON_ENV) -m mypy

check_by_pyright:
	$(PYTHON_ENV) -m pyright

check_by_pylint:
	$(PYTHON_ENV) -m pylint ./lib/
