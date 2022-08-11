from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import Experts, Course, Contact

class ExpertsAdmin( admin.ModelAdmin ):
    list_display = ( 'id' , 'first_name', 'last_name', 'role', 'display_about_page')
    list_display_links  = ( 'first_name', 'id')
    search_fields = ('first_name', 'role')
    list_filter = ( 'role', 'display_about_page')

admin.site.register(Experts, ExpertsAdmin)


class CourseAdmin( admin.ModelAdmin ):
    
    def display_photo( self, obj ):
        return format_html( '<img src="{}" width="100" border="0" />'.format(obj.photo.url) )
        
    list_display = ( 'id', 'display_photo', 'course_name', 'fee', 'display')
    list_display_links  = ( 'course_name', 'id')
    search_fields = ('course_name',)
    list_filter = ( 'course_name', 'duration')
    list_editable = ('display', ) 

admin.site.register(Course, CourseAdmin)



class ContactAdmin( admin.ModelAdmin ):
    
    list_display = ( 'id', 'first_name', 'last_name', 'subject')
    list_display_links  = ( 'id',)
    search_fields = ('subject','first_name', 'last_name')
    list_filter = ( 'first_name', 'last_name')

admin.site.register(Contact, ContactAdmin)