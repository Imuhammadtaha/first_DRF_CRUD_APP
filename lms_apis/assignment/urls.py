from django.urls import path
from .views import upload_assignment, delete_assignment

urlpatterns = [
    path("upload_assignment/", upload_assignment, name="create_assignment"),
    path('delete_assignment/<int:asn_id>/', delete_assignment, name="delete_assignment")
]
