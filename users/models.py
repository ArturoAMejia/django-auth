from django.db import models

# Create your models here.

class Enrique(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name} ({self.email})"
    

class Colores(models.Model):
    color = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.color}"