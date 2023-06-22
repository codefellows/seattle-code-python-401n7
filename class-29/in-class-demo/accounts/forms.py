from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# we need to link our form to our custom user model
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email", "birthday")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email", "birthday")

