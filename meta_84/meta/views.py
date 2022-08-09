from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from .forms import RegisterForm, LoginForm
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView


# Create your views here.


class RegisterPage(FormView):
    template_name = 'signup.html'
    form_class = RegisterForm  # django form
    success_url = reverse_lazy('meta:landing')

    def form_valid(self, form):
        user = form.save()
        if user is not None:  # if user is authenticated log in the user!
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    # we need to prevent authenticated user from registering!

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('meta:landing')  # this is the page it will return instead of signing up
        return super(RegisterPage, self).get(*args, **kwargs)


class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    form_class = LoginForm
    redirect_authenticated_user = True  # if user is authenticated they should not be allowed to be in the login page

    def get_success_url(self):  # use this function whenever you need success url in login
        return reverse_lazy('meta:landing')
