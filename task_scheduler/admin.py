from django.contrib import admin
from . models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',  'author', 'created_date',  'duration', 'is_done')
    list_select_related=('author', )

admin.site.register(Task, TaskAdmin)
