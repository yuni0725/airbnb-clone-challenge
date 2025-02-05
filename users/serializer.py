from rest_framework.serializers import ModelSerializer
from .models import User


class TinyUserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)


class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "is_superuser",
            "id",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
        )
