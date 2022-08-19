from django.core.management.base import BaseCommand, CommandError
from handbook.models.WireHouse import WireHouse
from handbook.models.City import City
from handbook.models.Quality import Quality
from multistore.request import Request
class Command(BaseCommand):
    help = 'WireHouse create'

    request = Request()
    def handle(self, *args, **options):


        wirehouseList = self.request.get('/api/v1/handbook/warehouses')
        cityList = self.request.get('/api/v1/handbook/cities')
        qualityList = self.request.get('/api/v1/catalog/products/qualities')

        wirehouses = []
        cities = []
        qualities = []



        for item in wirehouseList['data']:
            wirehouses.append(
                WireHouse(
                    id=item['id'],
                    name=item['attributes']['name'],
                )
            )
        
        try:
            WireHouse.objects.bulk_create(wirehouses)
            self.stdout.write(self.style.SUCCESS('1. Successfully imported wirehouses'))
        except Exception as e:
            WireHouse.objects.bulk_update(wirehouses,fields=['name'])
            self.stdout.write(self.style.SUCCESS('1. Successfully updated wirehouses'))

        for item in cityList['data']:
            cities.append(
                City(
                    id=item['id'],
                    name=item['attributes']['name'],
                )
            )

        try:
            City.objects.bulk_create(cities)
            self.stdout.write(self.style.SUCCESS('2. Successfully imported cities'))
        except Exception as e:
        
            City.objects.bulk_update(cities,fields=['name'])
            self.stdout.write(self.style.SUCCESS('2. Successfully updated cities'))

        for item in qualityList:
            qualities.append(
                Quality(
                    id=item['id'],
                    name=item['attributes']['name'],
                )
            )
        
        try:
            Quality.objects.bulk_create(qualities)
            self.stdout.write(self.style.SUCCESS('3. Successfully imported qualities'))
        except Exception as e:
        
            Quality.objects.bulk_update(qualities,fields=['name'])    
            self.stdout.write(self.style.SUCCESS('3. Successfully updated qualities'))