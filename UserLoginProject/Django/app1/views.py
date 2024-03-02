from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer
from .models import Customer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

# Create your views here.


class CustomerAdd(APIView):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            email = request.data.get('email', None)
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
        else:
            return Response({"error": 'User is not authenticated'},
                            status=status.HTTP_401_UNAUTHORIZED)


class AdminLogin(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id': user.id})
        else:
            return Response({'error': 'Invalid credentials'}, 
                           status=status.HTTP_401_UNAUTHORIZED)

class AdminLogout(APIView):
    def post(self, request, *args, **kwargs):
        try:
            request.auth.delete()
            return Response({'message': 'Logout successfully'}, 
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":"User is not authenticated"},
                            status=status.HTTP_401_UNAUTHORIZED)