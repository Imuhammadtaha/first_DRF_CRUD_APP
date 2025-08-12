from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from instructor.instructorMIddleware import IsInstructor, IsOwner
from rest_framework.permissions import IsAuthenticated
from .serializer import ResultSerializer
from django.shortcuts import get_object_or_404
from .models import Result
from students.models import Student



# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsInstructor])
def upload_result(request, student_id):
    try:
        student = get_object_or_404(Student, id=student_id)
        
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            res = serializer.save(student=student)
            return Response({
                "Message": "Result Uploaded Successfully",
                "Result_id": res.id,
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({"Message": f"Server Error {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

   
@api_view(['DELETE']) 
@permission_classes([IsAuthenticated, IsInstructor, IsOwner])
def delete_result(request, res_id):
    res = get_object_or_404(Result, id=res_id)

    for permission in (IsOwner(),):
        if not permission.has_object_permission(request, None, res):
            return Response({"Message": "You're Not Permitted"}, status=status.HTTP_403_FORBIDDEN)

    res.delete()
    return Response({"Message": "Result Deleted Successfully"}, status=status.HTTP_200_OK)
