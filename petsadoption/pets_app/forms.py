from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
      # add extra field if you want

    class Meta:
        model = User
        # Only show these fields in the form
        fields = ("username", "first_name", "last_name", "password1", "password2")


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", 'first_name', 'last_name']    