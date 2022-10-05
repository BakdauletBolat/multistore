from multistore.request import Request
from product.models.Product import ProductBase
from loguru import logger

request = Request()

class CreateProductsAction:


    def run(self):
        products = []
        for page in range(1,37): 
            try: 
                response = request.get_products(page=page)
                for product in response['data']:
                    prObj = ProductBase(
                        id=product['id'],
                        uid=product['attributes']['code'],
                        code=product['attributes']['code'],
                        status=product['attributes']['status'],
                        brand_id=product['attributes']['brand_id'],
                        category_id=product['attributes']['category_id'],
                        full_name=product['attributes']['full_name'],
                        name=str(product['attributes']['name'])
                        )
                    products.append(prObj)
                print('Added Page =',page)
            except Exception as e:
                print(e)
                print('Exeption on page =',page)
        
        lengthProducts = len(products)
        
        ProductBase.objects.bulk_create(products)
        
        logger.success(f'Successfully created {lengthProducts} product')