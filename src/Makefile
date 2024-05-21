style:
	isort **/*.py --profile black
	black .

run:
	uvicorn main:app --reload --host 0.0.0.0 --port 8000