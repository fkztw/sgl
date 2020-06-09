PROJECT=sgl

all: install

install:
	poetry install

run-cli:
	poetry run python scripts/591/main.py

run-server:
	FLASK_APP=app.py poetry run flask run -h "0.0.0.0" -p "8000" --debugger --reload
