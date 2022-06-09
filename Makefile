environment:
	python3 -m venv venv

activate:
	source venv/bin/activate

install: 
	pip install -r requirements.txt

format:
	.

lint:
	.

test:
	.

deploy:
	.

start:
	uvicorn source.application:application --host=0.0.0.0 --port=4000 --workers 2 --reload --log-level error

all: install format lint test deploy