# tasks/urls.py

from django.urls import path
from .views import (
    TaskListCreateAPIView,
    TaskRetrieveUpdateDeleteAPIView,
    SubTaskListCreateAPIView,
    SubTaskRetrieveUpdateDeleteAPIView,
)

urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view()),
    path('tasks/<int:task_id>/', TaskRetrieveUpdateDeleteAPIView.as_view()),
    path('tasks/<int:task_id>/subtasks/', SubTaskListCreateAPIView.as_view()),
    path('tasks/<int:task_id>/subtasks/<int:subtask_id>/',
         SubTaskRetrieveUpdateDeleteAPIView.as_view()),
]
