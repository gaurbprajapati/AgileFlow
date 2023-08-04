from django.urls import path
from .views import *

urlpatterns = [

    path('roles/', AllRolesView.as_view(), name='all-role'),
    # path('add-roles/', AddRolesView.as_view(), name='add-role'),

    path('department/', AllDepartmentView.as_view(), name='AllDepartmentView'),
    # path('add-department/', AddDepartmentView.as_view(), name='AddDepartmentView'),

    path('all-employees/', AllEmployeeView.as_view(), name='all-employees'),
    path('add-employee/', AddEmployeeView.as_view(), name='add-employee'),

    # API to remove an employee by emp_id
    path('remove_emp/<int:emp_id>/',
         RemoveEmployeeView.as_view(), name='remove_employee'),

    # API to filter employees based on name, dept, and role
    path('filter_emp/', FilterEmployeeView.as_view(), name='filter_employee'),
]
