from multistore.request import ImsServiceRequest
from product.models import Price, ProductBase
from loguru import logger
from django.db import connection
from celery import shared_task

request = ImsServiceRequest()


class CreatePricesAction:

    @staticmethod
    def run():
        prices = []
        for page in range(1, 57):
            try:
                response = request.get_prices(page)
                for product in response['data']:
                    pr_obj = Price(
                        product_id=int(product['product_id']),
                        price_type_id=int(product['price_type_id']),
                        quality_id=int(product['quality_id']),
                        updated_at=product['updated_at'],
                        cost=str(product['cost']),
                    )
                    prices.append(pr_obj)
                logger.success(f'added {page} - page')
            except Exception as e:
                logger.exception(e)

        length_prices = len(prices)

        with connection.constraint_checks_disabled():
            Price.objects.bulk_create(prices,
                                      update_conflicts=True,
                                      update_fields=['product_id', 'price_type_id', 'quality_id', 'cost'],
                                      unique_fields=['id'])

        logger.success(f'Успешно импортированы {length_prices} цен')


class CreateProductsAction:
    import_entity = 'Product'

    @staticmethod
    def run():
        products = []
        for page in range(1, 37):
            try:
                response = request.get_products(page=page)
                for product in response['data']:
                    product_obj = ProductBase(
                        id=product['id'],
                        uid=product['attributes']['uid'],
                        code=product['attributes']['code'],
                        status=product['attributes']['status'],
                        brand_id=product['attributes']['brand_id'],
                        category_id=product['attributes']['category_id'],
                        full_name=product['attributes']['full_name'],
                        name=str(product['attributes']['name'])
                    )
                    products.append(product_obj)
                logger.success(f'added {page} - page')
            except Exception as e:
                logger.exception(e)
                logger.info(f'exception at {page}')

        length_products = len(products)

        ProductBase.objects.bulk_create(products, update_fields=['uid', 'code', 'status', 'brand_id', 'category_id',
                                                                 'full_name', 'name'], unique_fields=['id'],
                                        update_conflicts=True)

        logger.success(f'Успешно импортировано {length_products} продуктов')
