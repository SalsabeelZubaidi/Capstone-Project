from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib import messages


#my Views
class LandingPage(View):
    template_name = "landing_page.html"
    
    def get(self,request):
        return render(request, self.template_name)
    
def signup(request):
    error_message = ''
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)  # built-in form for creating users
        if form.is_valid():
            user = form.save()  # save user to DB
            login(request, user)  # log the user in immediately
            return redirect('home')  # redirect to home page after signup
        else:
            error_message = 'Invalid signup - try again'
    else:
        form = CustomUserCreationForm()  # empty form for GET request
    return render(request, 'registration/signup.html', {'form': form, 'error_message': error_message})
   
@login_required
def home(request):
    return render (request, 'home.html')

class AllPets(ListView):
    model= Pets
    template_name='all_pets.html'
    context_object_name = 'pets' #this to loop over it in the html file

class Profile(View):
    model=User
    template_name='profile.html'
    context_object_name='user'

    def get(self, request):
        form = UserEditForm(instance=request.user)
        return render(request, self.template_name, {'form': form, 'user': request.user})

    
    def post(self, request):
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        return render(request, self.template_name, {'form': form , 'user': request.user})

class MyPets(ListView):
    model=PetUser
    template_name='my_pets.html'