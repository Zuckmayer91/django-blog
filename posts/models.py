from django.db import models

    
class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)  # Nuevo campo para el orden
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']  # Esto hace que Django ordene los posts por defecto
        
   