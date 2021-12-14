from django.db.models.fields import SlugField
from rest_framework import fields, serializers
from api.models import User, Employee, Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'department')


class EmployeeSerializer(serializers.ModelSerializer):
    # department = serializers.SlugRelatedField(
    #     many=False,
    #     read_only=True,
    #     slug_field='department'
    #     )

    class Meta:
        model = Employee
        fields = ('id', 'name', 'email', 'department')
