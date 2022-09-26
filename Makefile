-include .env
export

.PHONY: up
up:
	touch .env
	docker-compose up

.PHONY: uninstall
uninstall:
	docker-compose down --remove-orphans --volumes

PGPASSWORD=fa_mtm_pass

.PHONY: recreate_db
recreate_db:
	echo ${PGPASSWORD}
	-psql -h 192.168.31.201 -U fa_mtm_user -d postgres -c 'DROP DATABASE "fa_mtm_db_name" WITH (FORCE);'
	psql -h 192.168.31.201 -U fa_mtm_user -d postgres -c 'CREATE DATABASE "fa_mtm_db_name"';

.PHONY: init_env
init_env:
	echo ${TEST}
