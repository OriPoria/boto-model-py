all: test build

test:
	python -m pytest ./tests/unit_tests
	python -m pytest ./tests/e2e_tests/test.py

test_single:
	python -m pytest ./tests/e2e_tests/test.py -k test_single

cleanup:
	rm response/*
	rm dist/*
	rm -rf ./src/boto_model_py.egg-info

build:
	python -m build

release_test:
	python3 -m twine upload --repository testpypi dist/*

release_prod:
	python3 -m twine upload --repository pypi dist/*

coverage:
	 python -m pytest tests/unit_tests --cov=src/ --cov-report=html
