from django import forms
from django.forms import ModelForm
from .models import Pelicula
import datetime

class PeliculaForm(ModelForm):
	nombre=forms.CharField(min_length=6,max_length=50)
	duracion=forms.IntegerField(min_value=1,max_value=8)




	class Meta:
		model=Pelicula
		fields=['nombre','duracion','anio','genero','fecha_estreno','sinopsis','imagen']


		widgets={
			'fecha_estreno':forms.SelectDateWidget(years=range(1945,2021))
		}


	def clean_fecha_estreno(self):
		fecha=self.cleaned_data['fecha_estreno']
		if fecha>datetime.date.today():
			raise forms.ValidationError("La fecha no puede ser mayor al dia de hoy!!!")

		return fecha

