from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from .models import Experts, Contact, Course
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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

    if request.method == 'POST':
        
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        conf_password = request.POST['conf_password']
        is_error = False
        if password != conf_password :
           messages.error( request , 'Both password should be same') 
           is_error = True

        if User.objects.filter(email=email).exists() :
            messages.error( request , 'You are already registered') 
            is_error = True

        if User.objects.filter(username=username).exists() :
            messages.error( request , 'Username already exists') 
            is_error = True    

        if is_error == False:
            obj_user = User.objects.create_user(username=username, password=password, email=email, first_name = fname, last_name= lname  )
            obj_user.save()
            user = authenticate(request, username=username, password=password, email=email, first_name = fname, last_name= lname)
            if user is not None :
                login( request, user )
                return redirect('/home')
            else:
                messages.error( request , 'Wrong credential')

    return render(request, 'signup.html')

def my_login( request ):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        is_error = False
        
        user = authenticate( request, username=username, password=password)
        if user is not None :
            login( request, user )  
            return redirect('/home')            
        else:
            messages.error( request , 'Wrong username or password') 

    return render(request, 'login.html')

def course_detail( request, id ):
    cdata = get_object_or_404( Course, pk = id )    
    return render(request, 'course-detail.html', {'course': cdata})

def my_logout( request ):
    logout( request )
    return redirect('/')       
     