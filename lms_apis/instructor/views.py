from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializer import InstructorSerializer

# Create your views here.

@api_view(['POST'])
def register_instructor(request):
    try:
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not all([name,email,password]):
            return Response({"Message":"Name, Email and Password are mandatory"})
        
        if User.objects.filter(email = email).exists():
            return Response({"Message":"User With this email already Exists"})
        
        user = User.objects.create_user(username=email, email=email, password=password)
        
        instructor_data = request.data.copy()
        instructor_data['user'] = user.id
        instructor_data['role'] = "instructor"
        
        serializer = InstructorSerializer(data = instructor_data)
        
        if serializer.is_valid():
            serializer.save(user = user)
            
            token,_ = Token.objects.get_or_create(user = user)
            
            return Response({"Message":"Instructor Registered Successfully", "token":token.key},status=status.HTTP_201_CREATED) 
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"Message":f"Error in registration {str(e)}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])

def login_instructor(request):
    try:
        
        email = request.data.get('email')
        password = request.data.get('password')

        if not all([email,password]):
            return Response({"Message":"Email and Password is mandatory"})
        
        user = authenticate(username = email, password = password)
        
        if user is not None:
            
            token,_ = Token.objects.get_or_create(user = user)
            
            return Response({"Message":"Login Successfull","token":token.key},status=status.HTTP_201_CREATED)

        return Response({"Message":"Invalid credentials"})
        
    except Exception as e:
        return Response({"Message":f"Server Error {str(e)}"})@api_view(['POST'])
