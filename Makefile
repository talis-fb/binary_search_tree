run:
	test -e /bin/pyton && python main.py  || python3 main.py

test: 
	test -e /bin/pyton && python -m unittest discover tests  || python3 -m unittest discover tests
