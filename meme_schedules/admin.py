from django.contrib import admin
from .models import TaskType, ScheduleTask


admin.site.register(TaskType)
admin.site.register(ScheduleTask)
