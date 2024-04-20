from django.contrib.auth import get_user_model

from djoser import serializers


User = get_user_model()

class UserCreateSerializer(serializers.UserCreateSerializer):
    class Meta(serializers.UserCreateSerializer.Meta): 
        model = User
        fields = ("id","email","username","first_name","last_name","password")