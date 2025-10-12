from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # add extra field if you want

    class Meta:
        model = User
        # Only show these fields in the form
        fields = ("username", "first_name", "last_name", "password1", "password2")
