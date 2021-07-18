class CatalogoPeliculas:
    rutaArchivo = 'peliculas.txt'

    #comentario
    @classmethod
    def agregarPelicula(cls,pelicula):
        with open(cls.rutaArchivo,'a',encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}/n')
