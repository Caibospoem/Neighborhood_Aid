from django.urls import path
from .views import RegisterView, UserProfileView, send_verification_email, verify_code, send_password_reset_code, reset_password, VerifyTokenView



urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'), # 用户注册视图
    path('profile/', UserProfileView.as_view(), name='profile'), # 用户个人信息视图
    path('verify-token/', VerifyTokenView.as_view(), name='verify-token'), # 
    
    path('send_verification_email/', send_verification_email, name='send_verification_email'), # 发送邮箱验证邮件
    path('verify_email/', verify_code, name='verify_email'), # 验证邮箱视图
    path('send_password_reset_code/', send_password_reset_code, name='send_password_reset_code'), # 发送密码重置验证码
    path('reset_password/', reset_password, name='reset_password'), # 重置密码视
    
]
