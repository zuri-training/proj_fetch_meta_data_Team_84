from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.contrib.auth import views as auth_views

# app_name = 'meta'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
     path('dashboard/', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),

    path('password_reset/',auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]