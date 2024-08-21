from django.utils import timezone

from .models import User, Promocode
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, LoginSerializer, PromocodeCreateSerializer
from rest_framework import  permissions


# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpgradeStageView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        promocode = request.data.get('promocode')

        if not promocode:
            return Response({"detail": "Promocode is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            promo = Promocode.objects.get(code=promocode)
        except Promocode.DoesNotExist:
            return Response({"detail": "Invalid Promocode"}, status=status.HTTP_400_BAD_REQUEST)

        if not promo.is_valid():
            return Response({"detail": "Promocode is not valid or expired"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the user has already used this promocode
        if user in promo.used_by.all():
            return Response({"detail": "You have already used this Promocode"}, status=status.HTTP_400_BAD_REQUEST)

        # If everything is fine, upgrade the user's stage
        user.upgrade_stage()
        promo.used_by.add(user)

        return Response({'stage': user.stage})


class PromocodeCreateView(generics.CreateAPIView):
    queryset = Promocode.objects.all()
    serializer_class = PromocodeCreateSerializer
    permission_classes = [permissions.IsAdminUser]
