from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 label='First Name',
                                 widget=forms.TextInput(attrs={
                                                                'placeholder': 'First Name',
                                                                'name': "first-name",
                                                                'id': "firstName",


                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={
                                                                'placeholder': 'Last Name',
                                                                'name': "last-name",
                                                                'id': "lastName",
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'id': 'username',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email Address',
                                                           'id': 'signUpEmail',
                                                           'name': "signUp-email"
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                label='Password',
                                widget=forms.PasswordInput(attrs={'placeholder': '********',
                                                                  'name': 'signUp-password',
                                                                  'id': 'signUpPassword',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                label= 'Confirm Password',
                                widget=forms.PasswordInput(attrs={'placeholder': '********',
                                                                  'name': 'signUp-password2',
                                                                  'id': 'signUpPassword2',
                                                                  }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               label='Username',
                               widget=forms.TextInput(attrs={'placeholder': 'Username',

                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               label='Password',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',

                                                                 }))
    remember_me = forms.BooleanField(required=False, label='Remember Me')

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']