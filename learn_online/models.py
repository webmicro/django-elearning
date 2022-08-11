from asyncio.windows_events import NULL
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Experts (models.Model):
    first_name = models.CharField( max_length= 64 )
    last_name = models.CharField( max_length= 64 )
    role = models.CharField( max_length=64)
    fb_url = models.URLField( max_length =255, null= True, blank=True )
    tw_url = models.URLField( max_length =255, null= True, blank=True )
    ins_url = models.URLField( max_length =255, null= True, blank=True )
    photo = models.ImageField( upload_to = "expert_pics/", null = True )
    display_about_page = models.BooleanField( default = False )

    def __str__( self ):
        return self.first_name

class Course ( models.Model ):

    no_students = (
        (5, '5 Students'),
        (10, '10 Students'),
        (15, '15 Students'),
        (20, '20 Students'),
        (25, '25 Students'),
        (30, '30 Students')
    )
    course_name = models.CharField( max_length= 128)
    fee = models.FloatField( max_length=20)
    duration =  models.CharField(max_length=100)
    total_student =  models.IntegerField( choices=no_students)
    trainer = models.CharField( max_length=100)
    photo = models.ImageField( upload_to = "courses/")
    description = RichTextField()
    display = models.BooleanField( default=True)


class Contact (models.Model):
    first_name = models.CharField( max_length= 64 )
    last_name = models.CharField( max_length= 64 )
    email = models.CharField( max_length= 64, default=NULL )
    subject = models.CharField( max_length=128)
    message = models.TextField()

