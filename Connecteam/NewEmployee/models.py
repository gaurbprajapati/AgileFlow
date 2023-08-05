# NewEmployee/models.py

from django.db import models

from employee.models import Employee


class NewEmployee(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    Employee_details = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
