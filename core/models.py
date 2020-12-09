from django.db import models

# Create your models here.

class Genero(models.Model):
	nombre=models.CharField(max_length=80)

	def __str__(self):
		return self.nombre


class Pelicula(models.Model):
	nombre=models.CharField(max_length=200)
	duracion=models.IntegerField()
	anio=models.IntegerField()
	genero=models.ForeignKey(Genero,on_delete=models.CASCADE)
	sinopsis=models.TextField(null=True,blank=True)
	fecha_estreno=models.DateField()
	imagen=models.ImageField(null=True,blank=True)
	def __str__(self):
		return self.nombre
			