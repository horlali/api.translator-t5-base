# FastAPI application for T5-Base Model

## Toolchain

* [poetry](https://python-poetry.org/) for dependency management
* [black](https://github.com/psf/black) for code styling
* [isort](https://pycqa.github.io/isort/) for import sorting styling
* [flake8](https://flake8.pycqa.org/en/latest/) for linting

In the `scripts/` folder there are 3 scripts that can be used to check and correct any
problems. The scripts will only check by default, if you would
like to correct the errors you need to pass the `--fix` option. If you are using `zsh`
and got some errors, consider execution via `bash`

## Running tests

```bash
./scripts/run-tests.sh
```

## Running linters

```bash
./scripts/black-check.sh # add --fix flag to fix black linting issues
./scripts/flake8-check.sh
./scripts/isort-check.sh
```

## Running all linters in one line

```bash
./scripts/all-checks.sh
```
