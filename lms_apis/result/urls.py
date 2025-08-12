from django.urls import path
from .views import upload_result,delete_result

urlpatterns = [
    path("upload_result/<int:student_id>/", upload_result, name='upload_result' ),

    path("delete_result/<int:res_id>/", delete_result, name='delete_result')
]
