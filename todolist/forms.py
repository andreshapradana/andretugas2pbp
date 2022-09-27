from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('user', 'date', 'title', 'description')
        exclude = ['user', 'date']
    