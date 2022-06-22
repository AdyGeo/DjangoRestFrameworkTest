from rest_framework import serializers
from ..models import (Task, Note)

class TaskSerializer(serializers.ModelSerializer):
    priorityName = serializers.CharField(source='get_priority_display', read_only=True)
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields =  ['done']


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','done']


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

