# newemployee/views.py

from team.serializers import TeamSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import NewEmployee
from .serializers import NewEmployeeSerializer
from employee.models import Employee
from employee.serializers import EmployeeSerializer
from team.models import Team
from team.serializers import TeamSerializer


class NewEmployeeAPIView(APIView):
    def get(self, request):
        employees = NewEmployee.objects.all()
        serializer = NewEmployeeSerializer(employees, many=True)
        return Response(serializer.data)


class EmployeeDetailView(APIView):
    def get(self, request, emp_id):
        employee = NewEmployee.objects.get(id=emp_id)
        emp_detail = employee.Employee_details  # Access the related Employee object
        print(emp_detail.email)
        emp_detail_serializer = EmployeeSerializer(emp_detail)
        serializer = NewEmployeeSerializer(employee)
        return Response(emp_detail_serializer.data)


class EmployeeTeamView(APIView):
    def get(self, request):
        employee = Employee.objects.get(id=2)
        # emp_detail = employee.Employee_details  # Access the related Employee object
        team = Team.objects.all()

        serializer = TeamSerializer(team, many=True)

        # userTeam =[]
        user_id = 2
        user_team_names = []
        for team in serializer.data:
            if user_id in team["members"]:
                user_team_names.append(team)
        return Response(user_team_names)
