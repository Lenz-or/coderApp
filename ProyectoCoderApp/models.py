from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre= models.CharField(max_length=30) #texto
    apellido= models.CharField(max_length=30) #texto
    email = models.EmailField(blank=False, null=True) #email-opcional

class Curso(models.Model):
    nombre= models.CharField(max_length=30) #texto
    comision= models.IntegerField()
    

class Profesor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email = models.EmailField(blank=False, null=True) #email-opcional
    profesion= models.CharField(max_length=30)