from rest_framework import serializers
from api.models import User, Employee, Department


class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    name = serializers.CharField(max_length=100)
    email  = serializers.EmailField(max_length=60)

    class Meta:
        model = Employee
        fields = ('name', 'email', 'department')


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('department', 'employees')
