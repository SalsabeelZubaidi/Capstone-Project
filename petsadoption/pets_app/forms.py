from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import AdoptionRequest

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


class AdoptionRequestForm(forms.ModelForm):
    class Meta:
        model = AdoptionRequest
        fields = ['care_plan']
        widgets = {
            'care_plan': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe how you’ll take care of the pet...'}),
        }

class PetNameForm(forms.ModelForm):
    class Meta:
        model = AdoptionRequest
        fields = ['pet_name']
        widgets = {
            'pet_name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your pet’s new name'
            })
        }                    