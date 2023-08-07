# Generated by Django 3.2.5 on 2023-08-07 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtask',
            name='task',
        ),
        migrations.AddField(
            model_name='task',
            name='subtask',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='task.subtask'),
            preserve_default=False,
        ),
    ]