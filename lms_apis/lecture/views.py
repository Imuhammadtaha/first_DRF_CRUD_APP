from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from instructor.instructorMIddleware import IsInstructor,IsOwner
from rest_framework.permissions import IsAuthenticated
from .serializer import LectureSerializer
from .models import Lecture
from django.shortcuts import get_object_or_404

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsInstructor])

def create_lecture(request):
    try:
        serializer = LectureSerializer(data = request.data)
        
        if serializer.is_valid():
            lecture = serializer.save()
            return Response({"Message":"Lecture Created Successfully","lecture_id":lecture.id, "Lecture":serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as e:
        return Response({"Message":f"Server Error {str(e)}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated,IsOwner])

def delete_lecture(request, lec_id):
    lecture = get_object_or_404(Lecture, id = lec_id)
    
    for permssion in [IsOwner()]:
        
        if not permssion.has_object_permission(request,None,lecture):
            return Response({"Message":"Permission Denied"},status=status.HTTP_401_UNAUTHORIZED)

    lecture.delete()
    return Response({"Message":"Lecture Deleted Successfully"})