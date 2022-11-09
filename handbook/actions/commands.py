from multistore.request import ImsServiceRequest
from handbook.models import Category, City, Department, WareHouse, Quality, Brand, Language
from product.models import PriceType
from store.models import Store
from loguru import logger

request = ImsServiceRequest()


class CreateLanguageAction:

    @staticmethod
    def run():
        items = [{
            'id': 1,
            'name': 'Русский'
        },
            {
                'id': 2,
                'name': 'Английский'
            }
            , {
                'id': 3,
                'name': 'Казахский'
            }]
        list_create = []
        for item in items:
            list_create.append(
                Language(
                    id=item['id'],
                    name=item['name']
                )
            )

        Language.objects.bulk_create(list_create,
                                      update_conflicts=True,
                                      unique_fields=['id'],
                                      update_fields=['name'])

        logger.success(f'Успешно импортировано {len(list_create)}')





class CreateWareHouseAction:

    @staticmethod
    def run():
        items = request.get_warehouses()
        list_create = []
        for item in items['data']:
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

        WareHouse.objects.bulk_create(list_create,
                                      update_conflicts=True,
                                      unique_fields=['id'],
                                      update_fields=['name', 'uid', 'code', 'status', 'store_id', 'city_id'])
        logger.success(f'Успешно импортировано {len(list_create)} складов')


class CreateCitiesAction:

    @staticmethod
    def run():
        items = request.get_cities()
        list_create = []
        for item in items['data']:
            list_create.append(
                City(
                    id=item['id'],
                    uid=item['attributes']['uid'],
                    name=item['attributes']['name'],
                )
            )

        list_create.append(
            City(
                id=1000,
                uid='hello',
                name='По умолчанию'
            )
        )

        City.objects.bulk_create(list_create,
                                 update_conflicts=True,
                                 unique_fields=['id'],
                                 update_fields=['name', 'uid'])

        logger.success(f'Успешно импортировано {len(list_create)} городов')


class CreateQualitiesAction:

    @staticmethod
    def run():
        items = request.get_qualities()
        list_create = []
        for item in items:
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

        Quality.objects.bulk_create(list_create,
                                    update_conflicts=True,
                                    unique_fields=['id'],
                                    update_fields=['name', 'uid', 'code', 'status', 'alias', 'order'])

        logger.success(f'Успешно импортировано {len(list_create)} качествы')




class CreatePriceTypeAction:

    @staticmethod
    def run():
        items = request.get_price_types()
        list_create = []
        for item in items:
            list_create.append(
                PriceType(
                    id=item['id'],
                    name=item['attributes']['name'],
                    uid=item['attributes']['uid'],
                    code=item['attributes']['code'],
                    status=item['attributes']['status']
                )
            )

        PriceType.objects.bulk_create(list_create,
                                    update_conflicts=True,
                                    unique_fields=['id'],
                                    update_fields=['name', 'uid', 'code', 'status'])

        logger.success(f'Успешно импортировано {len(list_create)} качествы')


class CreateCategoriesAction:

    @staticmethod
    def run():
        items = request.get_categories()
        list_create = []
        for item in items:
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

        Category.objects.bulk_create(list_create,
                                     update_conflicts=True,
                                     unique_fields=['id'],
                                     update_fields=['name', 'uid', 'code', 'status', 'parent_id'])

        logger.success(f'Успешно импортировано {len(list_create)} категорий')


class CreateDeparmentsAction:

    @staticmethod
    def run():
        items = request.get_deparment()
        list_create = []

        for item in items:
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

        Department.objects.bulk_create(list_create,
                                       update_conflicts=True,
                                       unique_fields=['id'],
                                       update_fields=['name', 'uid', 'code', 'status', 'parent_id'])

        logger.success(f'Успешно импортировано {len(list_create)} под разделений')


class CreateBrandsAction:

    @staticmethod
    def run():
        items = request.get_brands()
        list_create = []

        for item in items:
            list_create.append(
                Brand(
                    id=item['id'],
                    name=item['attributes']['name'],
                    uid=item['attributes']['uid'],
                    code=item['attributes']['code'],
                    status=item['attributes']['status']
                )
            )

        Brand.objects.bulk_create(list_create,
                                  update_conflicts=True,
                                  unique_fields=['id'],
                                  update_fields=['name', 'uid', 'code', 'status'])

        logger.success(f'Успешно импортировано {len(list_create)} брендов')


class CreateStoresAction:

    @staticmethod
    def run():
        items = request.get_stores()
        list_create = []

        for item in items:
            list_create.append(
                Store(
                    id=item['id'],
                    name=item['attributes']['name']
                )
            )

        Store.objects.bulk_create(list_create,
                                  update_conflicts=True,
                                  unique_fields=['id'],
                                  update_fields=['name'])

        logger.success(f'Успешно импортировано {len(list_create)} магазинов')
