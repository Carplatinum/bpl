from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import UserSerializer

class UserListView(generics.ListAPIView):
    """
    Просмотр списка пользователей, доступ разрешен всем.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
