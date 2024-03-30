from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from . import models
from django import forms


class UserCreationForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ['username', 'email', 'login', 'password1', 'password2']


class UserEditForm(ModelForm):
    class Meta:
        model = models.User
        fields = ['username', 'email', 'login', 'avatar']
        widgets = {
            'avatar': forms.FileInput(attrs={'accept': 'image/*,.png,.jpg'}),
        }
