mig:
	python3 manage.py makemigrations
	python3 manage.py migrate
	@echo 'Migrate qilindi.'

dummy:
	python3 manage.py createdummydata -c 10 -s 5 -p 1000

load:
	python3 manage.py loaddata region
	python3 manage.py loaddata district
	@echo 'Regions and districts added'
