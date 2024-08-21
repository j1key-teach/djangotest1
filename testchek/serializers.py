from rest_framework import serializers
from .models import Test, Bolim, BolimTest


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class BolimSerializer(serializers.ModelSerializer):
    tests = TestSerializer(many=True, read_only=True)

    class Meta:
        model = Bolim
        fields = '__all__'


class BolimTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BolimTest
        fields = '__all__'
