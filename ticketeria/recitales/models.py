from django.db import models

class Establecimiento(models.Model):
    nombre = models.CharField(max_length=64)
    ciudad = models.CharField(max_length=64)
    direccion = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.nombre} ({self.direccion} - {self.ciudad}) "

# Create your models here.
class Recital(models.Model):
    banda_artista = models.CharField(max_length=64)
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE, related_name="lugar")
    fecha = models.DateField()
    horario = models.TimeField()
    precio = models.IntegerField() 
    imagen = models.ImageField(null=True, blank =True)

    def __str__(self) -> str:
        return f"{self.id}: {self.banda_artista} - {self.horario}"

class Reserva(models.Model):
    recital = models.ForeignKey(Recital,on_delete=models.CASCADE, related_name="recital")
    cantidad_entradas = models.IntegerField()

class Usuario(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    reservas = models.ForeignKey(Reserva,on_delete=models.CASCADE, related_name="reservas")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
 
