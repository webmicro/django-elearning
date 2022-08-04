from pyexpat import model
from tokenize import blank_re
from django.db import models

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
