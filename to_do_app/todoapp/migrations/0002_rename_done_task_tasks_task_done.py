# Generated by Django 4.2.3 on 2023-07-17 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='done_task',
            new_name='task_done',
        ),
    ]
