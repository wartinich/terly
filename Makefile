server:
	uvicorn src.main:app --reload

create-db:
	python -m scripts.database

install-dev-deps:
	pip install -r requirements/dev.txt

install-prod-deps:
	pip install -r requirements/prod.txt

lint:
	flake8 .
