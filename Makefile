
test:
	coverage run --branch -m pytest -v test_ttt.py test_pytest.py
	coverage report --show-missing ttt.py
