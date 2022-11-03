from loguru import logger
from multistore.request import ImsServiceRequest
from stock.models import Stock

request = ImsServiceRequest()


class CreateStocksAction:

    @staticmethod
    def run():
        stocks = []
        for page in range(1, 3):
            response = request.get_stocks(page)
            try:

                for stock in response['data']:
                    stock_obj = Stock(
                        quality_id=stock['quality_id'],
                        warehouse_id=stock['warehouse_id'],
                        product_id=stock['product_id'],
                        quantity=stock['quantity']
                    )
                    stocks.append(stock_obj)
                logger.success(f'added {page} - page')
            except Exception as e:
                logger.exception(e)

        length_stocks = len(stocks)

        Stock.objects.bulk_create(stocks)
        logger.success(f'Успешно импортировано {length_stocks} складов')
