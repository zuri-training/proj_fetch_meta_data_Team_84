from django.urls import path, reverse_lazy
from django.views.generic import TemplateView
from .views import RegisterPage, CustomLoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from .views import upload

app_name = 'meta'

urlpatterns = [
    path('', TemplateView.as_view(template_name='meta/index.html'), name='index'),
    path('dashboard/', upload, name='dashboard'),
    path('about-us/', TemplateView.as_view(template_name='meta/about-us.html'), name='about-us'),
    path('faqs/', TemplateView.as_view(template_name='meta/faqs.html'), name='faqs'),
    path('contact-us/', TemplateView.as_view(template_name='meta/contact-us.html'), name='contact-us'),
    path('signup/', RegisterPage.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='meta:index'), name='logout'),

    # Change Password

    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='password/change-password.html',
            success_url='/'  # use this for home page
        ),
        name='change_password'
    ),

    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password/password_reset_confirm.html',
             subject_template_name='password/password_reset_subject.txt',
             email_template_name='password/password_reset_email.html',
             success_url=reverse_lazy('meta:password_reset_done')
         ),
         name='password-reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password/password_reset_confirm.html',
             success_url=reverse_lazy('meta:password_reset_complete')
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
            template_name='password/password_reset_complete.html',
         ),
         name='password_reset_complete'),

]