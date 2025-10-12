from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# My Models / tables.

User = get_user_model()   #built in user model

class Pets(models.Model):
    name=models.CharField(max_length=100)
    breed=models.CharField(max_length=100)
    age=models.IntegerField()
    description=models.TextField()
    photo=models.ImageField(upload_to='pet_photos/', blank=True, null=True)
    is_available=models.BooleanField(default=True)
    adoption_status=models.CharField(max_length=100)   

    def __str__(self):   #to retrun the object name /// pet name // return object val as String
        return self.name 

class PetUser(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    pet=models.ForeignKey(Pets,on_delete=models.CASCADE)
    is_favorite=models.BooleanField(default=True)
    applied_at=models.DateField(auto_now=True)

    def __str__(self):   
        return f"{self.user.username} - {self.pet.name}"    


class AdoptionRequest(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    pet=models.ForeignKey(Pets,on_delete=models.CASCADE)
    adoption_status=models.CharField(max_length=100)
    requested_at=models.DateField(auto_now=True)
    commitment=models.BooleanField(default=True)
    care_plan=models.TextField()

    def __str__(self):  
        return f"{self.user.username} - {self.pet.name}"  


