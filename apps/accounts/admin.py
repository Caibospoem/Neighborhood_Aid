from django.contrib import admin
from .models import UserProfile, UserCreditScore
# Register your models here.

admin.site.register(UserProfile)  # 注册用户模型
admin.site.register(UserCreditScore)  # 注册用户信用分数模型