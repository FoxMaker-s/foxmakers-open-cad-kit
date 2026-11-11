# Contributing to foxmakers-open-cad-kit

Thank you for your interest in contributing! 🦊

## Ways to contribute

- 🐛 **Bug reports** — open an issue with the STL file that caused the error
- 💡 **Feature requests** — open an issue describing the desired behavior
- 📐 **New STL models** — submit a PR with a new 2-manifold STL + OpenSCAD source
- 🔧 **Code improvements** — fork, improve, submit a PR
- 📚 **Documentation** — improve README, add docstrings, translate

## Development Setup

```bash
git clone https://github.com/FoxMaker-s/foxmakers-open-cad-kit
cd foxmakers-open-cad-kit
python -m venv venv && source venv/bin/activate
pip install -e ".[dev]"
```

## Submitting a PR

1. Fork the repo
2. Create a branch: `git checkout -b feat/my-feature`
3. Test your changes: `python -m pytest tests/`
4. Submit a PR with a clear description

## Code Style

- Python: Black formatter (`black .`)
- Docstrings: Google style
- Commits: Conventional Commits (`feat:`, `fix:`, `docs:`)

## STL Model Requirements

New models must:
- Be 2-manifold (watertight)
- Pass `foxcad_manifold_utils.check_manifold()` without errors
- Include OpenSCAD source in `models/sources/`
- Be licensed MIT or CC0

## License

By contributing you agree your contributions will be licensed under MIT.

---

Questions? Open an issue or email [info@foxmakers.it](mailto:info@foxmakers.it)  
Free STL tools at [hub.foxmakers.it](https://hub.foxmakers.it/en/tools)