from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import StudentSerializer
from .models import Student
from lecture.models import Lecture
from lecture.serializer import LectureSerializer

@api_view(['POST'])

def register_student(request):
    try:
        name = request.data.get("name")
        email = request.data.get("email")
        password = request.data.get("password")
        
        if not all([name,email,password]):
            return Response({"Message":"Name, Email and Password are mandatory"},status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email = email).exists():
            return Response({"Message":"User with this email already Exists"},status=status.HTTP_208_ALREADY_REPORTED)

        user = User.objects.create_user(username=email, email=email, password=password)

        student_data = request.data.copy()
        student_data['user'] = user.id

        serializer = StudentSerializer(data = student_data)
        
        if serializer.is_valid():
            serializer.save(user = user)
            token,_ = Token.objects.get_or_create(user = user)

            return Response({"Message":"SignUp Successfull","token":token.key},status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({"Message":f"Server Error {str(e)}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def login_student(request):
    try:
        email = request.data.get("email")
        password = request.data.get("password")
        
        if not all([email,password]):
            return Response({"Message":"Email and Password are mandatory"},status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username = email, password = password)

        if user:
            token,_ = Token.objects.get_or_create(user = user)
            return Response({"Message":"Login Successfull"},status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"Message":"Invalid Credentials"},status=status.HTTP_400_BAD_REQUEST)        
        
    except Exception as e:
        return Response({"Message":f"Server Error {str(e)}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
@api_view(["GET"])

def home():
    return Response({"Message":"Welcome to the lMS APIs"})



@api_view(['GET'])

def get_all_students(request):
    try:
        students = Student.objects.all()
        if students.count() == 0:
            return Response({"Message":"No Students Found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"Message": f"Server Error {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET'])

def get_student_only(request, sid):
    try:
        student = Student.objects.get(id = sid)
        if not student:
            return Response({"Message":"Student Not Found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"Message":f"Server Error {str(e)}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
    

@api_view(['GET'])

def get_lectures(request):
    try:
        lecture = Lecture.objects.all()
        if lecture.count() == 0:    
            return Response({"Message":"No Lectures Found"}, status=status.HTTP_404_NOT_FOUND)  
        serializer = LectureSerializer(lecture, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)     
    except Exception as e:
        return Response({"Message":f"Server Error {str(e)}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)