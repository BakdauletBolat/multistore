from typing import Optional
from busket.models.Busket import Busket
import uuid

class GetBusketAction:


    
    def run(self,request) -> tuple[Optional[Busket], str | None]:
        valueUUID = None

        if request.user.is_authenticated:
                try:
                    busket = Busket.objects.get(user=request.user,is_active=True)
                except Busket.DoesNotExist:
                    busket = Busket.objects.create(user=request.user)
        else:
            uuid_user = request.COOKIES.get('uuid_user',None)
            if uuid_user is not None:
                value = request.COOKIES.get('uuid_user')
                try:
                    busket = Busket.objects.get(uuid_user=value,is_active=True)
                except Busket.DoesNotExist:
                    busket = Busket.objects.create(uuid_user=value)
            else:
                valueUUID = str(uuid.uuid4())
                try:
                    busket = Busket.objects.get(uuid_user=valueUUID,is_active=True)
                except Busket.DoesNotExist:
                    busket = Busket.objects.create(uuid_user=valueUUID)  
        return busket,valueUUID