from django.apps import AppConfig

# La clase 'ProjectsConfig' es una configuración de la aplicación Django llamada 'projects'.
# Se utiliza para definir configuraciones específicas de la aplicación y su comportamiento dentro del proyecto.
class ProjectsConfig(AppConfig):
    # 'default_auto_field' establece el tipo de campo que se utilizará por defecto para los campos de clave primaria
    # en los modelos de esta aplicación. 'BigAutoField' permite manejar un rango más amplio de valores.
    default_auto_field = 'django.db.models.BigAutoField'
    
    # 'name' especifica el nombre de la aplicación, que es 'projects'. Este nombre se utiliza para referirse
    # a la aplicación dentro del proyecto Django.
    name = 'projects'