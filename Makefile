install:
	pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C,W1203,E1101 mlib cli utilscli

all: install format lint