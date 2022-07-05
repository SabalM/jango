from django.urls import path,include
#from polls import views
from userapp import views

urlpatterns = [
    path("register/", views.register, name='register'), 
    path("login/",views.user_login,name='user_login' ),
    path("logout/",views.user_logout,name='user_logout'),
    path("password_reset/",views.password_reset_request,name="password_reset"),
]