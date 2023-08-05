# newemployee/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('newemployees/', NewEmployeeAPIView.as_view(), name='new_employee_list'),
    path('newemployees/<int:emp_id>/',
         EmployeeDetailView.as_view()),
    path('newemployees/team/<int:emp_id>/',
         EmployeeTeamView.as_view()),
]
