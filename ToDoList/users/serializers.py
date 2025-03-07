from rest_framework import serializers
from .models import ToDoList


class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ['id', 'title', 'content', 'tag', 'status', 'created_at', 'updated_at']
