import email
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login
from .form import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.

def signup(request):
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form=SignupForm
    return render(request, 'signup.html', {'form':form})

def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        
        password=request.POST['login-password']
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'you are welcome')
            return render(request, 'dashboard.html', {'username':username} )
        else:
            messages.error(request, 'you have entered the wrong detail')
            return redirect('signin')

    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html' )

