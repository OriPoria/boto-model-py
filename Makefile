all: test build

test:
	python -m pytest ./tests

build:
	python -m build

