SERVER_ROOT := ./server/manage.py
VENV_ROOT := virtualenv
VENV_ACTIVATE := . $(VENV_ROOT)/bin/activate

compile:
	(\
		python -m venv $(VENV_ROOT) && \
		$(VENV_ACTIVATE) && \
		pip compile; \
	)

install:
	(\
		python -m venv $(VENV_ROOT) && \
		$(VENV_ACTIVATE) && \
		pip install -r requirements.txt; \
	)

migrate:
	(\
		$(VENV_ACTIVATE) && \
		python $(SERVER_ROOT) makemigrations && \
		python $(SERVER_ROOT) migrate; \
	)

server: 
	(\
		$(VENV_ACTIVATE) && \
		$(SERVER_ROOT) runserver; \
	)

setup: install migrate

run: install migrate server