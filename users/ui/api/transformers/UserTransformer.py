from rest_framework import serializers
from users.models.User import User
class UsersTransformer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'last_login')