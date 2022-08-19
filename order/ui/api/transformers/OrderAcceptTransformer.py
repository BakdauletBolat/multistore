from rest_framework import serializers


class OrderAcceptTransformer(serializers.Serializer):
    
    id = serializers.CharField()
    dateTime = serializers.DateTimeField()
    invoiceId = serializers.CharField()
    amount = serializers.IntegerField()
    issuer = serializers.CharField()
    code = serializers.CharField()
    email = serializers.CharField()
    phone = serializers.CharField()
     