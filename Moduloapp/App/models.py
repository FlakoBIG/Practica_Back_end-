from django.db import models

# Create your models here.
class Personaje(models.Model):
    Nombre = models.CharField(max_length=20)
    Arma = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
