from django.core.management import BaseCommand
from faker import Faker

from apps.models import Product, Store, Category

fake = Faker()


class Command(BaseCommand):
    help = '''
        You can create dummy data. Like this:
    * Products      -> 1000
    * Categories    -> 15
    * Store          -> 20
    '''

    def handle(self, *args, **options):

        # Create 10 dummy data Category

        title = set(' '.join(fake.unique.text().split()[:3]) for i in range(15))
        for i in title:
            catagory = Category.objects.create(title=i, image=fake.image_url())
            catagory.save()
            print(i, 'added')

        # Create 20 dummy data Store

        name = set(fake.unique.company() for i in range(20))
        for i in name:
            store = Store.objects.create(image=fake.image_url(), name=i, short_des=''.join(i.split()[:2]))
            print(i, 'added')

        # Create 1000 dummy data Product

        for i in range(100):
            title = ' '.join(fake.text().split()[:3])
            main_picture = fake.image_url()
            price = abs(int(fake.longitude()))*1000
            created_at = fake.date_time()
            bonus = price // 100
            free_delivery = fake.boolean()
            reserve = abs(int(fake.longitude()))
            store = 1
            category = 1
            product = Product.objects.create(title=title, main_picture=main_picture, price=price, created_at=created_at,
                                             bonus=bonus, free_delivery=free_delivery, reserve=reserve, store_id=store, category_id=category)
            print(product.title, 'added')