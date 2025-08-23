# urls.py
"""
URL configuration for neighborhood_aid project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name='home/base.html'), name='home'),  # 首页视图
    path('profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),  # 个人资料视图
    path('register/', TemplateView.as_view(template_name='registration/register.html'), name='register'),  # 注册视图
    path('api/accounts/', include('apps.accounts.urls')),
    
    # JWT 认证视图
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # 获取 JWT 访问令牌
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # 刷新 JWT 访问令牌
]
