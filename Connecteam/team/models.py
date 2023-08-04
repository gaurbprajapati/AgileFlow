from django.db import models
# Assuming the Employee model is defined in a separate app named 'employee'
from employee.models import Employee


# class GlobalAdmin(models.Model):
#     admin = models.OneToOneField(
#         Employee, on_delete=models.CASCADE, related_name='global_admin')

#     def __str__(self):
#         return "Global Admin"


class Team(models.Model):
    name = models.CharField(max_length=100, null=False)
    goal = models.CharField(max_length=255, null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(Employee, related_name='teams')

    def __str__(self):
        return self.name
