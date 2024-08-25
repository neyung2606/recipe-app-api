from rest_framework import viewsets, status
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from user.serializers import UserSerializer


User = get_user_model()


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        data = request.query_params
        users = User.objects.all()
        serializers = UserSerializer(users, many=True).data
        return Response(data=serializers)

    def create(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.save()
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
