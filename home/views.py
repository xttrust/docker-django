# home/views.py
from django.shortcuts import render

def home(request):
    context = {
        'title': 'Home Page',
        'content': 'Welcome to the Home Page'
    }
    return render(request, 'home/home.html', context)
