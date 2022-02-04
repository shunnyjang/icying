from django.urls import path, include
from core.apis import *


urlpatterns = [
    path('restaurant/', RestaurantApi.as_view()),
    path('my-restaurant/', MyRestaurantApi.as_view())
]
