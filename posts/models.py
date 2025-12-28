from django.db import models
from django.conf import settings # Para referenciar al AUTH_USER_MODEL

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # Cambia la línea del slug por esta:
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    
    # Imagen de portada (se guardará en la carpeta /media/posts/)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    
    # Fecha de creación y actualización automática
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Relación con tu modelo de usuario personalizado
      
    
    user = models.ForeignKey(
    settings.AUTH_USER_MODEL, 
    on_delete=models.CASCADE,
    related_name='posts',
    null=True,    # <--- Añade esto temporalmente
    blank=True    # <--- Añade esto temporalmente
   )

    def __str__(self):
        return self.title