from django.urls import path, include
from rewards.apis import *


# restaurant_patterns = [
#     path('', RestaurantApi.as_view()),
#     path('<int:pk>/', RestaurantDetailApi.as_view()),
# ]

urlpatterns = [
    # path('restaurant/', include(restaurant_patterns)),
    path('icepack/', CreateDonationApi.as_view()),
]
