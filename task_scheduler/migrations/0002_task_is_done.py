# Generated by Django 2.0.4 on 2018-04-21 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]
