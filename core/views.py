from django.shortcuts import render,redirect
from .models import Pelicula
from .forms import PeliculaForm

# Create your views here.
def home(request):
	data={
		'peliculas':Pelicula.objects.all()
	}
	return render(request,'core/index.html',data)


def galeria(request):
	return render(request,'core/galeria.html')


def listado_pelicula(request):
	peliculas=Pelicula.objects.all()
	data={
		'peliculas':peliculas
	}
	return render(request,'core/listado_peliculas.html',data)



def nueva_pelicula(request):
	data={
		'form':PeliculaForm()
	}

	if request.method=='POST':
		formulario=PeliculaForm(request.POST,request.FILES)
		if formulario.is_valid():
			formulario.save()
			data['mensaje']="guardado correctamente!!"

		data['form']=formulario

			
	return render(request,'core/nueva_pelicula.html',data)


def modificar_pelicula(request,pk):

	pelicula=Pelicula.objects.get(id=pk)
	data={
		'form':PeliculaForm(instance=pelicula)
	}

	if request.method=='POST':
		formulario=PeliculaForm(data=request.POST,instance=pelicula,files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			data['mensaje']="actualizado con exito!!"
		data['form']=PeliculaForm(instance=Pelicula.objects.get(id=pk))


	return render(request,'core/modificar_pelicula.html',data)



def eliminar_pelicula(request,pk):
	pelicula=Pelicula.objects.get(id=pk)
	pelicula.delete()

	return redirect('listado_pelicula')