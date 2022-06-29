environment:
	python3 -m venv venv

install: 
	pip install -r requirements.txt

test:
	pytest --capture=no --disable-warnings

deploy:
	docker build -t application .

	docker tag application wwalterr/weather 

	docker login

	docker push wwalterr/weather

	kubectl apply -f k8s

	minikube service application --url

clean:
	kubectl delete -f k8s

start:
	uvicorn source.application:application --host=0.0.0.0 --port=4000 --workers 2 --reload

all: install test deploy

.PHONY: test