from users.tasks.api import GenerateOtpTask, CreateUserOtpTask
from users.models import User
from multistore.request import SmsServiceRequest
from users.exceptions import SmsServiceException


class SendUserOtpAction:

    @staticmethod
    def run(user: User):
        request = SmsServiceRequest()
        otp = GenerateOtpTask.run()
        user_otp = CreateUserOtpTask.run(user=user, otp=otp)
        try:
            request.send_sms(phone=user_otp.user.phone,
                             text=user_otp.otp)
        except Exception as e:
            raise SmsServiceException()



