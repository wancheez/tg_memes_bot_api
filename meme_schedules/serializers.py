from rest_framework import serializers

from .models import ScheduleTask, TaskType


class ScheduleTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleTask
        fields = ('id', 'task_type', 'chat_id')


class TaskTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskType
        fields = ('id', 'name', 'period')
