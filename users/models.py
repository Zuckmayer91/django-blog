from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Hacemos que el email sea obligatorio y único
    email = models.EmailField(unique=True) 
    
    web_site = models.CharField(max_length=255, blank=True)
    twitter = models.CharField(max_length=255, blank=True)
    facebook = models.CharField(max_length=255, blank=True)
    instagram = models.CharField(max_length=255, blank=True)

    # Establecemos el email como el identificador principal
    USERNAME_FIELD = 'email'
    # Campos obligatorios además del password y email al crear superuser
    REQUIRED_FIELDS = ['username']
   