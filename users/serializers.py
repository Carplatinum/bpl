from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для кастомного пользователя.
    """
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'is_active', 'is_staff']
        read_only_fields = ['id', 'is_active', 'is_staff']
