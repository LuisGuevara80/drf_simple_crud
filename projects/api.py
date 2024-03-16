from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet): 
    queryset = Project.objects.all() 
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer

# This class creates a flexible API endpoint (ProjectViewSet) for managing Project model data.
# It supports Create, Read, Update, and Delete operations
# and uses ProjectSerializer to convert data to and from JSON format effortlessly.
