from rest_framework.views import APIView
from rest_framework.views import Request
from rest_framework.response import Response
from users.serializers import PhoneSerializer, VerifyUserSerializer
from users.actions.api import SendUserOtpAction
from users.models import User
from users.tasks.api import GetFilteredOtpTask, CheckTimeTask, GenerateTokenForUserTask
from users.exceptions import OtpNotValidException


class AuthorizationUserView(APIView):

    def post(self, request: Request):
        phone_serializer = PhoneSerializer(data=request.data)
        phone_serializer.is_valid(raise_exception=True)
        phone = phone_serializer.validated_data.get('phone', None)
        user, is_created = User.objects.get_or_create(phone=phone)
        SendUserOtpAction.run(user=user)
        return Response({'status': 'success'}, status=201)


class VerifyUserView(APIView):

    def post(self, request: Request):
        verify_otp_serializer = VerifyUserSerializer(data=request.data)
        verify_otp_serializer.is_valid(raise_exception=True)
        phone = verify_otp_serializer.validated_data.pop('phone')
        verify_otp_serializer.validated_data['user__phone'] = phone

        otp = GetFilteredOtpTask.run(verify_otp_serializer.validated_data)
        is_valid, user = CheckTimeTask.run(user_otp=otp)

        if is_valid:
            token = GenerateTokenForUserTask.run(user=user)
            return Response(token, status=200)
        else:
            raise OtpNotValidException()
