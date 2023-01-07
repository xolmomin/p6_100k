#username := admin
#email := admin@gmail.com
#password := 1

mig:
	python3 manage.py makemigrations
	python3 manage.py migrate
#user:
#	python3 manage.py createsuperuser --username=$(username) --email=$(email)
#	@echo -p $(password)
#	@echo $(password)