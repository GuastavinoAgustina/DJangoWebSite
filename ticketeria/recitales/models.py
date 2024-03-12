from django.db import models

class Establecimiento(models.Model):
    nombre = models.CharField(max_length=64)
    ciudad = models.CharField(max_length=64)
    direccion = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.nombre} ({self.ciudad})"

# Create your models here.
class Recital(models.Model):
    #establecimiento = models.ForeignKey(Establecimiento, 
    #                           on_delete=models.CASCADE, 
    #                           related_name="lugar")
    banda_artista = models.CharField(max_length=64)
    #genero = models.CharField(max_length=64)
    horario = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.id}: {self.banda_artista} - {self.horario}"


class Usuario(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    recitales = models.ManyToManyField(Recital, blank=True, related_name="usuario")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
