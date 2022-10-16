from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    login = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=150)
    acs_lvl = serializers.IntegerField()
    # author = serializers.CharField(source='author.username', max_length=200)
