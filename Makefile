install-requirements:
	pip3 install -r requirements.txt

run:
	python3 sgl/main.py

runserver:
	FLASK_APP=app.py python -m flask run -h 0.0.0.0 --debugger --reload
