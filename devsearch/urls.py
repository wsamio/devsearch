from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def projects(request):
    return  HttpResponse('Here are our products')

def project1(request):
    return  HttpResponse('SINGLE PROJECTS')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', projects, name="projects"),
    path('projects1/', project1, name="Single"),
]
