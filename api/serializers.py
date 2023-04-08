from rest_framework import serializers
from projects.models import Project

class ProjectSerializers(serializers.ModelSerializers):
    class Meta:
        model = Project
        fields = '__all__'
