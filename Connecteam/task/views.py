# tasks/views.py

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task, SubTask
from .serializers import TaskSerializer, SubTaskSerializer
from team.models import Team
from employee.models import Employee
from rest_framework.permissions import IsAuthenticated, IsAdminUser



class TaskListCreateAPIView(APIView):
    
    permission_classes = [IsAdminUser]
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskRetrieveUpdateDeleteAPIView(APIView):
    
    permission_classes = [IsAdminUser]
    def get(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({"detail": "Task not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({"detail": "Task not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({"detail": "Task not found."}, status=status.HTTP_404_NOT_FOUND)

        task.delete()
        return Response({"detail": "Task deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class SubTaskListCreateAPIView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({"detail": "Task not found."}, status=status.HTTP_404_NOT_FOUND)

        subtasks = SubTask.objects.filter(task=task)
        serializer = SubTaskSerializer(subtasks, many=True)
        return Response(serializer.data)

    def post(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({"detail": "Task does not exist."}, status=status.HTTP_404_NOT_FOUND)

        serializer = SubTaskSerializer(
            data=request.data, context={'task': task})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubTaskRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, task_id, subtask_id):
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({"detail": "Task not found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            subtask = SubTask.objects.get(id=subtask_id, task=task)
        except SubTask.DoesNotExist:
            return Response({"detail": "Subtask not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = SubTaskSerializer(subtask)
        return Response(serializer.data)

    def put(self, request, task_id, subtask_id):
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({"detail": "Task not found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            subtask = SubTask.objects.get(id=subtask_id, task=task)
        except SubTask.DoesNotExist:
            return Response({"detail": "Subtask not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = SubTaskSerializer(subtask, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, task_id, subtask_id):
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({"detail": "Task not found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            subtask = SubTask.objects.get(id=subtask_id, task=task)
        except SubTask.DoesNotExist:
            return Response({"detail": "Subtask not found."}, status=status.HTTP_404_NOT_FOUND)

        subtask.delete()
        return Response({"detail": "Subtask deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
