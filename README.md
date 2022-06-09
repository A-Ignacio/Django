# Módulo 6 - Django

Esta rama contiene los elementos propios o requeridos del Módulo 6, de la Actividad Individual número 5.

## Tabla de Contenidos

* [Tecnologias Usadas](#Tecnologias)
* [Instalacion](#Instalacion)
* [Consideraciones](#Consideraciones)
+ [Actualización](#Actualizacion)

<a name="Tecnologias"></a>
## Tecnologias

Este proyecto fue creado usando:
* HTML
* CSS
* [Boostrap](https://getbootstrap.com/)
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)  


<a name="Instalacion"></a>
## Instalacion
Para descargar este proyecto, se debe clonar desde este repositorio remoto a un repositorio local.

$git clone https://github.com/A-Ignacio/Django/tree/AE_individual_5

<a name="Consideraciones"></a>
## Consideraciones

El uso de Django es lo que artícula el funcionamiento central y general de este proyecto, para ello se hace uso del módelo MVC Model - View - Controller

Cuenta con diferentes Templates, dividos en la sección Blog y en la sección Registration, que en general, intenta ordenar los diferentes archivos html respecto de los permisos concedidos, es decir, si está registrado o no. No obstante, es más bien un intento, existen mezclas e imperfecciones en el ejercico de lo recién descrito.

Se han utilziado dos bases de datos, la que viene por defecto en Django respecto al almacenamiento de usuarios llamada User y una creada para el almacenmianto de libros.

En esta versión del proyecto, el almacenamiento de libros contempla sólo el uso de links para su redirección, en un futuro se pretende almacenar directamente los ejemplares que la comunidad comparta.

En el archivo View.py se encuentran las acciones y visualizaciones. Lo destacable es lo concerniente el loggin, logout (salida) y el registro de libros y usuarios.

Respecto del funcionamiento en ejecución de la aplicación, en caso de no estar registrado, se podrá visitar los apartados "index", "Quienes somos", "Crear Usuario" e "Ingresar".

Al momento de ingresar, las opciones disponibles serán "inicio", "Quienes Somos", "Compartir", "Catálogo", "Comunidad", "Salir.

De lo último, aquello destacable es:
  Compartir: se utiliza para registrar el autor, título y enlace para compartir los libros.
  catálogo: Muestra los libros ingresados/almacenados.
  "Comunidad": Muestra los usuarios registrados, junto a información de interés.
  
<a name="Actualizacion"></a>
## Actualización

En esta versión del proyecto, se han incorporado permisos y restricciones.
Se crearon dos grupos de permisos:
*1.UsuariosComunes: Sólo puede subir libros y ver los que están almacenados. Puede acceder a las vistas de "Inicio", "Quiénes Somos", "Catálogo", "Compartir" y "Salir". Dentro de "Catálogo" no pueden editar* ni eliminar.
  Cuentan con los usuarios: 
  Pedro clave: Pedro123
  Pablo clave: Pablo123
  
*2.UsuariosModeradores: Están registrados como Staff, y pueden editar y agregar libros, pueden ver el apartado de "Comunidad", además de los anteriormente mencioandos. En el apartado "Comunidad" pueden editar usuarios.
Cuentan con los usuarios:
Ale clave: Ale123
Nico clave: Nico123

Además, el administrador (usuario Admin) puede eliminar libros y usuarios, además de todos los permisos previamente mencionados.
Cuenta con el usuario:
Admin clave: Admin123
  
Ningún derecho reservado, disponible para su copia, modificación y/o distribución en pos del aprendizaje.
