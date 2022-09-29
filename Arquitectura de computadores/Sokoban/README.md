# Sokoban
La tarea consiste en programar un pequeño juego de Sokoban.

Este debe trabajar en el modo texto de 80x25 a 16 colores y para programarlo deben utilizar acceso directo a memoria de video.

La idea es programar un sistema que permita jugar niveles de Sokoban. Del juego en sí se dan detalles más adelante. Será la primera tarea
con una interfaz donde se permanezca “adentro” y no sea por entrada salida estándar o por línea de comandos.

La interfaz debe contener un área suficiente para desplegar el nivel actual donde se juega, así como las opciones a utilizar y los contadores
estadísticos.

Se restringirá el tamaño máximo de cada nivel a 20 filas x 50 columnas para evitar que tengan que programar scroll y puedan trabajar con
estructuras de datos estáticas.

Haremos una bolsa de niveles que todos usaremos. Para esto se les pedirá que los diseñen (o los copien de algún otro sokoban) y los
publiquen en el foro en el topic que pondremos para ese fin. A cada estudiante se le asignará cinco códigos del 000 al 999 para que publique
sus niveles con ese nombre. Los niveles deben ser archivos de texto independientes con el nombre sokoXXX.txt donde XXX es el código de
ese nivel. El formato interno de cada nivel en el archivo txt debe seguirse exactamente para que todos los programas puedan compartirlos.
Este formato se comenta más adelante.

El juego debe comenzar con el nivel 000 y si este no es encontrado debe avanzar automáticamente al 001 y si este no se encuentra al 002 y
ya creo que entendieron la idea. Si al ganar un nivel y buscar el siguiente código el archivo no está, solo pasen al siguiente. Si el contador va
por 999 regresen al 000. 

La actividad de entregar los niveles vale puntos de esta tarea. Serán 10 puntos de la tarea programada, por lo que si la tarea vale 12
resúmenes, entregarlos correctamente les hace ganar 1,2 resúmenes (sin programar nada en ASM, a punta de notepad o del editor de texto
de su preferencia). Adicionalmente les asignaré 5 códigos extra por si se emocionan haciendo niveles puedan ganar unos puntos extras para
la tarea. Si van a entregar niveles extra deben entregarlos junto con los cinco obligatorios para que se tomen en cuenta y todos los
estudiantes puedan utilizarlos. Dejaremos este fin de semana como límite para que los trabajen. 

Para cada nivel debe llevarse un registro del top ten de soluciones. Esto es el registro de las 10 veces que se ha resuelto el nivel de la mejor
forma. El estadístico que se usa para el score es la cantidad de empujones de cajas en premier lugar y la de movimientos que tomó resolverlo
en caso de empate. Cada vez que se mueve con una flecha se cuenta un movimiento. Cada vez que se empuja una caja un espacio cuenta
como un empujón. Claramente entre menos empujones y menos movimientos tome resolver un nivel es un mejor score. Cuando se grabe un
score (resuelva un nivel) se deben pedir las iniciales del jugador para almacenar el score. El formato del archivo o archivos de scores queda a
su criterio y diseño.

Hacer un algoritmo que revise si un nivel puede resolverse o no es algo que no es sencillo (a diferencia del resto de cosas de la tarea) por lo
que esto no se solicitará. Solo se pedirá que al cargar un nivel, antes de permitir jugarlo se hagan dos pequeñas revisiones de cumplimiento.
Si falla en alguna no se debe permitir jugarlo y debe desplegarse un mensaje razonable al respecto. Las dos revisiones son que haya
exactamente un protagonista, no puede no haberlo ni haber más de un bodeguero. Segundo la cantidad de cajas y casillas de acomodo debe
ser la misma y debe ser al menos uno. Esto es no puede ni sobrar cajas ni sobrar casillas de acomodo y no debe haber un nivel sin cajas.

Si alguien diseña algún nivel que no se puede resolver por el tipo de laberinto (bodeguero o cajas encerrados entre muros o cosas similares
por ejemplo) eso no es responsabilidad de ustedes.

Las opciones a programar en el juego como mínimo son las siguientes. La forma de seleccionarlas, teclado, menú, etc. Queda a su elección,
pero debe ser muy claro en la interfaz como seleccionarla.

- Jugar el nivel actual: Debe permitir jugar el nivel con las flechas e ir actualizando las estadísticas conforme se vayan efectuando movimientos
(las estadísticas de los contadores se solicitan más adelante). Si se completa el nivel se debe mostrar una ventana con un mensaje de éxito y
proseguir a jugar el siguiente nivel disponible.

- Resetear el nivel: Debe redesplegar el nivel a como está en el archivo y resetear los contadores de nivel para jugarlo de nuevo. Esta opción
debe ser posible accesarla mientras se está jugando, por que hay veces que fácilmente uno echa a perder el nivel que esta jugando y debe
comenzarlo de nuevo.

- Pasar al nivel siguiente o Regresar al anterior. Cambia de nivel para facilitar la revisión de juego de todos los niveles. Claramente al llegar
al nivel nuevo debe resetear los contadores para comenzar a jugarlo.

- Desplegar los highscores para el nivel actual. Debe abrir una ventana y mostrar el highscore para el nivel actual. Si no se ha logrado ganar
(los datos están en blanco) debe mostrar un mensaje razonable al respecto.

- Acerca de y ayuda. Debe desplegar una ventana con el acerca de y ayuda y tener una opción (botón, tecla, etc.) que le permita quitar la
ventana y regresar al juego. El acerca de y ayuda debe ser muy completo.

- Salir del juego. Debe haber una forma decente de salir al sistema operativo sin tener que matar la máquina virtual (o la real :(
