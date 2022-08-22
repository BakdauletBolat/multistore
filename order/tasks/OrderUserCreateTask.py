

from order.dto.OrderCreateDto import OrderCreateDto
from order.models.Order import Order
from users.models.User import User

class OrderUserCreateTask:


    def __init__(self,userData) -> None:
        self.userData = userData

    def run(self):

        try:
            user = User.objects.get(phone=self.userData['phone'])
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=self.userData['email'])
            except User.DoesNotExist:
                user = User.objects.create(
                                email=self.userData['email'],
                                last_name=self.userData['last_name'],
                                first_name=self.userData['first_name'],
                                phone=self.userData['phone'],
                            )
                user.set_password('Zz123456')
                user.save()

        return user