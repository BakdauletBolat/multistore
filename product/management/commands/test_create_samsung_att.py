from django.core.management.base import BaseCommand, CommandError
from multistore.request import Request
from beav.models.Attribute import Attribute
from beav.models.Group import Group
from beav.models.Value import Value
from beav.models.Entity import Entity
from django.db import transaction

from product.models.Product import Product
class Command(BaseCommand):
    help = 'Creating Products from IMS'

   
    def handle(self, *args, **options):
        
        with transaction.atomic():
            product_samsung = Product.objects.filter(store_id=1)

            attr = Attribute(name='Своиства')
            attr.save()

            group = Group.objects.create(name='Общая')
            valueAll = Value.objects.create(name='Я общая')

            for product in product_samsung:
                en = Entity.objects.create(group=group, product=product,attribute=attr)
                en.values.set([valueAll,Value.objects.create(name=f'личная{product.id}')])

            
            self.stdout.write(self.style.SUCCESS(f'Successfully created product'))