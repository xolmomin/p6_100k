import csv

from django.core.management.base import BaseCommand

from apps.models import Region, District


class Command(BaseCommand):
    help = 'Creating region or district table'

    def add_arguments(self, parser):
        parser.add_argument('type', type=str, help='Choose region or district')

    def handle(self, *args, **options):
        choose = options.get('type')
        if choose == 'regions':
            with open('apps/fixtures/regions.csv', 'r') as f:
                f.readline()
                read = csv.reader(f)
                for row in read:
                    Region.objects.update_or_create(
                        id=row[0],
                        name=row[1]
                    )
        elif choose == 'districts':
            with open('apps/fixtures/districts.csv', 'r') as f:
                f.readline()
                read = csv.reader(f)
                for row in read:
                    District.objects.get_or_create(
                        id=row[0],
                        name=row[1],
                        region_id=row[2]
                    )