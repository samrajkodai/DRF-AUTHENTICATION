from djoser.serializers import UserCreateSerializer
from . models import  User


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("id", "email", "username", "first_name", "last_name", "password",'phoneno')