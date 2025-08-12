from django.urls import path
from .views import create_lecture,delete_lecture


urlpatterns = [
    path('create/', create_lecture, name='create_lecture'),
    path('delete/<int:lecture_id>/', delete_lecture, name='delete_lecture'),

]
