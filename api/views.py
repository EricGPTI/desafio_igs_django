from django.shortcuts import render, HttpResponse

# Create your views here.

def employees(requests):
    return HttpResponse("Estou on")