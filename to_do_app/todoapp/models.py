from django.db import models


class Tasks(models.Model):
    task = models.CharField(max_length=100)
    task_done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.task} <---> {self.task_done}'
