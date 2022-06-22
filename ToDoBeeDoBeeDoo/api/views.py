from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models import (Task, Note)
from .serializers import (TaskSerializer, TaskUpdateSerializer, NoteSerializer)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TaskUpdatetView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskUpdateSerializer
    http_method_names = ['put','get']


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)
