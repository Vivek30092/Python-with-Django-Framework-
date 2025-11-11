"""
URL configuration for project01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
# to connect views to url
from . import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home),
    path('entry1/',views.entry1),
    path('entry2/',views.entry2),
    path('entry3/',views.entry3),
    path('entry4/',views.entry4),
    
]
