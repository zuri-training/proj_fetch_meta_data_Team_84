from django.urls import path
from django.views.generic import TemplateView
from .views import RegisterPage, CustomLoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

app_name = 'meta'

urlpatterns = [
    path('', TemplateView.as_view(template_name='meta/landing.html'), name='landing'),
    path('about-us/', TemplateView.as_view(template_name='meta/about.html'), name='about-us'),
    path('faqs/', TemplateView.as_view(template_name='meta/faqs.html'), name='faqs'),
    path('contact-us/', TemplateView.as_view(template_name='meta/contact-us.html'), name='contact-us'),
    path('signup/', RegisterPage.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='meta:landing'), name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uid64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')




]