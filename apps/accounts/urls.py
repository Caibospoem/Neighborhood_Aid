from django.urls import path
from .views import home, RegisterView, ProfileView



urlpatterns = [
    path('', home, name='home'), # 首页视图
    path('register/', RegisterView.as_view(), name='register'), # 用户注册视图
    path('profile/', ProfileView.as_view(), name='profile'), # 用户个人信息视图

]
