run: python-is-installed
	python main.py  || python3 main.py

test: python-is-installed
	python -m unittest discover tests  || python3 -m unittest discover tests

python-is-installed: 
	test -e /bin/python
