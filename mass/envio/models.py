from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cuenta(models.Model):
    usuario         =   models.CharField(max_length=50)
    clave           =   models.CharField(max_length=20)
    servidor_smtp   =   models.CharField(max_length=250)
    puerto_smtp     =   models.IntegerField()
    
    def __str__(self):
        return self.usuario
    

class Mensaje(models.Model):
    html_mensaje    =   models.TextField()
    
    
    
class Envio(models.Model):
    mensaje         =   models.ForeignKey(Mensaje)
    usuario         =   models.CharField(max_length=240)
    fecha_envio     =   models.DateTimeField()
    enviado         =   models.BooleanField()