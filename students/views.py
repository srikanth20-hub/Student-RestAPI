from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def students(request):
    students = [
        {'id': 1,'name': 'Ravi', 'Email':'ravi@gmail.com','age':45}
    ]
    return HttpResponse(" <h1>Hello Ravi</h1>")