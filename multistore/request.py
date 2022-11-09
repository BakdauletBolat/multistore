import requests
import os
import json


class Request:
    url = ''


    @staticmethod
    def get_token():
        response = requests.post('http://10.10.1.65:8090/api/services/login', data={
            'login': 'datastorage.service',
            'password': 'Zz123456'
        })
        return response.json().get('access_token', None)

    def get(self, url):
        response = requests.get(f'{self.url}{url}', headers={
            'Authorization': 'Bearer ' + self.get_token()
        })

        return response.json()

    def post(self, url, body):
        response = requests.post(f'{self.url}{url}', data=body, headers={
            'Authorization': 'Bearer ' + self.get_token()
        })

        return response.json()


class SaleServiceRequest(Request):
    url = os.environ.get('SALE_URL')

    def find_sales(self, body):
        """Функция для получение доступных акций"""

        payload = json.dumps(body)
        response = self.post('/sale/find/', payload)

        return response.json()


class SmsServiceRequest(Request):
    url = os.environ.get('SMSSERVICE_URL', None)

    def get_token(self):
        return os.environ.get('SMSSERVICE_TOKEN', None)

    def send_sms(self, phone, text):
        return self.post('/send-sms', {
            "phone": phone,
            "text": text,
            "source": "1C",
            "account": "INFOBIP_SONY"
        })


class ImsServiceRequest(Request):
    url = os.environ.get('IMS_URL', None)

    def get_prices(self, page):
        return self.get(f'/pricing/price?page={page}&per_page=1000')

    def get_products(self, page):
        return self.get(
            f'/catalog/products?page={page}&per_page=1000')

    def get_stocks(self, page):
        response = self.get(f'/catalog/stock/list?warehouse_id=1&per_page=1000?page={page}')
        return response

    def get_brands(self):
        return self.get('/catalog/products/brands')

    def get_categories(self):
        return self.get('/catalog/categories/list')

    def get_cities(self):
        return self.get('/base/cities')

    def get_deparment(self):
        return self.get('/base/departments')

    def get_qualities(self):
        return self.get('/catalog/products/qualities')

    def get_stores(self):
        return self.get('/base/stores')

    def get_warehouses(self):
        return self.get('/base/warehouses')


class StockServiceRequest(Request):
    url = os.environ.get('STOCK_IMS_URL', None)

    def get_stocks_for_product(self, warehouse_id, product_id, quality_id):
        try:
            return self.get(f'/stock/{warehouse_id}/{product_id}/{quality_id}')
        except Exception as e:
            return []
