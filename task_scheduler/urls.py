from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.tasks_list, name='main_page'),
    re_path(r'^task/detail/(?P<task_id>\d+)$',views.task_detail, name='task_detail'),
    re_path(r'^task/create/', views.task_create, name='task_create'),    
]
