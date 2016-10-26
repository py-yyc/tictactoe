
test:
	coverage run --branch -m pytest -v test_ttt.py
	coverage report --show-missing ttt.py
