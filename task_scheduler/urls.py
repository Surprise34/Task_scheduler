from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tasks_list, name='main_page'),
]
