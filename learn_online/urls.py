from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('courses', views.courses, name='courses'),
    path('team', views.team, name='team'),
    path('contact', views.contact, name='contact'),
    path('sign', views.sign, name='signup')
]

