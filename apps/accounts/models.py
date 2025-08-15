from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
    phone = models.CharField(max_length=11, blank=True, null=True) # 手机号码
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True) # 头像
    bio = models.TextField(blank=True, null=True) # 个人简介
    address = models.CharField(max_length=255, blank=True, null=True) # 地址
    
    def __str__(self):
        return self.username # 返回用户名

class UserCreditScore(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE) # 与UserProfile关联，意思是如果用户被删除，则信用分数也会被删除
    score = models.IntegerField(default=70) # 信用分数，默认为0
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.score}" # 返回用户名和信用分数