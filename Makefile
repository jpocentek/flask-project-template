all: format lint test

format:
	black ./src ./tests

lint:
	pylint --rcfile=setup.cfg ./src/* ./tests/*
	mypy ./src ./tests

test:
	coverage run -m pytest -v -s
	coverage report --fail-under=100 --show-missing
