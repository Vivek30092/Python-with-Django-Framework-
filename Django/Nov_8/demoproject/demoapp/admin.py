from django.contrib import admin

# Register your models here.

from demoapp.models import Registration

class regAdmin(admin.ModelAdmin):list_display=['emid','ename','desg','loc','salary','exp','status']
# class regAdmin(admin.ModelAdmin):list_display=['eid','ename','esal','eaddr','eunm','pw']

admin.site.register(Registration,regAdmin)
