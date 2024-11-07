from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

# Define la clase ProjectViewSet que hereda de ModelViewSet
class ProjectViewSet(viewsets.ModelViewSet):
    # Define el conjunto de consultas que se utilizará para la vista, en este caso, todos los objetos de Project
    queryset = Project.objects.all()
    # Define las clases de permisos; en este caso, se permite el acceso a cualquier usuario
    permission_classes = [permissions.AllowAny] 
    # Define el serializador que se utilizará para validar y serializar los datos del modelo Project
    serializer_class = ProjectSerializer 