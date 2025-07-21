# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

### Changed

### Deprecated

### Removed

### Fixed

### Security

## [1.0.21] - 2025-07-22

## Changed

- Issue #44: `Proxy` property in `FreeCADTemplates` is typed as `typing.Any`,
  because in Python is not possible at the moment to write stubs for
  an optional Protocol.

# Fixed

- Issue #43: invalid return type for `getPropertyByName`/

## [1.0.20] - 2025-02-21

### Fixed

- Issue #37: Fix for `Part.makeLoft` to accept kwargs.

## [1.0.19] - 2025-02-19

### Fixed

- Issue #34: Updated old stub file for `Part.makeLoft`.

## [1.0.18] - 2025-01-07

### Added

- Support for detecting object namespace.
- (WIP) code generation based on clang parser.

### Fixed

- Issue #29: missing stubs for `FreeCAD.Units`.
- Issue #20: wrong return type for function with sibling namespace.

## [1.0.17] - 2024-02-05

### Added

- Changelog file.
- Python code to generate `.cpp` from `.xml`.
- Python code to replace macros in `.cpp`/`.h` files.

### Changed

- Do not show default argument when argument is required by C API.
- Updated generator code for recent changes in FreeCAD src code.
- Update stub to recent FreeCAD version (`main` from 2024-02-05
  `c57a83cb4f7f8bc8840ebbfc9aba97c15a502bd9`).

### Fixed

- Issue #10: make `templates.py` easy copy-paste.
- Issue #8: use `qtpy` in `FreeCADTemplates` as optional dependency.
- Fix submodules (add to public API, use module attributes):
  - Issue #14: add `FreeCADGui.PySideUic`,
  - Issue #17: move `ProgressIndicator` to `FreeCAD.Base`,
  - Issue #16: set `FreeCAD.Console` as attribute,

## [1.0.16] - 2023-11-24

### Changed

- Update stub to recent FreeCAD version (`main` from 2023-11-24
  `0179cd28ecd67a997e4df4162ca1fd77e3a672f2`).
- New Python 3.12 typing syntax in generator code.

### Fixed

- Errors reported by `pyright`.

## [1.0.15] - 2023-11-10

### Added

- `pre-commit` configuration.

### Fixed

- Errors reported by `ruff`, `mypy`, `pyright`.

## [1.0.14] - 2023-01-29

### Changed

- An installation process uses `pyproject.toml`.
