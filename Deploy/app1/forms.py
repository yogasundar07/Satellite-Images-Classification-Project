from django import forms
from .models import UserImageModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import UserImageModel

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserImageForm(forms.ModelForm):

    class Meta:
        model = UserImageModel
        fields = ['image']