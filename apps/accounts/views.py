from django.shortcuts import render

from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.utils.crypto import get_random_string

from django.contrib.auth import get_user_model
from .serializers import UserProfileSerializer, UserRegisterSerializer
from .models import EmailVerificationCode
from django.core.mail import send_mail
from django.http import JsonResponse
from neighborhood_aid.settings import DEFAULT_FROM_EMAIL
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt



User = get_user_model()

class RegisterView(generics.CreateAPIView):
    """
    用户注册视图
    """
    queryset = User.objects.all() # 获取所有用户
    serializer_class = UserRegisterSerializer # 使用序列化器进行数据验证和创建
    permission_classes = [permissions.AllowAny] # 允许任何人访问此视图

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        code = request.data.get('code')
        # 校验邮箱验证码
        try:
            verification_code = EmailVerificationCode.objects.get(email=email, code=code)
            # 可加过期校验
            if (now() - verification_code.created_at).seconds > 600:
                return Response({'error': '验证码已过期'}, status=status.HTTP_400_BAD_REQUEST)
        except EmailVerificationCode.DoesNotExist:
            return Response({'error': '邮箱未验证或验证码错误'}, status=status.HTTP_400_BAD_REQUEST)
        # 验证通过，创建用户
        response = super().create(request, *args, **kwargs)
        # 注册成功后删除验证码记录
        verification_code.delete()
        return response

class ProfileView(generics.RetrieveUpdateAPIView):
    """
    用户个人信息视图
    """
    queryset = User.objects.all() # 获取所有用户
    serializer_class = UserProfileSerializer # 使用序列化器进行数据验证和更新
    permission_classes = [permissions.IsAuthenticated] # 仅允许已认证的用户访问此视图

    def get_object(self):
        return self.request.user # 返回当前请求的用户对象


@csrf_exempt
def send_verification_email(request):
    if request.method == 'POST':
        import json
        try:
            data = json.loads(request.body.decode())
            email = data.get('email')
        except Exception:
            email = request.POST.get('email')
        if not email:
            return JsonResponse({'error': 'Email is required'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already in use'}, status=400)
        
        code = get_random_string(length=6, allowed_chars='0123456789')
        # 不创建用户，只保存验证码和邮箱
        EmailVerificationCode.objects.create(email=email, code=code)

        send_mail(
            'Verify your email',
            f'Your verification code is: {code}',
            DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        return JsonResponse({'message': 'Verification email sent'}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def verify_code(request):
    if request.method == 'POST':
        try:
            import json
            data = json.loads(request.body.decode())
            email = data.get('email')
            code = data.get('code')
        except Exception:
            email = request.POST.get('email')
            code = request.POST.get('code')
        if not email or not code:
            return JsonResponse({'error': 'Email and code are required.'}, status=400)
        try:
            verification_code = EmailVerificationCode.objects.get(email=email, code=code)
            # 可加过期校验
            if (now() - verification_code.created_at).seconds > 600:
                return JsonResponse({'error': 'Code expired.'}, status=400)
            # 验证通过，返回成功
            return JsonResponse({'message': 'Email verified.'})
        except EmailVerificationCode.DoesNotExist:
            return JsonResponse({'error': 'Invalid code.'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)











def home(request):
    """
    Render the home page of the application.
    """
    return render(request, 'base.html')
