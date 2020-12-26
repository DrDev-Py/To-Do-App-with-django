from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    task = forms.CharField(label="Create a New Task")

    class Meta:
        model = Task
        fields= ['task']
