from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class Task(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    description = models.CharField(verbose_name='Описание', max_length=200)
    author = models.ForeignKey(
        verbose_name = 'Пользователь',
        to=User,
        null=True,
        on_delete = models.CASCADE
    )
    created_date = models.DateTimeField(default=timezone.now)
    duration = models.DurationField(default=timedelta(seconds=30))
    is_done=models.BooleanField(default=False)

    class Meta:
        ordering = ('title', 'author',)
        verbose_name='Заголовок'
        verbose_name_plural='Заголовки'

    def __str__(self):
        return self.title
