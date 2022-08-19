import requests

class Request:
    url = 'http://10.10.1.74:80'
    def __init__(self) -> None:
        self.token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vMTAuMTAuMS42NTo4MDkwL2FwaS9sb2dpbiIsImlhdCI6MTY2MDYzMjUwNywiZXhwIjoxNjYxNDk2NTA3LCJuYmYiOjE2NjA2MzI1MDcsImp0aSI6Imo2UjIzY05SYlI2Y2pjTHkiLCJzdWIiOiI4NzQiLCJwcnYiOiI2ZmFjMWQ5ZjU5OTVhMzkxODNmNmRiYTdkY2QyNDZiNGI5ZGRmMjFkIiwiaWQiOjg3NCwiZmlyc3RfbmFtZSI6ImV6YXoua2giLCJyb2xlIjpudWxsfQ.LcZB4LXhHusHTPLkPoZjLUYJDuET6ToS_vFXa4VKxT8'


    def get(self,url):
        response = requests.get(f'{self.url}{url}',headers={
        'Authorization':'Bearer ' + self.token
            })
        
        return response.json()
