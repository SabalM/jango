from django.urls import path,include
#from polls import views
from userapp import views

urlpatterns = [
    path("register/", views.register, name='register'), 
    path("login/",views.user_login,name='user_login' ),
]