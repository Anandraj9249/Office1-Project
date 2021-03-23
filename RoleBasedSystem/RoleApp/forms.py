from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Admin, User, Sub_Admin, AdminAdditional
from django import forms
from django.core.validators import RegexValidator

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Seller
        fields = [
            'email',
            'name',
            'password1',
            'password2',
        ]