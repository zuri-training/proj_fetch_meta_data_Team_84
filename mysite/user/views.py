from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from mysite import settings

from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator

# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def signup(request):    
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists, try another")
            return redirect('home')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('home')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 characters")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "User must be Alpha-numeric!")
            return redirect('home')

        user = User.objects.create_user(username, email, pass1)
        user.first_name = fname
        user.last_name = lname
        user.is_active = False
            
        user.save()
        
        messages.success(request, "Your Account has been successfully created. Confirm your account from your email in order to create this account")

        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        
        domain = get_current_site(request).domain
        
        link = reverse('activate', kwargs={
            'uidb64':uidb64, 'token':token_generator.make_token(user)})
        
        activate_url = 'http://'+domain+link

        email_body = 'Hi '+ user.first_name + ' Please make use of this link to activate your account\n' + activate_url

        send_mail(
            'Welcome to this page',
            email_body,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
    
        return redirect('signin')
    
    return render(request, "authentication/signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html", {'fname': fname})

        else:
            messages.error(request, "Credentials Not Found")
            return redirect('home')

    return render(request, "authentication/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')


def activate (request, uidb64, token):
    
    try:
        id = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=id)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, "Your Account has been activated")
        return redirect ('signin')

    else:
        return redirect('signin')
