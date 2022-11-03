from rest_framework.exceptions import APIException
from rest_framework import status


class SmsServiceException(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'Ошибка при сервисе Sms Service'
    default_code = 'smsservicerror'


class OtpNotValidException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Не валидный код или истек время кода'
    default_code = 'nodvalidotp'
