from typing import Any
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Employee



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Re-enter Password'


class EmplProfileForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'fname',
            'lname',
            'phone',
            'age',
            'dob',
            'hispanic',
            'ethnicity',
            'gender',
            'orientation',
            'us_citizenship',
            'non_citizen',
            'gross_income',
        ]
        widgets = {
            'fname': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'lname': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age', 'min': '0'}),
            'dob': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Date of Birth'}),
            'hispanic': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ethnicity': forms.Select(attrs={'class': 'form-select'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'orientation': forms.Select(attrs={'class': 'form-select'}),
            'us_citizenship': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'non_citizen': forms.Select(attrs={'class': 'form-select'}),
            'gross_income': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Additional initial setup if needed
        self.fields['dob'].widget.attrs['max'] = '2005-12-31'  # Example to restrict DOB for age limits