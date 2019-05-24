"""starnavi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from blog import views
from django.conf.urls import include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from rest_auth.registration.views import VerifyEmailView

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('admin/', admin.site.urls),
    path('posts/', views.PostList.as_view()),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='detail'),
    path('create/', views.PostCreate.as_view(), name='create'),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('account-confirm-email/', VerifyEmailView.as_view(),
                 name='account_email_verification_sent'),
    path('auth-jwt/', obtain_jwt_token),
    path('auth-jwt-refresh/', refresh_jwt_token),
    path('auth-jwt-verify/', verify_jwt_token),


]
