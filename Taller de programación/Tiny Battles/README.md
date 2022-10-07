# Introducción
El desarrollo de juegos es una de las herramientas más utilizadas en el proceso de aprendizaje de programación. En esta tarea se deberá implementar el juego de “Guerra de Soldados”, utilizando estructuras de datos como matrices, listas, vectores, funcionalidad del random, generación de interfaces gráficas, entre otros. Se espera que el estudiante (al igual que en los proyectos I y II) desarrolle habilidades en investigación y pueda llevar ese conocimiento a la práctica, y de esta forma, cumplir con los requerimientos que se detallan en esta especificación.

# Descripción del programa
El juego de Guerra de Soldados presenta elementos como:
- **Soldados:** los cuales presentan 4 habilidades mínimas: Fuerza, Inteligencia, Defensa y ataque (se pueden agregar más, si lo desean). Cada escuadrón tendrá 10 soldados.
- **Campo de batalla:** lo cual es una matriz donde los soldados se podrán desplazar de forma aleatoria. Cabe destacar que el campo de batalla debe presentar elementos como árboles, edificios, autos, lagos, etc.

La matriz bidimensional (Campo de batalla) tiene dimensiones definidas por el creador del juego, considerando la racionalidad con respecto a la cantidad de soldados. Una celda o casilla puede ser ocupada a los sumo por dos soldados de diferente escuadrón, la forma interna de representar los elementos en el campo de batalla es libre para el desarrollador.
A continuación se muestra un ejemplo meramente ilustrativo (el diseño e implementación es libre para el desarrollador) del campo de batalla.

<p align = "center">
    <img src = "https://user-images.githubusercontent.com/34630050/194616628-78235c85-5f49-42bb-b089-221c4c2eaf1d.png">
</p>

# Requerimientos de la aplicación
- Funcionalidad correcta del juego:
  -   Posicionamientos aleatorios de los soldados dentro del campo de batalla, contemplando todos los elementos.
  -   Creación y resolución de conflictos, en este caso deberá generar una ventana aparte que ejecute según lo explicado por el profesor. Debe mostrar los detalles visuales (diferentes habilidades). En esta opción debe de presentar dos botones: pelea y huir.
      -  <ins>Pelea:</ins>  determina el soldado vencedor contemplando las diferentes habilidades que presentan cada soldado. Para esto se debe crear una fórmula que utilice los % de cada habilidad y a partir de esto determinar el vencedor. El soldado ganador toma cierto porcentaje de las habilidades del perdedor.
       -  <ins>Huir:</ins>   Simplemente los soldados deciden no pelear y continuar con el juego.
  -  Ver ficha, muestra en una ventana el perfil de cada soldado, habilidades y sus porcentajes, nombre de pila, conflictos ganados y una imagen de cuerpo entero del soldado
  -  Resumen de la batalla, muestra las estadísticas que género la guerra de soldados (Soldados en vida, Soldado muertos, etc.) Esta opción aplica cuando ya no queda ningún soldado de un determinado escuadrón o se decide finalizar el juego en cualquier momento.
