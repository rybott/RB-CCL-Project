from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def main(request):
    employees = Employee.objects.all()
    return render(request, 'index.html', {'employees':employees})

def login_employee(request):
    return render(request,'login.html',{})
