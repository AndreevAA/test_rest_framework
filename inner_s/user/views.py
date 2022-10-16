from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer

from capitals.models import Capital
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class GetUserInfoView(APIView):
    def get(self, request):
        # Извлекаем набор всех записей из таблицы User
        queryset = User.objects.all()

        # Создаём сериалайзер для извлечённого наборa записей
        serializer_for_queryset = UserSerializer(
            instance=queryset,  # Передаём набор записей
            many=True  # На вход подается именно набор, а не одна запись
        )
        return Response(serializer_for_queryset.data)


def main_page(request):
    """
    Контроллер для отображения на главной странице списка всех записей.
    """
    list_of_capitals = User.objects.all()
    context = {'list_of_capitals': list_of_capitals}
    return render(
        request=request,
        template_name='user/main.html',
        context=context
    )
