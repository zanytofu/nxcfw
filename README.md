# nxcfw

Custom firmware pack.

## Requirements

- Python 3.9 or higher
- uv (Python package manager)

## Setup

Create and activate virtual environment:
```bash
uv venv
source .venv/bin/activate  # with fish shell: .venv/bin/activate.fish
```

Install dependencies:
```bash
uv pip install -e .
```

## Version Management

This project uses `bump-my-version` for semantic versioning and git tagging.

### Bump version commands

**Patch version** (0.1.0 → 0.1.1):
```bash
bump-my-version patch
```

**Minor version** (0.1.0 → 0.2.0):
```bash
bump-my-version minor
```

**Major version** (0.1.0 → 1.0.0):
```bash
bump-my-version major
```

### What happens when you bump

Each command will automatically:
1. Update the version in `pyproject.toml`
2. Create a git commit
3. Create a git tag (e.g., `v0.1.1`)
4. Push the commit and tag to remote

## Development

1. Make your changes
2. Commit your changes: `git add . && git commit -m "Your changes"`
3. Bump version: `bump-my-version patch` (or `minor`/`major`)
4. Your version is now updated and tagged!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
