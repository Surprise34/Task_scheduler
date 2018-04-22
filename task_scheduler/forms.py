from django import forms
from .models import Task
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'duration')
        widgets = {
            'description' : forms.Textarea(attrs = {'cols' :  45 , 'rows' : 4}),
        }
        
        
    
    
