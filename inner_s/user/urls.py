from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet

# Notes router
user_router = routers.SimpleRouter()
user_router.register(
    r'user',
    UserViewSet,
)

urlpatterns = [
    path('api/', include(user_router.urls)),
]
