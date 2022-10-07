# Introducción
El desarrollo de juegos es una de las herramientas más utilizadas en el proceso de aprendizaje de programación. En esta tarea se deberá implementar el juego de Buscaminas, utilizando estructuras de datos como Matrices, listas, entre otras. Se espera que el estudiante desarrolle sus habilidades en investigación y pueda llevar ese conocimiento a la práctica, y de esta forma, cumplir con los requerimientos que se detallan en esta especificación.

# Descripción del programa
Un buscaminas es una matriz bidimensional de un número (n) de filas y número (m) de columnas en donde cada celda tiene un valor entero para representar la cantidad de minas colindantes dentro de la matriz. Entiéndase que un cero (0) indica que esa casilla/celda no tiene ninguna mina colindante, un uno (1) indica que esa casilla/celda tiene una mina colindante, un dos (2) indica que esa casilla/celda tiene dos minas colindantes, y así sucesivamente. A continuación se muestra un ejemplo de los valores que tendría la estructura matriz y como se representaría a nivel grafico.

  <figure>
    <img src="https://user-images.githubusercontent.com/34630050/194624390-275538f2-e82e-41c1-a9f4-ba61c133301c.png">
    <figcaption>Figura 1: Ejemplo de estructura de la matriz</figcaption>
  </figure>
  
  <figure>
     <img src="https://user-images.githubusercontent.com/34630050/194624335-c2c6515a-8a39-4b2f-a367-9f399e3ad05b.png">
     <figcaption>Figura 2: Ejemplo de visualización del juego buscaminas tomando la estructura de la figura 1</figcaption>
  </figure>
  
# Requerimiento de la aplicación
- Deberá generar toda la interfaz gráfica para la ejecución correcta de la aplicación, según lo explicado por el profesor.
- Deberá permitir jugar al usuario, o sea el jugador trata de encontrar y marcar las celdas de la cuadricula que contengan minas. Cuando haga clic en una celda aparecerá el número de celdas colindantes que tienen una mina. Si haces clic en una celda con 0 minas alrededor, se revelaran automáticamente las celdas junto a ellas.
- Se requiere marcar las celdas de la cuadricula que contengan minas con una bandera. Adicionalmente, se puede marcar la celda con un signo de pregunta “?”. Esto sirve para ayudar a vigilar las celdas desconocidas mientras se continua resolviendo la cuadricula.
- Se gana la partida cuando se hayan descubierto todas las celdas libres (sin minas). Si hace clic sobre una celda que contiene una mina, se perderá la partida.
- El juego tendrá tres modos de juego: Fácil, tiene una cuadricula de 5x5 y 5 minas, Medio, tiene una cuadricula de 10x10 y 10 minas y Difícil, tiene una cuadricula de 16x16 y tiene 25 minas. Adicionalmente, tendrá la opción de personalizado donde el jugador podrá ubicar las minas en las celdas deseadas y posteriormente construir la interfaz del juego.
- Las matrices con la estructura de la cuadricula serán almacenadas en archivos de texto. Esto implica que se deben de realizar lectura y escritura de archivos de texto para guardar partidas del juego.
- La aplicación tendrá las opciones de juego nuevo, lo cual implica un “reset” al juego actual y comenzar de nuevo.
- La aplicación tendrá la opción de “descubrir” aplicación que consiste en revelar lo que contiene cada celda de la cuadricula.
- Otras opciones adicionales son: “Acerca de…” donde muestra toda la información relevante del juego, por ejemplo, derechos de autor, versión, entre otros (ver ejemplos en internet). La otra opción es “Ayuda”, en donde el usuario podrá encontrar información sobre como utilizar el juego, cuales son los objetivos, formas de usos, funcionalidades, entre otros.
- Cualquier duda con algún requerimiento deberá consultar con el profesor, y es importante destacar que la aplicación esta abierta para la creatividad del programador, en caso de incluir alguna funcionalidad o característica adicional.
- Se entregarán puntos extras al mejor proyecto. Este punto es a consideración del profesor.
