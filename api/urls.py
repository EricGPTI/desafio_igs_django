from django.contrib import admin
from django.urls import path
from api import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('employees/', views.get_employees, name='employees'),
    path('employees/<int:pk>', views.delete_employee, name='employee'),
]
