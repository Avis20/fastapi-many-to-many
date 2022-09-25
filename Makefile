-include .env
export

.PHONY: up
up: ## Up all services locally with docker-compose
	touch .env
	docker-compose up

.PHONY: uninstall
uninstall:
	docker-compose down --remove-orphans --volumes

.PHONY: init_env
init_env:
	echo ${TEST}
