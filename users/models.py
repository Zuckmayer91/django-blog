from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission # Añadimos estos imports

class User(AbstractUser):
    # Hacemos que el email sea obligatorio y único
    email = models.EmailField(unique=True) 
    
    web_site = models.CharField(max_length=255, blank=True)
    twitter = models.CharField(max_length=255, blank=True)
    facebook = models.CharField(max_length=255, blank=True)
    instagram = models.CharField(max_length=255, blank=True)

    # --- AQUÍ ESTÁ LA SOLUCIÓN AL ERROR ---
    # Añadimos estos dos campos para evitar el choque con el modelo auth.User
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups", # Nombre único para resolver el conflicto
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions", # Nombre único para resolver el conflicto
        blank=True
    )

    # Establecemos el email como el identificador principal
    USERNAME_FIELD = 'email'
    # Campos obligatorios además del password y email al crear superuser
    REQUIRED_FIELDS = ['username']
   