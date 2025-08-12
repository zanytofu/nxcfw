[![Release](https://github.com/zanytofu/nxcfw/actions/workflows/release.yaml/badge.svg)](https://github.com/zanytofu/nxcfw/actions/workflows/release.yaml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# nxcfw

Custom firmware pack for Nintendo Switch.

## Overview

This package includes a curated collection of custom firmware components:

- [Atmosphere](https://github.com/Atmosphere-NX/Atmosphere)
- [Hekate](https://github.com/CTCaer/hekate)
- [Sys-patch](https://github.com/impeeza/sys-patch)
- [OC-Switchcraft-EOS](https://github.com/halop/OC-Switchcraft-EOS)
- [Ultrahand-Overlay](https://github.com/ppkantorski/Ultrahand-Overlay)
- [Status-Monitor-Overlay](https://github.com/ppkantorski/Status-Monitor-Overlay)
- [Sys-clk-overlay](https://github.com/ppkantorski/sys-clk)
- [NX-ovlloader](https://github.com/ppkantorski/nx-ovlloader)
- [Sysmodules](https://github.com/ppkantorski/ovl-sysmodules)
- [SaltyNX](https://github.com/masagrator/SaltyNX)
- [FPSLocker](https://github.com/masagrator/FPSLocker)
- [NX-FanControl](https://github.com/Zathawo/NX-FanControl)
- [ReverseNX-RT](https://github.com/dominatorul/ReverseNX-RT)
- [AIO Switch Updater](https://github.com/HamletDuFromage/aio-switch-updater)
- [Lockpick RCM](https://github.com/s1204IT/Lockpick_RCM)
- [TegraExplorer](https://github.com/suchmememanyskill/TegraExplorer)

## Installation

1. Download the latest `nxcfw.zip` file from the [releases page](https://github.com/zanytofu/nxcfw/releases)
2. Prepare your SD card:
  - If you are using a new SD card, format it to **FAT32**
  - Delete all files and folders from your SD card except `Nintendo/` and `emuMMC/` (if present)
3. Extract the contents of `nxcfw.zip` to the root of your SD card
4. Insert the SD card into your Nintendo Switch
5. Boot your console following standard CFW installation procedures

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

### Update Checker

This script checks for newer package versions from `packages.yaml`.

1. **Configure GitHub Token (Optional):**

Create a `.env` file by copying `env.example` and add your GitHub personal access token. This is only required if you exceed the GitHub API rate limit for unauthenticated requests.

```bash
cp env.example .env
```

2. **Run the checker:**
```bash
python scripts/update_checker.py
```

The script will fetch the latest stable and pre-release versions from GitHub and display a summary of available updates.

## License

This package is a collection of third-party packages, each under its own license.
Please see the [LICENSE](LICENSE) file for details.

Any original code in this repository is licensed under the MIT License.
