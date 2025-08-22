# serializers 序列化器 
# 将较为复杂的数据类型（如Django模型实例或QuerySet）转化成Python原生的数据类型，以便渲染成JSON等格式。
from rest_framework import serializers
from .models import UserProfile, UserCreditScore
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

# Serializers for UserProfile model
class UserRegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=False, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'password', 'password2')
    
    def validate(self, attrs):
        if attrs['password'] != attrs.get('password2'):
            raise serializers.ValidationError("两次输入的密码不一致")
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            phone=validated_data.get('phone', ''),
            password=validated_data['password'],
        )
        return user
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'email', 'phone', 'avatar', 'level', 'bio', 'help_count', 'helped_count', 'address', 'points', 'rating')

class UserCreditScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCreditScore
        fields = ['score', 'last_updated']