import csv
import os

import yaml
from django.apps import apps
from django.core.management.base import BaseCommand, CommandError

from apps.models import District


class Command(BaseCommand):
    help = 'This command will read data from csv file and write to database'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_name = District

    def get_current_app_path(self):
        return apps.get_app_config('apps').path

    def get_csv_file(self, filename):
        app_path = self.get_current_app_path()
        file_path = os.path.join(app_path, "management",
                                 "commands", filename)
        return file_path

    def clear_model(self):
        try:
            self.model_name.objects.all().delete()
        except Exception as e:
            raise CommandError(
                f'Error in clearing {self.model_name}: {str(e)}'
            )

    def insert_currency_to_db(self, data):
        try:
            self.model_name.objects.create(
                name=data["name"]
            )
        except Exception as e:
            raise CommandError(
                f'Error in inserting {self.model_name}: {str(e)}'
            )

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS(f'filename:district.yml'))
        file_path = self.get_csv_file('district.yml')
        line_count = 0
        try:
            with open(file_path) as file:
                data = yaml.load(file, Loader=yaml.FullLoader)
                self.clear_model()
                for _, row in data.items():
                    for i in row:
                        i = i.split(',')
                        _, created = District.objects.get_or_create(
                            id = i[0],
                            name=i[1],
                            region_id=i[2]
                        )
                        line_count += 1
            self.stdout.write(
                self.style.SUCCESS(
                    f'{line_count} entries added to Currencies'
                )
            )
        except FileNotFoundError:
            raise CommandError(f'File {file_path} does not exist')
