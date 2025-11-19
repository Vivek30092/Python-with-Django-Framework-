from django.contrib import admin
from shopApp.models import Customers
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):list_display=['cname','cadd','phone','email','unm','pw']

admin.site.register(Customers,CustomerAdmin)