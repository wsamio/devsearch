from django.http import JasonResponse

def getRoutes(request):

    routes = [
        {'GET':'/api/projects'},
        {'GET':'/api/projects/id'},
        {'POST':'/api/projects/id/vote'},
        
        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},
    ]

    return JasonResponse(routes)