from rest_framework.generics import CreateAPIView
from .serializers import CreateUserSerializer

class UserCreateAPIView(CreateAPIView):
    serializer_class = CreateUserSerializer