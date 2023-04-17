from .models import CustomUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    
    """
        Serializing our custom models  
    """
     
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'gender', 'email', 'phone_number']