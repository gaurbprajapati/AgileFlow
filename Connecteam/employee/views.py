from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee, Role, Department
from .serializers import EmployeeSerializer, RoleSerializer, DepartmentSerializer
from django.db.models import Q

# Create your views here.


class AllRolesView(APIView):
    def get(self, request):
        role = Role.objects.all()
        serializer = RoleSerializer(role, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# class AddRolesView(APIView):


    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'message': 'Role added Successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AllDepartmentView(APIView):
    def get(self, request):
        role = Department.objects.all()
        serializer = DepartmentSerializer(role, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# class AddDepartmentView(APIView):

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'message': 'Role added Successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AllEmployeeView(APIView):
    def get(self, request):
        emps = Employee.objects.all()
        serializer = EmployeeSerializer(emps, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddEmployeeView(APIView):
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'message': 'Employee added Successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response({'detail': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class RemoveEmployeeView(APIView):
    def get(self, request, emp_id=0):
        if emp_id:
            try:
                emp_to_be_removed = Employee.objects.get(id=emp_id)
                emp_to_be_removed.delete()
                return Response({"message": "Employee Removed Successfully"})
            except Employee.DoesNotExist:
                return Response({"error": "Please Enter A Valid EMP ID"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Please Enter A Valid EMP ID"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, emp_id=0):
        return Response({"detail": "Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class FilterEmployeeView(APIView):
    def post(self, request):
        name = request.data.get('name')
        dept = request.data.get('dept')
        role = request.data.get('role')
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name)
                               | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)

        serializer = EmployeeSerializer(emps, many=True)
        return Response(serializer.data)

    def get(self, request):
        return Response({"detail": "Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
