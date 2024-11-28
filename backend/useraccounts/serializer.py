from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.http import JsonResponse


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = [
            "id",
            "date_joined",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
        ]
        extra_kwargs = {
            "email": {"required": False},
            "name": {"required": False},
            "avatar": {"required": False},
        }
