from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    page = 'projects'
    return  render(request, 'projects/projects.html', {'page': page})

def project(request, pk):
    return  render(request, 'projects/single-project.html')