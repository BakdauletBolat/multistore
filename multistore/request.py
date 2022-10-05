import requests

class Request:
    url = 'http://10.10.1.74:80/api/v1'
    def __init__(self) -> None:
        self.token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vMTAuMTAuMS42NTo4MDkwL2FwaS9zZXJ2aWNlcy9sb2dpbiIsImlhdCI6MTY2NDg4MDg0MiwiZXhwIjozNTU3MDQwODQyLCJuYmYiOjE2NjQ4ODA4NDIsImp0aSI6InFMcUVNc1hTU2lwZ01tRDUiLCJzdWIiOiIyIiwicHJ2IjoiMDgxNjY2Mjg5ZGMzNTljM2NmM2I3OTczMTg4ZjEwMmVhMGI4OGI3MSIsImlkIjoyLCJmaXJzdF9uYW1lIjoiYmFnZGF1bGV0LmIiLCJyb2xlIjo0fQ.-3R1GmDAUR_s7GOuTurDzF6_yS6JnFRHVXVawBKpVnM'

    def get(self,url):
        response = requests.get(f'{self.url}{url}',headers={
        'Authorization':'Bearer ' + self.token
            })
        
        return response.json()
    
    def get_products(self,page):
        return self.get(
                    f'/catalog/products?page={page}&per_page=1000')

    def get_stocks(self,page):
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
    


