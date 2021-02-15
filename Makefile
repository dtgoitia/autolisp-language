requirements.txt:
	pip-compile --no-header --no-emit-index-url --verbose requirements.in --output-file requirements.txt

install:
	pip install -r requirements.txt

lint:
	flake8
	black --check --diff .
	isort --check --diff .
	python -m mypy --config-file setup.cfg --pretty .

test:
	pytest tests -vv

type-check:
	python -m mypy --config-file setup.cfg --pretty .

coverage:
	pytest tests --cov=gpy --cov-report=html
	python -m webbrowser -t file://$(realpath htmlcov/index.html)

.PHONY: install lint test coverage
