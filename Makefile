.PHONY: dev prod build stop logs clean

dev:
	docker compose up docs-dev

prod:
	docker compose --profile production up docs-prod

build:
	docker compose build

stop:
	docker compose down

logs:
	docker compose logs -f

clean:
	docker compose down -v
	rm -rf dist node_modules
