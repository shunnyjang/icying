from rest_framework import serializers

from core.serializers import RestaurantDetailSerializer
from rewards.models import Rewards, RewardCode, Donation


class RewardSerializer(serializers.ModelSerializer):
    is_exist = serializers.SerializerMethodField()

    # def get_is_exist(self, obj):

    class Meta:
        model = RewardCode
        fields = []


class DonationSerializer(serializers.ModelSerializer):
    restaurant = RestaurantDetailSerializer(source='restaurant_id', read_only=True)

    class Meta:
        model = Donation
        fields = [
            'donation_id',
            'user_id',
            'restaurant_id',
            'restaurant',
            'ice_pack_number',
            'created_at',
        ]
