from django.contrib.auth import get_user_model

import environ
from dj_rest_auth.registration.serializers import (
    RegisterSerializer as BaseRegisterSerializer,
)
from rest_framework import serializers

env = environ.Env()

User = get_user_model()


class RegisterSerializer(BaseRegisterSerializer, serializers.ModelSerializer):

    password1 = None
    password2 = None

    class Meta:
        model = User
        fields = ["email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        return data

    def get_cleaned_data(self):
        return {
            "password1": self.validated_data.get("password", ""),
            "email": self.validated_data.get("email", ""),
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["uuid", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}
