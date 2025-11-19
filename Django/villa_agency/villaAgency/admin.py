from django.contrib import admin
from villaAgency.models import SignUp
# Register your models here.

class RegSignup(admin.ModelAdmin):list_display=['name','email','mobilenumber','username','password']
admin.site.register(SignUp, RegSignup)