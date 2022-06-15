environment:
	python3 -m venv venv

install: 
	pip install -r requirements.txt

test:
	pytest --capture=no --disable-warnings

deploy:
	.

start:
	uvicorn source.application:application --host=0.0.0.0 --port=4000 --workers 2 --reload --log-level error

all: install test deploy

.PHONY: test