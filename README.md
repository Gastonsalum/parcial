# Farmasoft

# Informe

# Flujo de programa

Al ingresar a la pagina, vamos a observar la bienvenida al sitio, no permitiendo ingresar a las diferentes consultas que se encuentran en el menu superior SIN LOGUEARSE anteriormente. Una vez logueado, podra acceder a la informacion que administra el sistema.

# Estructura de archivos

El progama esta compuesto por 3 archivos .py. A continuacion se resume que es lo que realiza cada uno de los archivos .py.

1_app.py: El programa esta compuesto por este principal archivo, el cual contiene el import de nuestro archivo .CSV y el ruteo a todas las funciones de la pagina.
2_forms.py: En el mismo se observan las clases de los formularios utilizados en el programa ( cliente, producto, Login)
3_funciones.py: En este mismo archivo estaremos realizando varias cosas. En su primera ejecucion se encontrara validando el archivo .CSV. En la segunuda instalacia se encontrara generando la clave de registro. Luego comenzamos a ejecutar las funciones que se realizaron para poder cumplir con las consignas del Parcial.
funcion de Validacion de caracteres ingresados para la busqueda tanto como para la de clientes y la de producto, funcion de busqueda de clientes ingresados en la lista de registros retorna una lista con todos los clientes encontrados, funcion de busqueda de productos ingresados en la lista de registros retorna una lista con todos los productos encontrados, funcion de busqueda del producto/Cliente encontrado y trae una lista con los objetos del registro que tengan el Producto/Cliente, funcion de suma la cantidad de los productos y me muestra una lista con la suma de lo productos mas vendidos y los ordena de mayor a menor y funcion de busqueda de clientes que gastarons mas dinero y se reconocen como clientes VIP multiplicando las cantidades por el precio.


# Uso del programa

Al ingresar a nuestro sitio, visualizaremos la opcion de bienvenida.En donde visualizaremos nuestro logo, el nombre de nuestra empresa y los creadores de la pagina + la opcion de ingresar al sitio para que se habiliten las opciones que posee el sitio. ( Usser admin, pass admin). A continuacion pasamos a detallar que se observara en cada una de las pestañas del sitio. 

Farmasoft: Se visualizara nuestra pantalla de bienvenida con nuestros datos.

Ingresar: solicitara Usuario y contraseña para poder ingresar al sitio. Luego que se loguearon, visualizaran automaticamente la pantalla de ULTIMAS VENTAS, con opciones en el marco superior: FARMASOFT, SALIR, ULTIMAS VENTAS, CONSULTAS. Pudiendo cliclear sobre cada una de ellas, segun la busqueda que quiera realizar.

Salir: Se deslogueara el usuario logueado.

Ultimas Ventas: En la misma podran visualizar las ultimas ventas que se realizaron.

Consultas: Al cliclear la opcion de consultas, se desplazaran las siguientes opciones : ( Productos por clientes, Clientes por producto, Productos mas vendidos, Mejores clientes. 

Productos por Cliente: Se visualizara en la pagina, el campo de Ingrese el nombre del cliente, en donde debe ingresar una cantidad minima de 3 caracteres, al cliclear la opcion Buscar, aparecera en pantalla los clientes relacionado a los 3 caracteres ingresados, dando la opcion de cliclear LINK, en donde llevara a mostrar en pantalla el listado de productos por clientes. 

Clientes por producto: Se visualizara en la pagina, el campo de Ingrese el nombre del producto, en donde debe ingresar una cantidad minima de 3 caracteres, al cliclear la opcion Buscar, aparecera en pantalla los productos relacionado a los 3 caracteres ingresados, dando la opcion de cliclear LINK, en donde llevara a mostrar en pantalla el listado deseado.

Productos mas vendidos: Se visualizara una lista de los productos mas vendidos, la misma se encontrara de mayor a menor.

Méjores Clientes: Se visualizara una lista de los clientes con mayor compra realizada, la misma se encontrara de mayor a menor.

# Clases diseñadas

Archivos forms.py contiene las siguientes clases:

ProductoForm: en esta clase, se genera el formulario para el ingreso de palabra a buscar entre todos los productos
ClienteForm: en esta clase, se genera el formulario para el ingreso de palabra a buscar entre todos los clientes
LoginForm: en esta clase, se genera el formulario para el ingreso del sistema

Archivos funciones.py contiene la siguiente Clase:
Registro: En esta clase, se realiza la generacion de objeto por cada linea, con los atributos: Codigo, cliente, cantidad, precio, producto






