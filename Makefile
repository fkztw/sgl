PROJECT=sgl
PYTHON_VERSION=3.7.0

all: install

install:
	env PIPENV_VENV_IN_PROJECT=true pipenv --python $(PYTHON_VERSION)
	pipenv install

run-cli:
	pipenv run python scripts/591/main.py

run-server:
	FLASK_APP=app.py pipenv run flask run -h "0.0.0.0" -p "8000" --debugger --reload
