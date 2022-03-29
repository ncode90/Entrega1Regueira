from django.db import models

# Clase 1
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

# Clase 2
class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

# Clase 3
class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)