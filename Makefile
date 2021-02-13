all: format lint build test

build:
	npm run build

format:
	black ./src ./tests

lint:
	npx eslint .
	pylint --rcfile=setup.cfg ./src/* ./tests/*
	mypy ./src ./tests

test:
	coverage run -m pytest -v -s
	coverage report --fail-under=100 --show-missing
