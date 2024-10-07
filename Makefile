mig:
	python3 manage.py makemigrations
	python3 manage.py migrate
user:
	python3 manage.py createsuperuser --phone +998940021444
sort:
	black .
	isort .
