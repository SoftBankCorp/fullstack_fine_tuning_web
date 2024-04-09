"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework.authtoken.views import obtain_auth_token 
# from decouple import config
# OPENAI_API_KEY = config('OPENAI_API_KEY')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('fine_tuning_chatbot.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    #이제 api-token-auth/ 엔드포인트로 사용자 이름과 비밀번호를 포함한 JSON 객체를 전송하여 토큰을 생성할 수 있습니다.
]