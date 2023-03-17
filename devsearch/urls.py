from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def projects(request):
    return  HttpResponse('Here are our products')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', projects, name="projects"),
]
