from django.shortcuts import render
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone

# Create your views here.

def index(request):
    return render(request, 'index.html')

def tasks_list(request):
    if request.user.is_authenticated:
        tasks_list = Task.objects.filter(author=request.user).order_by('created_date')
        return render(
            request, 'index.html', {
                'tasks':tasks_list,
            }
        )
    else:
        return index(request)

@login_required
def task_detail(request , task_id):
    try:
        task = Task.objects.select_related('author').get(id=task_id)
    except Task.DoesNotExist:
        raise Http404
    if request.user != task.author:
        raise Http404
    return render(
        request, 'task_detail.html',{
            'task':task,
            'user':user
        }
    )

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            title_raw = form.cleaned_data['title_raw']
            description_raw = form. cleaned_data['description_raw']
            author1 = request.user
            if form.cleaned_data['duration_raw']!=None:
                t = Task(
                    title=title_raw,
                    description=descriprion_raw,
                    author=author1,
                    duration=form.cleaned_data['duration_raw'],
                )
            else:
                t = Task(
                    title=title_raw,
                    description=descriprion_raw,
                    author=author1,
                )
            t.save()
            return render(request, 'index.html')
    else:
        form = TaskForm()
    return render (
        request, 'task_create.html', {
            'form' : form,
        }
    )


            
            
        
            
            
            
            








    
