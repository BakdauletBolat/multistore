
from typing import Optional
from order.models.Order import Address, Order
from users.models.User import User

class AddressCreateTask:


    def __init__(self,dto:Optional[dict],user:User) -> None:
        self.dto = dto
        self.user = user

    def run(self)->Optional[int]:
        if self.dto is not None:
            return Address.objects.create(
                    city_id=self.dto['city_id'],
                    street=self.dto['street'],
                    user = self.user,
                    number_house=self.dto['number_house'],
                    number_flat=self.dto.get('number_flat',None),
                    
            ).id

        return None