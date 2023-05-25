run: python-is-installed
	python main.py examples/tree1.txt examples/commands1.txt || python3 main.py examples/tree1.txt examples/commands1.txt

test: python-is-installed
	python -m unittest discover tests  || python3 -m unittest discover tests

python-is-installed: 
	test -e /bin/python
