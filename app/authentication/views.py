from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

User = get_user_model()


class AuthViewSet(viewsets.ViewSet):
    def create(self, request):
        data = request.data.copy()
        email = data.get("email", "")
        password = data.get("password", "")
        user = User.objects.get(email=email)
        if not user:
            raise Exception("Email not existed.")
        pwd_encrypt = getattr(user, "password", "")
        is_correct_pwd = check_password(password, pwd_encrypt)
        if not is_correct_pwd:
            raise Exception("Password is incorrect.")
        token = RefreshToken.for_user(user=user)
        resp_data = dict(refresh=str(token), access=str(token.access_token))
        return Response(data=resp_data, status=status.HTTP_200_OK)
