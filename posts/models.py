from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # Cambiamos auto_created por auto_now_add
    created_at = models.DateTimeField(auto_now_add=True)