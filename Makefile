all: test build

test:
	python -m pytest ./tests/unit_tests
	python -m pytest ./tests/e2e_tests/test.py

test_single:
	python -m pytest ./tests/e2e_tests/test.py -k test_single

cleanup:
	rm response/*

build:
	python -m build

coverage:
	 python -m pytest --cov=tests/unit_tests/ --cov-report=html


