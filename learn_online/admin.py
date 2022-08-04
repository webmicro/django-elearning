from django.contrib import admin

# Register your models here.
from .models import Experts

class ExpertsAdmin( admin.ModelAdmin ):
    list_display = ( 'id' , 'first_name', 'last_name', 'role', 'display_about_page')
    list_display_links  = ( 'first_name', 'id')
    search_fields = ('first_name', 'role')
    list_filter = ( 'role', 'display_about_page')

admin.site.register(Experts, ExpertsAdmin)