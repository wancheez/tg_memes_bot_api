from rest_framework import viewsets, permissions

from .models import ScheduleTask, TaskType
from .serializers import ScheduleTaskSerializer, TaskTypeSerializer


class ScheduleTaskView(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    queryset = ScheduleTask.objects.all()
    serializer_class = ScheduleTaskSerializer


class TaskTypeView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = TaskType.objects.all()
    serializer_class = TaskTypeSerializer
