function confirmacionBorrar(id){
	Swal.fire({
  title: 'Estas seguro?',
  text: "No podras deshacer esto!",
  icon: 'warning',
  showCancelButton: true,
  confirmButtonColor: '#3085d6',
  cancelButtonColor: '#d33',
  confirmButtonText: 'Si, Eliminar!'

}).then((result) => {
  if (result.isConfirmed) {
    Swal.fire(
      'Borrado!',
      'La pelicula ha sido eliminada.',
      'success'
    )
  }
}).then((result2)=>{
    window.location.href="/eliminar-pelicula/"+id+"/";
})
}