.PHONY: help build up down restart logs shell \
        revision migrate downgrade history current \
        test lint format

help:
	@echo "Commandes disponibles :"
	@echo " make build"
	@echo " make up"
	@echo " make down"
	@echo " make restart"
	@echo " make logs"
	@echo " make shell"
	@echo " make revision MESSAGE='...' "
	@echo " make migrate"
	@echo " make downgrade"
	@echo " make history"
	@echo " make current"



build:
	docker compose build

up:
	docker compose up --build -d

down:
	docker compose down

restart:
	docker compose down
	docker compose up --build -d

logs:
	docker compose logs -f api

shell:
	docker compose exec api bash

revision:
	docker compose exec api alembic revision --autogenerate -m "$(MESSAGE)"

migrate:
	docker compose exec api alembic upgrade head

downgrade:
	docker compose exec api alembic downgrade -1

history:
	docker compose exec api alembic history

current:
	docker compose exec api alembic current