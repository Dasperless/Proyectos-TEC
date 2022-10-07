# Introducción
La reducción de los costos de los boletos aéreos se dio principalmente por la eliminación de los intermediarios a la hora de comprar boletos, ya que las aplicaciones de búsqueda de boletos permitieron que personas ajenas a agencias de viajes pudieran encontrar los precios más accesibles disponibles para un vuelo determinado. En esta tarea se va a implementar un buscador de vuelos básico, el cual permitirá a los usuarios hacer una serie de consultas y operaciones, las cuales serán descritas más adelante.

# Descripción del programa
La información del buscador de vuelos se va a manejar mediante una base de datos por medio de tablas. La tabla tiene una estructura, que representa los nombres de los campos o las columnas de la información que va a ser almacenada. Los registros (propiamente los datos) se llaman filas de la tabla. En varios archivos de texto se van a recibir los datos de los vuelos y de las aerolíneas. Los archivos van a ser convertidos a listas con estructura, para poder ser manipulados de esa forma. Cada lista tiene su propia estructura, como es descrita a continuación. Se van a tener las siguientes tablas:

Tabla: Aerolíneas

Nombre archivo: aerolineas.txt

Campos: ID, Nombre

<table>
  <thead>
    <tr>
      <th scope="col">ID</th>
      <th scope="col">Nombre</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">2</th>
      <td>Taca</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>United Airlines</td>
    </tr>
    <tr>
      <th scope="row">...</th>
      <td>...</td>
    </tr>
  </tbody>
</table>

El ID es un identificador interno único de cada aerolínea, va a ser manejado como un consecutivo de forma automática por el sistema.

Tabla: Vuelos

Nombre archivo: vuelos.txt

Campos: número vuelo, fecha, origen, destino, horaPartida, horaLlegada, idAerolínea, precio


<table>
  <thead>
    <tr>
      <th scope="col">Numero Vuelo</th>
      <th scope="col">Fecha</th>
      <th scope="col">Origen</th>
      <th scope="col">Destino</th>
      <th scope="col">Hora partida</th>
      <th scope="col">Hora llegada</th>
      <th scope="col">Id aerolínea</th>
      <th scope="col">Precio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">TA093</th>
      <td>12/03/2011</td>
      <td>SJO</td>
      <td>JFK</td>
      <td>1400</td>
      <td>1525</td>
      <td>1</td>
      <td>350</td>
    </tr>
    <tr>
      <th scope="row">UA1012</th>
      <td>06/07/2011</td>
      <td>LAX</td>
      <td>MIA</td>
      <td>930</td>
      <td>1145</td>
      <td>2</td>
      <td>120</td>
    </tr>
    <tr>
      <th scope="row">...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table>

Para la implementación del sistema se deben crear funciones que permitan accesar listas anidadas basadas en los algoritmos vistos en clase. Las tablas van a ser almacenadas como listas de listas. Nótese que los nombres de los campos no pertenecen a la lista, se asume que la estructura de las tablas es conocida por el programa. Los archivos de datos pueden venir inicialmente vacíos, o tener datos. La estructura de los archivos de datos es similar a la presentada a continuación:

Aerolíneas.txt

[1,”Taca”]</br>
[2,”United Airlines”]</br>
[3,”Iberia”]</br>

Vuelos.txt

[“TA093”,”12/03/2011”,”SJO”,”JFK”,”1400”,”1525”,1,350]
[“UA1012”,”06/07/2011”,”LAX”,”MIA”,”930”,”1145”,2,120]

A nivel conceptual, el sistema va a manejar dos modos: mantenimiento, que permite realizar operaciones sobre la base de datos, y modo consulta, que permite realizar búsquedas y consultas sobre los vuelos almacenados en el programa.

# Descripción funcional
- El programa deberá correr en el sistema operativo Windows, y deberá estar escrito para Python 3 o superior.
- El programa deberá correr utilizando interfaz gráfica. Para esta opción queda totalmente libre los componentes que deseen utilizar, pueden usar ventanas, menús, botones, canvas, o cualquier otro que deseen.
- Cuando el programa inicia, deberá cargar la información de aerolíneas y vuelos de los archivos aerolineas.txt y vuelos.txt. Posteriormente, el programa le presentará al usuario dos modos de operación: Gestión de la aplicación, y búsqueda de vuelos.

# Gestión de la aplicación
Debe permitir operaciones básicas sobre las tablas de la base de datos

Tabla de aerolíneas
- Inclusión: permite agregar una nueva aerolínea. Requiere el nombre de la aerolínea. El ID se generará automáticamente con base en los IDs anteriores (el ID es un consecutivo). En el archivo de aerolíneas (aerolineas.txt) se deberá agregar la nueva información, usando el formato descrito anteriormente.
- Exclusión: permite eliminar una fila de la tabla. Debe eliminarse la información del archivo de datos (aerolineas.txt).

Tabla de vuelos
- Inclusión: permite agregar información de nuevos vuelos. Requiere que el usuario ingrese toda la información de vuelos descrita anteriormente. El usuario ingresará el nombre de la aerolínea como parte de la información, pero en la tabla no se almacenará el nombre, sino que se almacenará el ID asociado a esa aerolínea, de acuerdo a la información de la tabla de aerolíneas. En el archivo de vuelos (vuelos.txt) se deberá agregar la nueva información, usando el formato descrito anteriormente.
- Exclusión: permite eliminar una fila de la tabla. Debe eliminarse la información del archivo de datos (vuelos.txt).

Tabla de reservaciones
Para esta opción, el estudiante es libre de estructurar y diseñar la tabla. Para esta operación, debe permitir al usuario (administrador) poder realizar las siguientes consultas:
- Mostrar todos los vuelos realizados por un usuario particular (origen - destino)
- Mostrar todos los vuelos realizados filtrados por una nacionalidad en particular
- Mostrar las 5 ciudades más visitadas

# Busqueda de vuelos
Debe permitir hacer las siguientes búsquedas de vuelos usando los siguientes filtros:
- Fecha del vuelo
- Aerolínea
- Lugar de origen
- Lugar de destino
- Vuelos menores a un precio

A la hora de hacer la búsqueda de un vuelo, el usuario podría elegir sólo usar un filtro. Por ejemplo, se podría buscar todos los vuelos en cierta fecha. O podría usar varios filtros, por ejemplo, buscar todos los vuelos de lugar de origen “SJO” y lugar de destino “MIA”, de la aerolínea “Delta”, para el día 03/04/2012.
El sistema deberá desplegar al usuario la información correspondiente a su búsqueda, de acuerdo a la información de la base de datos.
