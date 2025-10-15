from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views 

urlpatterns = [
    path('', views.LandingPage.as_view() , name='landing'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('pets/', views.AllPets.as_view(), name='all-pets'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('my-pets/', views.MyPets.as_view(), name='my-pets'),
    path('adopt/<int:pet_id>/', views.adopt_pet, name='adopt_pet'),
    path('delete_request/<int:request_id>/', views.delete_adoption_request, name='delete_request'),
    path('toggle_fav/<int:pet_id>/', views.toggle_favorite, name='toggle_fav'),
    path('name-pet-inline/<int:adoption_id>/', views.name_pet_inline , name='name-pet-inline'),


]