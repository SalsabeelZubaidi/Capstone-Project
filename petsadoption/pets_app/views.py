from django.shortcuts import render
from django.http import HttpResponse


#my Views

def home(request):
    return HttpResponse("<h1> HOME SCREEN </h1>")

