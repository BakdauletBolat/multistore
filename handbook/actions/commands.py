from handbook.models.Category import Category
from handbook.models.City import City
from handbook.models.Department import Department
from handbook.models.WareHouse import WareHouse
from handbook.models.Quality import Quality
from handbook.models.Brand import Brand
from multistore.request import Request
from store.models.Store import Store

from loguru import logger
request = Request()


class CreateWareHouseAction:

    def run(self):
        list = request.get_warehouses()
        list_create = []
        for item in list['data']:
            list_create.append(
                WareHouse(
                    id=item['id'],
                    name=item['attributes']['name'],
                    uid=item['attributes']['uid'],
                    code=item['attributes']['code'],
                    status=item['attributes']['status'],
                    store_id=item['attributes']['store_id'],
                    city_id=item['attributes']['city_id']
                )
            )
        try:
            WareHouse.objects.bulk_create(list_create)
            logger.success('1. Successfully imported WareHouses')
        except Exception as e:
            WareHouse.objects.bulk_update(list_create, fields=['name'])
            logger.success('1. Successfully updated WareHouses')


class CreateCitiesAction:

    def run(self):
        list = request.get_cities()
        list_create = []
        for item in list['data']:
            list_create.append(
                City(
                    id=item['id'],
                    name=item['attributes']['name'],
                )
            )
        try:
            City.objects.bulk_create(list_create)
            logger.success('2. Successfully imported cities')
        except Exception as e:
            City.objects.bulk_update(list_create, fields=['name'])
            logger.success('2. Successfully updated cities')


class CreateQualitiesAction:

    def run(self):
        list = request.get_qualities()
        list_create = []
        for item in list:
            list_create.append(
                Quality(
                    id=item['id'],
                    name=item['attributes']['name'],
                    uid=item['attributes']['uid'],
                    code=item['attributes']['code'],
                    status=item['attributes']['status'],
                    alias=item['attributes']['alias'],
                    order=item['attributes']['order'],
                )
            )

        try:
            Quality.objects.bulk_create(list_create)
            logger.success('3. Successfully imported qualities')
        except Exception as e:
            Quality.objects.bulk_update(list_create, fields=['name'])
            logger.success('3. Successfully updated qualities')


class CreateCategoriesAction:

    def run(self):
        list = request.get_categories()

        list_create = []

        for item in list:

            try:
                Category.objects.get(id=item['id'])
            except Exception as e:
                list_create.append(
                    Category(
                        id=item['id'],
                        name=item['attributes']['name'],
                        uid=item['attributes']['uid'],
                        code=item['attributes']['code'],
                        status=item['attributes']['status'],
                        parent_id=item['attributes']['parent_id']
                    )
                )

        Category.objects.bulk_create(list_create)

        logger.success('Successfully imported categories')



class CreateDeparmentsAction:

    def run(self):
        list = request.get_deparment()

        list_create = []

        for item in list:

            try:
                Department.objects.get(id=item['id'])
            except Exception as e:
                list_create.append(
                    Department(
                        id=item['id'],
                        name=item['attributes']['name'],
                        uid=item['attributes']['uid'],
                        code=item['attributes']['code'],
                        status=item['attributes']['status'],
                        parent_id=item['attributes']['parent_id']
                    )
                )

        Department.objects.bulk_create(list_create)

        logger.success('Successfully imported deparment')




class CreateBrandsAction:

    def run(self):
        list = request.get_brands()
        list_create = []

        for item in list:
            
            try:
                Brand.objects.get(id=item['id'])
            except Exception as e:
                list_create.append(
                    Brand(
                        id=item['id'],
                        name=item['attributes']['name'],
                        uid=item['attributes']['uid'],
                        code=item['attributes']['code'],
                        status=item['attributes']['status']
                    )
                )


        Brand.objects.bulk_create(list_create)
        
        logger.success('Successfully imported brands')


class CreateStoresAction:

    def run(self):
        list = request.get_stores()
        list_create = []
        
        for item in list:
            try:
                Store.objects.get(id=item['id'])
            except Exception as e:
                list_create.append(
                    Store(
                        id=item['id'],
                        name=item['attributes']['name']
                    )
                )


        Store.objects.bulk_create(list_create)
        
        logger.success('Successfully imported stores')
