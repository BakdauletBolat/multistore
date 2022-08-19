from store.models.Store import Store
from django.core.management.base import BaseCommand, CommandError
from handbook.models.Category import Category
from multistore.request import Request
class Command(BaseCommand):
    help = 'Category create'

    request = Request()
    def handle(self, *args, **options):


        categoriesList = self.request.get('/api/v1/catalog/categories/list')

        def getFiltered(array,key,value):
            return [item for item in array if item['attributes'][key]==value]

        def getFilteredById(array,value):
            return [item for item in array if item['id']==value][0]

        filteredSamsungs = getFiltered(categoriesList,'name','Samsung')

        ids = set()

        def add_parent_ids(filteredSamsung):
                ids.add(filteredSamsung['id'])
                parentSamsung = getFilteredById(categoriesList,filteredSamsung['attributes'].get('parent_id',None))
                if parentSamsung['attributes']['parent_id'] == None:
                    ids.add(parentSamsung['id'])
                    return 1
                else:
                    ids.add(parentSamsung['id'])
                    return add_parent_ids(parentSamsung)
                
        for filteredSamsung in filteredSamsungs:
            add_parent_ids(filteredSamsung)

        categoriesBySamsung = Category.objects.filter(id__in=ids)

        try:
            store = Store.objects.get(id=1)
        except Exception:
            store = Store.objects.create(name='Samsung')

        for item in categoriesBySamsung:
            item.store_id = store.id
            item.save()


        self.stdout.write(self.style.SUCCESS('Successfully binded Samsung Store'))