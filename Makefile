
test:
	#flake8 *.py
	coverage run --branch -m pytest -v test_uber.py test_ttt.py test_pytest.py test_game.py
	coverage report --show-missing ttt.py
