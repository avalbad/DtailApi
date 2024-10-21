from rest_framework import serializers
from Task.models import MyObject

class MyObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyObject
        fields = ['id', 'number']