from django.shortcuts import render, HttpResponse
from api.models import Employee, Department
from api.serializer import EmployeeSerializer, DepartmentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def employees(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

#@api_view(['POST'])
#def employees(requests):
#    if request.method == 'POST':
#        data = request.data
#        department = Department.objects.get(id=data['department_id'])
#        if department is None:
#            return Response(status=status.HTTP_400_BAD_REQUEST)
#        employee = Employee(name=data['name'].Capitalize(), email=data['email'].lower(), data['department'])
#        user = (data['name'], data['email'], data['department'])
#