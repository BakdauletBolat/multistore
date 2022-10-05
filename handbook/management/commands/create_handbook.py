from django.core.management.base import BaseCommand, CommandError
from handbook.actions.commands import CreateBrandsAction, CreateCategoriesAction, CreateCitiesAction, CreateDeparmentsAction, CreateQualitiesAction, CreateStoresAction, CreateWareHouseAction

from multistore.request import Request
class Command(BaseCommand):
    help = 'CreateSeed'
    request = Request()
    def handle(self, *args, **options):
        
        CreateStoresAction().run()
        CreateCategoriesAction().run()
        CreateBrandsAction().run()
        CreateCitiesAction().run()
        CreateDeparmentsAction().run()
        CreateQualitiesAction().run()
        CreateWareHouseAction().run()
        