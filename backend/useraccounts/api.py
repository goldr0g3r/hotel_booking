from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from useraccounts.models import User
from useraccounts.serializer import UserDetailSerializer
from rest_framework.views import APIView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from rest_framework.permissions import IsAuthenticated


class LoginView(LoginView):
    model = User


@api_view(["GET"])
@permission_classes([])
@authentication_classes([])
def landloard_detail(request, pk):
    user = User.objects.get(id=request.user.id)
    serializer = UserDetailSerializer(user, many=False)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([])
@authentication_classes([IsAuthenticated])
def generate_refresh_token(request):
    refresh_token = request.COOKIES.get("refresh")
    if not refresh_token:
        return TokenRefreshView.as_view()(request)
    return JsonResponse({"refresh": refresh_token}, status=200)
