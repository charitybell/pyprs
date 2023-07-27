# PyPrS

`npm run`-style scripts, for `pyproject.toml`

## Usage

Add your scripts to your `pyproject.toml` file

```toml
[tool.pyprs.scripts]
flake8 = 'flake8 pyprs'
mypy = 'mypy --strict -p pyprs'
```

Then run them!

```
$ python -m pyprs mypy
Success: no issues found in 2 source files
```

List your scripts with the `--list` flag

```
$ python -m pyprs --list
flake8:	flake8 pyprs
mypy:	mypy --strict -p pyprs
```

## License

Pyprs is public domain software. To avoid confusion about the copyright status of this code, a
"license" is provided via the [Unlicense](https://unlicense.org). The unlicense
disclaims copyright interest in the software, and explicitly places it in the public domain.
