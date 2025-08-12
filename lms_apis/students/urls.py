from django.urls import path
from .views import register_student, login_student,home, get_all_students,get_student_only, get_lectures

urlpatterns = [
    path('register/',  register_student,name='Signup'),
    path('login/', login_student, name='Login'),
    path("",home),
    path('all-students/', get_all_students, name='get_all_students'),
    path('student/<int:sid>/', get_student_only, name='get_student_only'),
    path('all_lectures/', get_lectures, name='get_all_lectures'),

]
