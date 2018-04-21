from django import forms
from .models import Task
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    title_raw=forms.CharField(label='Название задачи',max_length=100)
    description_raw=forms.CharField(label='Описание задачи',widget = forms.Textarea(attrs = {'class': 'form-control'}),max_length=200)
    duration_raw=forms.DurationField(label='Время выполнения(в формате "hh:mm:ss"). По умолчанию равно 30 сек.',required=False)
    
