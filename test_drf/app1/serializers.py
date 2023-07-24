from .models import Register
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

