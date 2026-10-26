from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView
from .models import User
from .serializers import UserSerializer,RegisterSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
# Create your views here.

class RegisterView(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer
    permission_classes=[AllowAny]

# class ProfileView(ListAPIView):
#     queryset=User.objects.get(username=self.username)
#     serializer_class=UserSerializer
#     permission_classes=[IsAuthenticated]
