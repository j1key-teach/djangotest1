from rest_framework import serializers
from .models import User
from .models import Promocode


class PromocodeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocode
        fields = ['code', 'is_active', 'valid_until']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'stage', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            stage=validated_data.get('stage', User.JUNIOR)
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
