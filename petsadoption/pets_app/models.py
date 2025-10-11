from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# My Models / tables.
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