from rest_framework import serializers
from .models import Department, Role, Employee


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    dept = DepartmentSerializer()
    role = RoleSerializer()

    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        dept_data = validated_data.pop('dept')
        role_data = validated_data.pop('role')

        # Create the Department instance
        department = Department.objects.create(**dept_data)

        # Create the Role instance
        role = Role.objects.create(**role_data)

        # Create the Employee instance and associate the Department and Role
        employee = Employee.objects.create(
            dept=department, role=role, **validated_data)
        return employee
