from django.urls import path
from .views import register_admin,login_admin


urlpatterns = [
    path("register/",register_admin,name='SignUp'),
    path('login/', login_admin,name='login'),
]
