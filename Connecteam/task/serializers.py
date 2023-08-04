
from rest_framework import serializers
from .models import Task, SubTask
from team.models import Team
from employee.models import Employee


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'

    def validate_assigned_to(self, value):
        task = self.context['task']
        team = task.team
        # print("Teams", team)
        employee_ids = team.members.values_list('id', flat=True)
        # print("Employee_ides", employee_ids)
        # print("Employee_ides value", value.id, value)
        if value.id not in employee_ids:
            raise serializers.ValidationError(
                "This employee is not a member of the team associated with the task.")
        return value

    # def create(self, validated_data):
    #     task = self.context['task']
    #     subtask = SubTask.objects.create(task=task, **validated_data)
    #     return subtask

    # def update(self, instance, validated_data):
    #     task = self.context['task']
    #     for attr, value in validated_data.items():
    #         setattr(instance, attr, value)
    #     instance.task = task
    #     instance.save()
    #     return instance

    # def validate_assignee(self, value):
    #     task_team = self.instance.task.team
    #     if value not in task_team.members.all():
    #         raise serializers.ValidationError(
    #             "Assignee must be a member of the task's team.")
    #     return value
