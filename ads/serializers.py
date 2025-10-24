from rest_framework import serializers
from .models import Ad

class AdSerializer(serializers.ModelSerializer):
    """
    Сериализатор для объявления.
    """
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Ad
        fields = ['id', 'title', 'description', 'owner', 'created_at']
