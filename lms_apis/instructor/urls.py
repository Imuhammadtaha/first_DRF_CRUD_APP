from django.urls import path

from .views import register_instructor,login_instructor

urlpatterns = [
    path('register/',register_instructor,name = 'Signup'),
    path('login/', login_instructor,name= 'Login'),
    
]