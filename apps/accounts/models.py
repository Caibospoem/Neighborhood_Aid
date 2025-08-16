from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
# 用户模型

class UserProfile(AbstractUser):
    phone = models.CharField(max_length=11, blank=True, null=True) # 手机号码
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True) # 头像
    bio = models.TextField(blank=True, null=True) # 个人简介
    address = models.CharField(max_length=255, blank=True, null=True) # 地址
    
    def __str__(self):
        return self.username # 返回用户名

# 用户信用分数模型
# 用于记录用户的信用分数
class UserCreditScore(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE) # 与UserProfile关联，意思是如果用户被删除，则信用分数也会被删除
    score = models.IntegerField(default=70) # 信用分数，默认为0
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.score}" # 返回用户名和信用分数
    

# 邮箱验证模型
# 用于存储用户的邮箱验证信息
class EmailVerificationCode(models.Model):
    email = models.EmailField()  # 邮箱地址
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.code}"