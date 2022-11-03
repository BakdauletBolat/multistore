import math, random
from users.models import UserOtp, User
from datetime import timedelta
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken

class GenerateOtpTask:

    @staticmethod
    def run():
        digits = "0123456789"
        otp = ""
        for i in range(4):
            otp += digits[math.floor(random.random() * 10)]

        return otp


class CreateUserOtpTask:
    def run(user: User, otp: str) -> UserOtp:
        return UserOtp.objects.create(
            otp=otp,
            user=user
        )


class CheckTimeTask:

    @staticmethod
    def run(user_otp: UserOtp):
        today_time = timezone.now() - timedelta(minutes=10)
        if user_otp is not None:
            if user_otp.created_at < today_time:
                return False, user_otp.user
            return True, user_otp.user
        return False, None


class GetFilteredOtpTask:

    @staticmethod
    def run(validated_data):
        return UserOtp.objects.filter(**validated_data).order_by('created_at').last()


class GenerateTokenForUserTask:

    @staticmethod
    def run(user: User):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
