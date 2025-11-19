from django.contrib import admin
from firstApp.models import student

# Register your models here.

class RegAdmin(admin.ModelAdmin):list_display=[ 'sid', 'sname' ,'sfees','saddr','sunm','pw'] 
    
admin.site.register(student,RegAdmin)