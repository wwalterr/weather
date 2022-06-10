# Zapata

Weather API

## Built with

- [Python](https://www.python.org/)
- [Fast API](https://fastapi.tiangolo.com/)

## Installation

> Skip all the installation using Docker and Docker Compose `docker-compose up --build -d` or `make all` which installs everything locally, i.e in the actual host

Use the package manager APT to install the general dependencies.

```sh
apt install python3 python3-dev python3-pip python3-venv
```

Create a virtual environment.

```sh
make environment
```

Activate the virtual environment.

```sh
sudo make activate
```

Install the dependencies in the virtual environment.

```sh
make install
```

## Usage

Start a server.

```sh
make start
```

Open the API at [localhost:4000/docs](http://localhost:4000/docs) and choose one code from this [list](https://tgftp.nws.noaa.gov/data/observations/metar/decoded) to use the API.

## Test

Run the test suite.

```sh
make test
```

## Contributing

Please, consider the following.

1. Make sure you code have quality, a.k.a standards
2. Make sure your code is secure
3. Make sure your code has no performance issues
4. Make sure your code is documented, if necessary
5. Describe the changes that were done

> No issue or PR template required, but be informative

## License

This project is not licensed under any license.
