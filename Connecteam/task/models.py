from django.db import models

# Create your models here.
from django.db import models
from team.models import Team
from employee.models import Employee


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='tasks')
    status_choices = [
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed')
    ]
    status = models.CharField(
        max_length=20, choices=status_choices, default='Not Started')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SubTask(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='subtasks')
    assigned_to = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='assigned_subtasks')
    status_choices = [
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed')
    ]
    status = models.CharField(
        max_length=20, choices=status_choices, default='Not Started')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
