from api.models import Employee, Department
from api.serializer import EmployeeSerializer, DepartmentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers


@api_view(['GET', 'POST'])
def get_employees(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        request_department = request.data.get('department')
        department = Department.objects.get(department=request_department)
        request.data['department'] = department.id
        employee = EmployeeSerializer(data=request.data)
        if employee.is_valid():
            employee.save()
            return Response(employee.data, status=status.HTTP_201_CREATED)
    return Response(serializers.ErrorDetail, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_employee(request, pk, format=None):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    employee.delete()
    return Response(status=status.HTTP_200_OK)
