from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from .serializer import AdminSerializer

@api_view(['POST'])
def register_admin(request):
    try:
        name = request.data.get("name")
        email = request.data.get("email")
        password = request.data.get("password")
        
        if not all([name, email, password]):
            return Response({"Message":"Name, Email and Password are mandatory"}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(email=email).exists():
            return Response({"Message":"User with this email already exists"}, status=status.HTTP_208_ALREADY_REPORTED)
        
        user = User.objects.create_user(username=email, email=email, password=password)

        admin_data = request.data.copy()
        admin_data['user'] = user.id
        admin_data['role'] = 'admin'
        
        serializer = AdminSerializer(data=admin_data)
        
        if serializer.is_valid():
            serializer.save(user=user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"Message":"Admin Registered", "token":token.key}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return Response({"Message":f"Error in Registration {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])

def login_admin(request):
    try:
        email = request.data.get("email")
        password = request.data.get("password")

        if not all([email,password]):
            return Response({"Message":"Email or Password is required"})
        
        user = authenticate(username = email, password = password)
        
        if user is not None:
            token,_ = Token.objects.get_or_create(user = user)
            return Response({"Message":"Login Successfull","token":token.key},status=status.HTTP_201_CREATED)
        
        return Response({"Message":"Invalid Credentials"},status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"Message":f"Server error in login {str(e)}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
