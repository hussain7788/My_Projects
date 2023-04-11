from rest_framework import serializers
from .models import *

class TodoSerializer(serializers.ModelSerializer):

    def to_representation(self, obj):
        data = super().to_representation(obj)
        print("data::", data, obj)
        if obj.t_completed == 0:
            data['t_completed'] = False
        else:
            data['t_completed'] = True
        return data


    class Meta:
        model = TodoModel
        fields = "__all__"