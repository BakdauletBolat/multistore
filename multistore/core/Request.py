import requests
import json

class Request:
    """Класс Request для связи с Сервисом акций"""
    

    url = 'http://10.10.1.70/api/v1'

    def findSales(self,body):
        """Функция для получение доступных акций"""

        payload = json.dumps(body)
        headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vMTAuMTAuMS42NTo4MDkwL2FwaS9sb2dpbiIsImlhdCI6MTY2MzA0NTY0MSwiZXhwIjoxNjYzOTA5NjQxLCJuYmYiOjE2NjMwNDU2NDEsImp0aSI6IjQ5dzVqTGs4QXhuSHBZa2oiLCJzdWIiOiIxMDgxIiwicHJ2IjoiOWE1Mjc2NWM2ZjgxYjE3ZjJiMTQ2ZTg2NDJlYzU0OWUzNDhkMTFlZiIsImlkIjoxMDgxLCJmaXJzdF9uYW1lIjoiZGl5YXIuc2giLCJyb2xlIjpudWxsfQ.8S5P6MiaRKw3ytxmLKjJpQBxN-Tyb79UcBJlSXkf6uk'
        }

        response = requests.request("POST", f"{self.url}/sale/find/", headers=headers, data=payload)

        
        return response.json()

