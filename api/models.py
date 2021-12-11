from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField


class Department(models.Model):
    id = models.IntegerField(primary_key=True, AutoField=True, unique=True)
    department = models.CharField(max_length=30)


class Employees(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, AutoField=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department_id = models.ForeignKey(Department, on_delete=CASCADE)
