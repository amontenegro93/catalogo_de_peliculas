from Pelicula import Pelicula
from CatalogoPeliculas import CatalogoPeliculas

opcion= None
while opcion !=4:
    try:
        print('Opciones: ')
        print('1. Agregar pelicula')
        print('2. Listar peliculas: ')
        print('3. Eliminar catalogo')
        print('4: Salir')
        opcion=int(input('escribe tu opcion (1-4)'))

        if opcion ==1:
            nombrePelicula= input('ingresa el nombre')
            pelicula= Pelicula(nombrePelicula)
            CatalogoPeliculas.agregarPelicula(pelicula)
        elif opcion ==2:
            CatalogoPeliculas.listarPeliculas()
        elif opcion==3:
            CatalogoPeliculas.eliminarPeliculas()

    except Exception as e:
        print(f'error: {e}')
        opcion=None
else:
    print('hasta luego')


