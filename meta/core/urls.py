from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'core'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='core:login'), name='logout'),
    path('core/', views.Core.as_view(), name='core'),
    path('dashboard/', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),

]
