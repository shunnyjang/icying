from rest_framework import serializers

from rewards.models import Rewards, RewardCode, Donation


class RewardSerializer(serializers.ModelSerializer):
    is_exist = serializers.SerializerMethodField()

    # def get_is_exist(self, obj):

    class Meta:
        model = RewardCode
        fields = []


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'
