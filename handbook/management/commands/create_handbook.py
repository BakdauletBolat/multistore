from django.core.management.base import BaseCommand
from handbook.actions.commands import CreateBrandsAction, CreateCategoriesAction, CreateCitiesAction, \
    CreateDeparmentsAction, CreateQualitiesAction, CreateStoresAction, CreateWareHouseAction


class Command(BaseCommand):
    help = 'Создание данных'

    def handle(self, *args, **options):
        CreateStoresAction().run()
        CreateCategoriesAction().run()
        CreateBrandsAction().run()
        CreateCitiesAction().run()
        CreateDeparmentsAction().run()
        CreateQualitiesAction().run()
        CreateWareHouseAction().run()
