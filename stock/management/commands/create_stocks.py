from django.core.management.base import BaseCommand, CommandError
from multistore.request import Request
from stock.models.Stock import Stock
class Command(BaseCommand):
    help = 'Creating Products from IMS'

   
    def handle(self, *args, **options):
        request = Request()
        stocks = []
        for page in range(1,8): 
            try: 
                response = request.get(f'/api/v1/catalog/stock/list?warehouse_id=56&per_page=1000?page={page}') 
                for stock in response['data']:
                    stObj = Stock(
                        quality_id=stock['quality_id'],
                        wirehouse_id=stock['warehouse_id'],
                        product_id=stock['product_id'],
                        quantity=stock['quantity'],
                        )
                    stocks.append(stObj)

                print('Added Page =',page)
            except Exception as e:
                print(e)
                print('Exeption on page =',page)
        
        lengthStocks = len(stocks)
        
        Stock.objects.bulk_create(stocks)
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created {lengthStocks} stocks'))