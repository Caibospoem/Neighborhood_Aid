from django.urls import path
from .views import home, RegisterView, ProfileView, send_verification_email, verify_code



urlpatterns = [
    path('', home, name='home'), # 首页视图
    path('register/', RegisterView.as_view(), name='register'), # 用户注册视图
    path('profile/', ProfileView.as_view(), name='profile'), # 用户个人信息视图
    
    path('send_verification_email/', send_verification_email, name='send_verification_email'), # 发送邮箱验证邮件
    path('verify_email/', verify_code, name='verify_email'), # 验证邮箱视图

    
]
