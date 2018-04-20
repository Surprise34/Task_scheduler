"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views as mysite_views
from django.conf.urls import url,include
import task_scheduler.urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('login/', auth_views.login, {'template_name':'login.html'},name='login' ),
    path('logout/',auth_views.logout,{'template_name':'logged_out.html'}, name='logout'),
    path('signup/',mysite_views.signup, name='signup'),    
    path('admin/', admin.site.urls),
    url(r'^', include (task_scheduler.urls)),
]

urlpatterns += staticfiles_urlpatterns()
