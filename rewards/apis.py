from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import Restaurant

from rewards.serializers import DonationSerializer

User = get_user_model()


def update_restaurant_list_up_status(restaurant_id, is_restaurant_ice_full):
    try:
        restaurant = Restaurant.objects.get(restaurant_id=restaurant_id)
        restaurant.is_full = is_restaurant_ice_full
        restaurant.save()
    except Restaurant.DoesNotExist:
        pass


class CreateDonationApi(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        is_restaurant_ice_full = request.data.get('is_full')
        del request.data['is_full']
        serializer = DonationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                "message": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        update_restaurant_list_up_status(request.data.get('restaurant_id'), is_restaurant_ice_full)
        return Response({
            "message": "아이스팩 받음 등록 성공"
        }, status=status.HTTP_201_CREATED)
