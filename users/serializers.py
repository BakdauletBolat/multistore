from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'last_login')


class PhoneSerializer(serializers.Serializer):
    phone = serializers.CharField()


class VerifyUserSerializer(serializers.Serializer):
    phone = serializers.CharField()
    otp = serializers.CharField()
