from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.utils.translation import gettext_lazy as _, ngettext_lazy

class UserRegisterForm(UserCreationForm):
    """ The form responsible for user registration. """
    
    email = forms.EmailField(
        label= 'Email',
        required=True,
    )

    username = forms.CharField(
        max_length=40, 
        required=True,
        label='Username'
    )

    first_name = forms.CharField(
        required=True,
        label='First Name'
    )

    last_name = forms.CharField(
        required=True,
        label='Last Name'
    )

    # Initial password input
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        label='Password'
    )
    
    # Confirm password input
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        label='Confirm Password'
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    """ The form responsible for updating user information. """
    
    email = forms.EmailField(
        label='Email',
        required=True
    )

    username = forms.CharField(
        required=True,
        label='Username',
    )

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """ The form responsible for updating user profile information. """
    
    image = forms.ImageField(
        label = 'Profile Picture'
    )
    
    about = forms.CharField(
        label = 'About you',
        required=False,
    )

    class Meta:
        model = Profile
        fields = ['image', 'about']