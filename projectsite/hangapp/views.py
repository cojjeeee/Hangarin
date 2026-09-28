from django.shortcuts import render
from django.views.generic.list import ListView
from hangapp.models import Task

# Create your views here.

class HomePageView(ListView):
    model = Task
    context_object_name = 'home'
    template_name = "home.html"