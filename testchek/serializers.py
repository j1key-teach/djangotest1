from rest_framework import serializers
from .models import Test, Bolim, UserTestAttempt


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'question', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_option']


class BolimSerializer(serializers.ModelSerializer):
    tests = TestSerializer(many=True)

    class Meta:
        model = Bolim
        fields = ['id', 'title', 'tests']


class UserTestAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTestAttempt
        fields = ['id', 'user', 'test', 'attempt_count', 'is_completed', 'error_count']
