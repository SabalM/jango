"""test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
#from polls import views
from classbased import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls, name='admin'), 
    path("1/",include('polls.urls')),
    path("2/",include('classbased.urls')),
    path('',include('userapp.urls')),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='userapp/password_reset_done.htm'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="userapp/password_reset_confirm.htm"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='userapp/password_reset_complete.htm'), name='password_reset_complete'),
]


