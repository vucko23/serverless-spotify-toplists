PY=python
PIP=pip

.PHONY: setup test lint local-run zip-lambda

setup:
	$(PIP) install -r requirements.txt -r requirements-dev.txt

test:
	pytest -q

lint:
	ruff check src tests

local-run:
	$(PY) scripts/local_run.py

zip-lambda:
	mkdir -p build
	cd src && zip -r ../build/lambda.zip .
	@echo "Created build/lambda.zip"
