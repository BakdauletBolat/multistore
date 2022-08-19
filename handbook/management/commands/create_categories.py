from django.core.management.base import BaseCommand, CommandError
from handbook.models.Category import Category
from multistore.request import Request
class Command(BaseCommand):
    help = 'Category create'

    request = Request()
    def handle(self, *args, **options):


        categoriesList = self.request.get('/api/v1/catalog/categories/list')

        categories = []

        for category in categoriesList:
            categories.append(
                Category(
                    id=category['id'],
                    name=category['attributes']['name'],
                    parent_id=category['attributes']['parent_id']
                )
            )

        Category.objects.bulk_create(categories)

        self.stdout.write(self.style.SUCCESS('Successfully imported categories'))