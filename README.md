# PR Kitchen

## Setup

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- For local development: Python 3.14 and [pipenv](https://pipenv.pypa.io/)

### Configure

```bash
cp env.example .env
```

### Run with Docker

```bash
docker compose up --build
```

The web app runs at <http://localhost:5000>.

### Run locally

```bash
docker run --name mongodb -d -p 27017:27017 mongo

cd machine-learning-client
pipenv install --dev
pipenv run python -m ml_client.app

# in another terminal
cd web-app
pipenv install --dev
pipenv run flask --app app run --port 5000
```
