PYTHON=python3.12
ENV_NAME=freecad_env
PYTHON_ENV=./$(ENV_NAME)/bin/python
export TERM=ansi

makefile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
repo_dir := $(dir $(makefile_path))

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
.PHONY: release_changelog prepare_build build_and_upload

prepare_build:
	$(PYTHON_ENV) -m pip install --upgrade pip
	$(PYTHON_ENV) -m pip install --upgrade build
	$(PYTHON_ENV) -m pip install --upgrade twine
	# use `--pre` because on pypi there are old versions
	$(PYTHON_ENV) -m pip install --upgrade keepachangelog --pre

release_changelog:
	# replace autoformat escaping, because it is not possible to configure it
	# https://github.com/executablebooks/mdformat/issues/112
	# Replace: `\[text\]` -> `[text]`
	sed --in-place --expression 's@\\\[@[@g' --expression 's@\\\]@]@g' CHANGELOG.md
	$(PYTHON_ENV) -m keepachangelog release '1.0.18'

build_and_upload:
	rm -rf ./dist
	$(PYTHON_ENV) -m build
	$(PYTHON_ENV) -m twine upload dist/*


# ######## pre-commit ########
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


# ######## docker ########
docker_image_build:
	docker build --tag "freecad_build_image" .

docker_freecad_build:
	docker run \
		--name "freecad_build_container" \
		--rm \
		--interactive \
		--tty \
		--user "$(shell id -u):$(shell id -g)" \
		--volume="/etc/group:/etc/group:ro" \
    	--volume="/etc/passwd:/etc/passwd:ro" \
    	--volume="/etc/shadow:/etc/shadow:ro" \
		--volume "${repo_dir}/FreeCAD:/build/FreeCAD" \
		--volume "${repo_dir}/lib/cpp_ast:/build/cpp_ast" \
		--workdir '/build/FreeCAD' \
		"freecad_build_image" \
		bash \
		# . ../env/bin/activate \
		# mkdir --parents build_clang && cd build_clang && cmake ../ && cmake --build . -j$$(nproc --ignore=2) \
		# python3 ../../cpp_ast/macro/run_makefile_for_intermediate.py --repo-path .
		# clang -Xclang -ast-dump -fsyntax-only /build/FreeCAD/build_clang/src/App/CMakeFiles/FreeCADApp.dir/Origin.cpp.i > /build/FreeCAD/build_clang/src/App/CMakeFiles/FreeCADApp.dir/Origin.cpp.i.ast
