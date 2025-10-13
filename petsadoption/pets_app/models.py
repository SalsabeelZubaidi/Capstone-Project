from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# My Models / tables.

User = get_user_model()   #built in user model

adoption_status_options=[
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('rejected', 'Rejected'),
    ]   

class Pets(models.Model):
    type=models.CharField(max_length=100)
    breed=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='pet_photos/', blank=True, null=True)
    is_available=models.BooleanField(default=True)
    adoption_status = models.CharField(max_length=10, choices=adoption_status_options, default='pending')
    def __str__(self):   #to retrun the object name /// pet name // return object val as String
        return self.type

class PetUser(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    pet=models.ForeignKey(Pets,on_delete=models.CASCADE)
    is_favorite=models.BooleanField(default=True)
    applied_at=models.DateField(auto_now=True)

    def __str__(self):   
        return f"{self.user.username} - {self.pet.type}"    


class AdoptionRequest(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    pet=models.ForeignKey(Pets,on_delete=models.CASCADE)
    adoption_status=models.CharField(max_length=100)
    requested_at=models.DateField(auto_now=True)
    commitment=models.BooleanField(default=True)
    care_plan=models.TextField()

    def __str__(self):  
        return f"{self.user.username} - {self.pet.type}"  


