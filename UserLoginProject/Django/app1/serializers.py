from rest_framework.serializers import ModelSerializer
from .models import Customer

class UserSerializer(ModelSerializer):

    def to_representation(self, obj):
        data = super().to_representation(obj)
        return data

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email',
                  'dob', 'phone']