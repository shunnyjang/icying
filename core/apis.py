from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import Restaurant
from core.serializers import RestaurantSerializer

from api.permissions import IsOwner

import requests
import os

User = get_user_model()


def get_lat_and_lng_from_google_maps_api(address):
    url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json" \
          f"?input={address}" \
          f"&inputtype=textquery" \
          f"&fields=geometry" \
          f"&key={os.getenv('GOOGLE_MAPS_API_KEY')}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload).json()
    geometry = response.get('candidates')[0].get('geometry').get('location')

    return geometry.get('lat'), geometry.get('lng')


class RestaurantApi(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        request.query.get()

    def post(self, request):
        request.data['user_id'] = request.user.id
        request.data['latitude'], request.data['longitude'] = \
            get_lat_and_lng_from_google_maps_api(request.data['address'])
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "매장 등록 성공"
                }, status=status.HTTP_201_CREATED)
        return Response({
            "code": serializer.errors,
            "message": "매장 등록 실패"
        }, status=status.HTTP_400_BAD_REQUEST)


class MyRestaurantApi(APIView):
    parser_classes = [JSONParser]
    permission_classes = [IsOwner]

    def get(self, request):
        try:
            queryset = Restaurant.objects.get(user_id=request.user)
            serializer = RestaurantSerializer(queryset)
            return Response({
                "message": "호출 성공",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Restaurant.DoesNotExist:
            return Response({
                "message": "등록한 매장이 없습니다"
            }, status=status.HTTP_400_BAD_REQUEST)
