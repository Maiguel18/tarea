from rest_framework import serializers
from .models import Project

# Se define un serializador para el modelo 'Project', que permite convertir instancias del modelo
# a formatos como JSON y viceversa, facilitando la interacción con la API.
class ProjectSerializer(serializers.ModelSerializer):
    # La clase Meta se utiliza para especificar el modelo y los campos que se incluirán en el serializador.
    class Meta:
        # Se indica que el modelo a serializar es 'Project'.
        model = Project
        
        # Se definen los campos que se incluirán en la representación del modelo.
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        
        # Se establece que el campo 'created_at' es de solo lectura, lo que significa que no se puede modificar
        # al crear o actualizar una instancia del proyecto a través del serializador.
        read_only_fields = ('created_at', )