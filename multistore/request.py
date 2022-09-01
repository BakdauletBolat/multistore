import requests

class Request:
    url = 'http://10.10.1.74:80'
    def __init__(self) -> None:
        self.token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vMTAuMTAuMS42NTo4MDkwL2FwaS9sb2dpbiIsImlhdCI6MTY2MjAwNDM0NCwiZXhwIjoxNjYyODY4MzQ0LCJuYmYiOjE2NjIwMDQzNDQsImp0aSI6Ik1RV2I0d1pwbnVIem43WlYiLCJzdWIiOiIxMDg3IiwicHJ2IjoiNmZhYzFkOWY1OTk1YTM5MTgzZjZkYmE3ZGNkMjQ2YjRiOWRkZjIxZCIsImlkIjoxMDg3LCJmaXJzdF9uYW1lIjoiZGl5YXIuc2giLCJyb2xlIjpudWxsfQ.TDq4qqJrThm1Sfrq1whsXNSXPtuy6FFxB36L140j460'


    def get(self,url):
        response = requests.get(f'{self.url}{url}',headers={
        'Authorization':'Bearer ' + self.token
            })
        
        return response.json()
