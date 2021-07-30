from django.db import models


class ScheduleTask(models.Model):
    task_type = models.ForeignKey(
        'TaskType',
        related_name='task_types',
        on_delete=models.PROTECT,
        default=None,
    )
    chat_id = models.BigIntegerField(default=None)

    def __str__(self):
        return f'Chat: {self.chat_id}'


class TaskType(models.Model):
    name = models.CharField(max_length=255, default='Not defined')
    period = models.CharField(max_length=255, default='Unknown')

    def __str__(self):
        return self.name
