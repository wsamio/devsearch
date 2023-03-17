from django.urls import path

urlpatterns = [
    path('projects/', projects, name="projects"),
    path('projects1/<str:pk>/', project1, name="Single"),
]