from django.contrib import admin
from .models import Pets, AdoptionRequest

# Register your models here // to be able to access them from admin panel
admin.site.register(Pets)
admin.site.register(AdoptionRequest)



