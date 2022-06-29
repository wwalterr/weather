# docker build -t application . # image name and Dockerfile path

# docker run -it -d --name application -p 4000:4000 application # container name and image name

# docker tag application username/application # image name, username and tag - change username

# docker push username/application # username and tag - change username

FROM python:3-alpine

# Prevent Python from writing intermediate files
ENV PYTHONDONTWRITEBYTECODE 1

# Prevent Python from bufering into stdout and stderr
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --user -r requirements.txt

COPY . /code/

# Not necessary while using Docker Compose
# EXPOSE 4000

# CMD python -m uvicorn source.application:application --host 0.0.0.0 --port 4000 --workers 2