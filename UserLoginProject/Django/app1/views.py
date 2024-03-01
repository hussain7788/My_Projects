from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from .serializers import UserSerializer
from .models import Customer

# Create your views here.

class AdminLogin(APIView):

    def post(self, request):
        user_name = request.data.get('username', None)
        password = request.data.get('password', None)
        if user_name and password:
            user = authenticate(request, 
                                username=user_name, 
                                password=password)
            if user is not None:
                login(request, user)
                return Response({'message': 'Login successful'}, 
                                status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, 
                                status=status.HTTP_401_UNAUTHORIZED)


class CustomerAdd(APIView):

    def post(self, request):
        first_name = request.data.get('first_name', None)
        last_name = request.data.get('last_name', None)
        email = request.data.get('email', None)
        dob = request.data.get('dob', None)
        phone = request.data.get('phone', None)
        if Customer.objects.filter(email=email).exists():
            return Response({"error": "customer with this email already exists"},
                             status=status.HTTP_400_BAD_REQUEST)
        ser_data = UserSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response({"message":"User registered successfully"},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({"error": 'Invalid data'},
                            status=status.HTTP_400_BAD_REQUEST)


class AdminLogout(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logout successfully'}, 
                        status=status.HTTP_200_OK)