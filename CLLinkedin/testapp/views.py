from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import CreateUserForm, EmplProfileForm

def main(request):
    employees = Employee.objects.all()
    return render(request, 'hp.html')



def register_employee(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new User instance

            # Create an Employee instance for the new user
            Employee.objects.create(user=user)

            # Optionally, log the user in after registration
            login(request, user)

            # Redirect to profile completion or home page
            return redirect('../complete_profile')  # Direct to complete profile after registration
    else:
        form = CreateUserForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def login_employee(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)

                # Check if the user profile is complete
                try:
                    profile = EmplProfileForm.objects.get(user=user)
                    if profile.is_complete():
                        return redirect('../')
                    else:
                        return redirect('complete_profile') 
                except EmplProfileForm.DoesNotExist:
                    return redirect('complete_profile')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'loginn.html', context)

def complete_profile(request):
    employee = request.user.employee
    form = EmplProfileForm(instance=employee)

    if request.method == 'POST':
        form = EmplProfileForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            # Optionally redirect to a success page
            return redirect('profile_success')

    return render(request, 'complete_employee.html', {'form': form})