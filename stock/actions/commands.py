from loguru import logger
from multistore.request import Request
from stock.models.Stock import Stock


request = Request()

class CreateStocksAction:
    def run(self):
        stocks = []
        for page in range(1,3): 
            response = request.get_stocks(page)
            try: 
               
                for stock in response['data']:
                    stObj = Stock(
                        quality_id=stock['quality_id'],
                        warehouse_id=stock['warehouse_id'],
                        product_id=stock['product_id'],
                        quantity=stock['quantity']
                        )
                    stocks.append(stObj)
                print('Added Page =',page)
            except Exception as e:
                print(e)
                print('Exeption on page =',page)
        
        lengthStocks = len(stocks)
        
        Stock.objects.bulk_create(stocks)
        logger.success(f'Successfully created {lengthStocks} stocks')