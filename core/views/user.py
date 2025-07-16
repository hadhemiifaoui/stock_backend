

import logging
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from  ..models.role import Role
from ..models import User
from ..serializers.userSerializer import UserSerializer
from ..models.role import Role

logger = logging.getLogger(__name__)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def signup(self, request):
        role_id = request.data.get("role_id")
        try:
            role = Role.objects.get(id=role_id)
        except Role.DoesNotExist:
            return Response({"error": "role id invalid"}, status=status.HTTP_400_BAD_REQUEST)

        password = request.data.get("password")
        request.data["password"] = password
        request.data["role"] = role.id

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = self.generate_jwt_token(user)
            return Response({
                "token": token,
                "user": serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def login(self, request):
        user_name = request.data.get("user_name", "").strip()
        password = request.data.get("password", "").strip()

        logger.debug(f"Login attempt for user: {user_name}")

        try:
            user = User.objects.get(user_name=user_name)
        except User.DoesNotExist:
            logger.error(f"User {user_name} not found.")
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        if check_password(password, user.password):
            token = self.generate_jwt_token(user)
            user_data = UserSerializer(user).data
            logger.debug(f"User {user_name} logged in successfully.")
            return Response({
                "token": token,
                "user": user_data
            }, status=status.HTTP_200_OK)
        else:
            logger.error(f"Password mismatch for user: {user_name}")
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    def generate_jwt_token(self, user):
        refresh = RefreshToken.for_user(user)
        #return {
           # 'refresh': str(refresh),
          #'access': str(refresh.access_token),
        #}

        return {'access': str(refresh.access_token)}

    @action(detail=False, methods=['get'], url_path='role/(?P<role_id>[0-9]+)')
    def get_users_by_role(self, request, role_id=None):
        users = User.objects.filter(role_id=role_id)
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)