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
        return f"{self.banda_artista} ({self.fecha}) "
    
    @property
    def imagenURL(self):
        try:
            url = self.imagen.url
        except:
            url = ''
        return url

class Reserva(models.Model):
    recital = models.ForeignKey(Recital,on_delete=models.CASCADE, related_name="recital")
    cantidad_entradas = models.IntegerField()
    imagen = models.ImageField(null=True, blank =True)
    
    @property
    def imagenURL(self):
        try:
            url = self.imagen.url
        except:
            url = ''
        return url
    def __str__(self):
        return f"{self.recital} {self.cantidad_entradas}"
    
    @property
    def get_total(self):
        total = self.recital.precio * self.cantidad_entradas
        return total



class Usuario(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    reservas = models.ForeignKey(Reserva,on_delete=models.CASCADE, related_name="reservas")
   
    @property
    def get_total_compra(self):
        entradas = Reserva.objects.all()
        total = sum([entrada.get_total for entrada in entradas])
        return total
    @property
    def get_total_entradas(self):
        entradas = Reserva.objects.all()
        total = sum([entrada.cantidad_entradas for entrada in entradas])
        return total

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
 
