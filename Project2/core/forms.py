from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-',
    }))

    
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-',
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-',
    }))

    
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-',
    }))

    
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-',
    }))

    
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Repeat your password',
        'class': 'w-full py-4 px-6 rounded-',
    }))