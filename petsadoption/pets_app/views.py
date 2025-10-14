from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            # get IDs of pets the user has favorited
            context['favorite_pet_ids'] = PetUser.objects.filter(
                user=self.request.user,
                is_favorite=True
            ).values_list('pet_id', flat=True)
        else:
            context['favorite_pet_ids'] = []
        return context

class Profile(View):
    model=User
    template_name='profile.html'
    context_object_name='user'

    def get(self, request):
        form = UserEditForm(instance=request.user)
        requests = AdoptionRequest.objects.filter(user=request.user).order_by('-requested_at')
        return render(request, self.template_name, {
            'form': form,
            'user': request.user,
            'requests': requests  # pass requests to template
        })

    def post(self, request):
        form = UserEditForm(request.POST, instance=request.user)
        requests = AdoptionRequest.objects.filter(user=request.user).order_by('-requested_at')
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        return render(request, self.template_name, {
            'form': form,
            'user': request.user,
            'requests': requests
        })

class MyPets(LoginRequiredMixin, TemplateView):
    template_name = 'my_pets.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Adopted pets (approved requests)
        context['adopted_pets'] = Pets.objects.filter(
            adoptionrequest__user=user,
            adoptionrequest__adoption_status='Approved'
        ).distinct()

        # Favorite pets
        context['favorite_pets'] = Pets.objects.filter(
            petuser__user=user,
            petuser__is_favorite=True
        ).distinct()

        return context
class AdoptRequest(ListView):  #to return to the user all of his adoption requests
    model=AdoptionRequest
    template_name='profile.html'
    context_object_name = 'requests'

    def get_queryset(self):
        return AdoptionRequest.objects.filter(user=self.request.user).order_by('-requested_at')


@login_required
def adopt_pet(request, pet_id):   #to allow the user to make an adoption request
    pet = get_object_or_404(Pets, id=pet_id)

    if AdoptionRequest.objects.filter(user=request.user, pet=pet).exists():
        messages.warning(request, f"You have already submitted a request for {pet.breed} {pet.type}.")
        return redirect('all-pets')
    
    if request.method == 'POST':
        form = AdoptionRequestForm(request.POST)
        if form.is_valid():
            adoption = form.save(commit=False)
            adoption.user = request.user
            adoption.pet = pet
            adoption.adoption_status = 'Pending'
            adoption.save()
            messages.success(request, f'Your adoption request for {pet.breed}, {pet.type} has been submitted!')
            return redirect('all-pets')
    else:
        form = AdoptionRequestForm()

    return render(request, 'adopt_pet.html', {'form': form, 'pet': pet})    


@login_required
def delete_adoption_request(request, request_id):      #to allow the user to delete the adoption request
    adoption_request = get_object_or_404(AdoptionRequest, id=request_id, user=request.user)
    adoption_request.delete()
    messages.success(request, "Your adoption request has been deleted.")
    return redirect('profile')  # or wherever you list the requests

@login_required
def toggle_favorite(request, pet_id):
    pet = get_object_or_404(Pets, id=pet_id)
    
    pet_user, created = PetUser.objects.get_or_create(user=request.user, pet=pet)
    pet_user.is_favorite = not pet_user.is_favorite  # toggle favorite
    pet_user.save()
    
    if pet_user.is_favorite:
        messages.success(request, f"{pet.type} has been added to your favorites!")
    else:
        messages.info(request, f"{pet.type} has been removed from your favorites.")
    
    return redirect('all-pets')
