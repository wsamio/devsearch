from django.shortcuts import render
from django.http import HttpResponse

project_list = [
    {
        'id' : '1',
        'title' : "Ecommerce Website",
        'description' : 'Fully functional eccomerce website'
    },
    {
        'id' : '2',
        'title' : "Portfolio Website",
        'description' : 'This was a project where I built out my portfolio'

    },
]

def projects(request):
    page = 'projects'
    number = 10
    context = {'page' : page, 'number': number, 'projects' : project_list}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = None
    for i in project_list:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project' : projectObj})