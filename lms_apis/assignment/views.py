from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from instructor.instructorMIddleware import IsInstructor, IsOwner
from rest_framework.permissions import IsAuthenticated
from .serializer import AssignmentSerializer
from .models import Assignment
from django.shortcuts import get_object_or_404


# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsInstructor])
def upload_assignment(request):
    try:
        serializer = AssignmentSerializer(data = request.data)
        if serializer.is_valid():
            if serializer.is_valid():
                assignment = serializer.save(instructor=request.user.instructor)  

            return Response({"Message":"Assignment Uploaded Successfully ","assignment_id":assignment.id, "assignment":serializer.data },status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as e:
        return Response({"Message":f"Server Error {str(e)}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsInstructor, IsOwner])

def delete_assignment(request, asn_id):
    assignmet = get_object_or_404(Assignment, id = asn_id)
    
    for permission in [IsOwner()]:
        
        if not permission.has_object_permission(request, None, assignmet):
            return Response({"Message":"Permission Denied"},status=status.HTTP_403_FORBIDDEN)
    
    assignmet.delete()
    
    return Response({"Message":"Assignment deleted successfully"})