from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from .models import Experts, Contact, Course
# Create your views here.

def home(request):
    return render( request, 'home.html')

def about(request):
    all_expert = Experts.objects.filter(display_about_page=True).all()
    return render( request, 'about.html' , { 'all_expert': all_expert })

def courses(request):
    all_course = Course.objects.filter( display=True).order_by('-course_name')

    return render( request, 'courses.html', {'all_course': all_course} )

def team(request):
    data = Experts.objects.all()
    #print(data)
    return render( request, 'team.html', { 'experts': data})

def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        con_obj = Contact(first_name=first_name, last_name=last_name, email=email, subject=subject, message=message )
        con_obj.save()
        messages.success(request, "Message sent successfully!")
        return redirect('/contact')

    else:
        return render( request, 'contact.html')

def sign(request):
    return render(request, 'signup.html')


def course_detail( request, id ):
    cdata = get_object_or_404( Course, pk = id )    
    return render(request, 'course-detail.html', {'course': cdata})