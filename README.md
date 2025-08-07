[![Release](https://github.com/zanytofu/nxcfw/actions/workflows/release.yaml/badge.svg)](https://github.com/zanytofu/nxcfw/actions/workflows/release.yaml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# nxcfw

Custom firmware pack for Nintendo Switch.

## Overview

This package includes a curated collection of custom firmware components:

TODO

## Installation

1. Download the latest release from the [releases page](https://github.com/zanytofu/nxcfw/releases)
2. Extract the nxcfw.zip file to the root of your SD card
3. Insert the SD card into your Nintendo Switch
4. Boot your console following standard CFW installation procedures

---

## Development

### Requirements

- Python 3.9 or higher
- uv (Python package manager)

### Setup

Create and activate virtual environment:
```bash
uv venv
source .venv/bin/activate  # with fish shell: .venv/bin/activate.fish
```

Install dependencies:
```bash
uv pip install -e .
```

### Version Management

This project uses `bump-my-version` for semantic versioning and git tagging.

**Bump version commands:**

```bash
bump-my-version bump patch   # 0.1.0 → 0.1.1
bump-my-version bump minor   # 0.1.0 → 0.2.0
bump-my-version bump major   # 0.1.0 → 1.0.0
```

**Dry run (preview changes):**
```bash
bump-my-version bump minor --dry-run --verbose
```

### Release Workflow

1. Make your changes and test thoroughly
2. Commit your changes: `git add . && git commit -m "feat: your changes"`
3. Bump version: `bump-my-version bump patch` (or `minor`/`major`)
4. Push the commit and tag to remote
5. GitHub Actions automatically creates a release with changelog and assets

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
