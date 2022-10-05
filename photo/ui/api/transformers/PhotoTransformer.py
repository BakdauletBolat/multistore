from rest_framework import serializers

class PhotoTransformer(serializers.Serializer):
    
    photo = serializers.FileField()

    
