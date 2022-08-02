from django.shortcuts import render
from .models import Experts
# Create your views here.

def home(request):
    return render( request, 'home.html')

def about(request):
    return render( request, 'about.html')

def courses(request):
    return render( request, 'courses.html')

def team(request):
    data = Experts.objects.all()
    #print(data)
    return render( request, 'team.html', { 'experts': data})

def contact(request):
    return render( request, 'contact.html')
