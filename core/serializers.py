from django.contrib.auth import get_user_model
from rest_framework import serializers

from core.models import Restaurant
User = get_user_model()


class RestaurantSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Restaurant
        fields = '__all__'
