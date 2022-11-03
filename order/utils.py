from random import randint
from rest_framework.request import Request


def get_client_ip(request: Request) -> str:
    """Сервис для получение ip клиента"""

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_short_uuid():
    return randint(1000000000, 9999999999)
