from django.db import models

# Create your models here.
class Project(models.Model):
    #es un campo que almacena el titulo del proyecto, con un maximo de 200 caracteres
    title = models.CharField(max_length = 200)
    #Aqui una explicacion mas detallada del proyecto
    description = models.TextField()
    #es un campo de texto que indica las tecnologias utilizadas 
    technology = models.CharField(max_length = 200)
    #es un campo de texto que indica la fecha de inicio del proyecto
    created_at = models.DateField(auto_now_add= True)


