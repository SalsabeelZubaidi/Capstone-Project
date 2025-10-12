from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required


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