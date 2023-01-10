mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

user:
	python3 manage.py shell -c "from apps.models import User; User.objects.create_superuser('admin1', '1')"

#username := admin1
#email := admin@gmail.com
#password := 1
#
#user:
#	python3 manage.py createsuperuser --username=$(username) --email=$(email)
#	@echo -p $(password)
#	@echo $(password)