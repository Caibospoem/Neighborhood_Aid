from django.shortcuts import render

from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model
from .serializers import UserProfileSerializer, UserRegisterSerializer



User = get_user_model()

class RegisterView(generics.CreateAPIView):
    """
    用户注册视图
    """
    queryset = User.objects.all() # 获取所有用户
    serializer_class = UserRegisterSerializer # 使用序列化器进行数据验证和创建
    permission_classes = [permissions.AllowAny] # 允许任何人访问此视图


class ProfileView(generics.RetrieveUpdateAPIView):
    """
    用户个人信息视图
    """
    queryset = User.objects.all() # 获取所有用户
    serializer_class = UserProfileSerializer # 使用序列化器进行数据验证和更新
    permission_classes = [permissions.IsAuthenticated] # 仅允许已认证的用户访问此视图

    def get_object(self):
        return self.request.user # 返回当前请求的用户对象

def home(request):
    """
    Render the home page of the application.
    """
    return render(request, 'base.html')
