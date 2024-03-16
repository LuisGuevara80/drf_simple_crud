from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer): # Converts the model into data that can be queried
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'technology', 'created_at') #  Fields to include in the response
        read_only_fields = ('created_at', )
        # added the , so that it considers it a tuple