install-requirements:
	pip3 install -r requirements.txt

run-591:
	python3 scripts/591/main.py

runserver:
	FLASK_APP=app.py python -m flask run -h 0.0.0.0 --debugger --reload
