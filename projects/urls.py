from rest_framework import routers
from .api import ProjectViewSet

# Create an instance of the DefaultRouter provided by Django Rest Framework
router = routers.DefaultRouter()

# Associate the ProjectViewSet with the 'api/projects' route
# Utilize 'projects' as the assigned route name for referencing
router.register('api/projects', ProjectViewSet, 'projects' ) 

urlpatterns = router.urls
