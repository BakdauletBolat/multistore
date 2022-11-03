from rest_framework import serializers


class PhotoSerializer(serializers.Serializer):
    photo = serializers.FileField()
