from django.urls import path, include
from rest_framework import routers
from . import views
from .views import UserViewSet, GetUserInfoView

# Notes router
user_router = routers.SimpleRouter()
user_router.register(
    r'user',
    UserViewSet,
)

urlpatterns = [
    path('api/', include(user_router.urls)),
    path('', views.main_page, name='main_page'),
]
