from rest_framework import serializers
from .models import User, ToDoList


class UserRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']


class UserLoginSerializer(serializers.ModelSerializer):
    pass


class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = '__all__'
