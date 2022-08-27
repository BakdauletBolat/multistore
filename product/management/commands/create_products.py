from django.core.management.base import BaseCommand, CommandError
from multistore.request import Request
from product.models.Product import Product
class Command(BaseCommand):
    help = 'Creating Products from IMS'

   
    def handle(self, *args, **options):
        request = Request()
        products = []
        for page in range(1,37): 
            try: 
                response = request.get(f'/api/v1/catalog/products?page={page}&per_page=1000') 
                for product in response['data']:
                    prObj = Product(
                        id=int(product['id']),
                        category_id=int(product['attributes']['category_id']),
                        full_name=product['attributes']['full_name'],
                        name=str(product['attributes']['name'])
                        )
                    products.append(prObj)

                print('Added Page =',page)
            except Exception as e:
                print(e)
                print('Exeption on page =',page)
        
        lengthProducts = len(products)
        
        Product.objects.bulk_create(products)
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created {lengthProducts} product'))