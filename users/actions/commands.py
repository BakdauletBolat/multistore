from users.models import User
from loguru import logger


class CreateUserAction:

    @staticmethod
    def run():
        try:
            user = User.objects.create_superuser(email='admin4@gmail.com', password="123", phone='8705919ds43s864')
           
            logger.success(f'Успешно создан супер пользователь')
        except Exception as e:
            print(e)
            pass
