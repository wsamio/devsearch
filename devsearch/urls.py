from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', projects, name="projects"),
    path('projects1/<str:pk>/', project1, name="Single"),
]
