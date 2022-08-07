from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm  # register
from django.contrib.auth import login
from django.urls import reverse_lazy

# Create your views here.


class RegisterPage(FormView):
    template_name = 'signup.html'
    form_class = RegisterForm  # django form
    success_url = reverse_lazy('core:core')

    def form_valid(self, form):
        user = form.save()
        if user is not None:  # if user is authenticated log in the user!
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    # we need to prevent authenticated user from registering!

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('core:core')  # this is the page it will return instead of signing up
        return super(RegisterPage, self).get(*args, **kwargs)


class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True  # if user is authenticated they should not be allowed to be in the login page

    def get_success_url(self):  # use this function whenever you need success url in login
        return reverse_lazy('core:core')


class Core(LoginRequiredMixin, View):  # must log in before viewing this page!
    login_url = '/login/'  # it will redirect here if the user is not logged in

    def get(self, request):
        context = {}
        return render(request, 'core.html', context)

class dashboard():
    dashboard_url = '/dashboard/'

    def get(self, request):
        context = {}
        return render(request, 'dashboard.html', context)
     
