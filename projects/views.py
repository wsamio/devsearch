from django.shortcuts import render

from django.http import HttpResponse

def projects(request):
    return  HttpResponse('Here are our products')

def project1(request, pk):
    return  HttpResponse('SINGLE PROJECTS' + ' ' + str(pk))