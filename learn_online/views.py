from django.shortcuts import render
from .models import Experts
# Create your views here.

def home(request):
    return render( request, 'home.html')

def about(request):
    all_expert = Experts.objects.filter(display_about_page=True).all()
    return render( request, 'about.html' , { 'all_expert': all_expert })

def courses(request):
    return render( request, 'courses.html')

def team(request):
    data = Experts.objects.all()
    #print(data)
    return render( request, 'team.html', { 'experts': data})

def contact(request):
    return render( request, 'contact.html')
