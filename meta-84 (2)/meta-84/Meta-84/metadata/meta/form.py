from dataclasses import fields
import email
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignupForm(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length=45)
    last_name=forms.CharField(max_length=45)

    class Meta:
        model=User
        fields=('username','first_name', 'last_name','email', 'password1', 'password2')
    