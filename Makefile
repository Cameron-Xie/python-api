# Docker Local Setup
up: create-dev-env
	@make start-containers

down:
	@make stop-containers

start-containers:
	@docker-compose up --build -d

stop-containers:
	@docker-compose down -v

create-dev-env:
	@test -e .env || cp .env.example .env

# Development
api-start:
	@poetry run uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload