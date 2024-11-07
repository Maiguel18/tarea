from rest_framework import routers
from .api import ProjectViewSet

# Se crea una instancia de DefaultRouter, que se encargará de gestionar las rutas de la API.
routers = routers.DefaultRouter()

# Se registra el 'ProjectViewSet' con el router, lo que permite manejar las operaciones CRUD (Crear, Leer, Actualizar, Eliminar)
# para la entidad 'projects' a través de la ruta 'api/projects'.
routers.register('api/projects', ProjectViewSet, 'projects')

# Se asigna la lista de URLs generadas por el router a la variable 'urlpatterns', 
# que se utilizará para configurar las rutas de la aplicación.
urlpatterns = routers.urls