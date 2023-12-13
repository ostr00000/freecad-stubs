# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Changelog file.

### Changed

- Do not show default argument when argument is required by C API.
- Updated generator code for recent changes in FreeCAD src code.

### Deprecated

### Removed

### Fixed

- Issue #10: make `templates.py` easy copy-paste.
- Issue #8: use `qtpy` in `FreeCADTemplates` as optional dependency.

### Security

## [1.0.16] - 2023-11-24

### Changed

- Update stub to recent FreeCAD version (`main` from 2023-11-24).
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

- An install file uses `pyproject.toml`.
