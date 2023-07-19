from django import forms
from .models import Tasks


class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['task', 'task_done']