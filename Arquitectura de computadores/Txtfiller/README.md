# Txtfiller
La tarea consiste en realizar un programa del tipo painter solo que en modo texto.

En la línea inferior de la pantalla en modo texto debe desplegarse el menú correspondiente.

Se trabajará con el teclado simulando un cursor que debe poder moverse por toda la pantalla con las flechas y dar “clicks” con la barra
espaciadora. Para el cursor escojan un carácter ASCII razonable. Recuerden que al irse moviendo deben salvar y restaurar lo que había
debajo al igual que lo hacía Asterix. Si el cursor está en la línea del menú debe poder seleccionar o una opción o un color.

Si el cursor está en alguna de las 24 líneas superiores puede estar en dos modos. Modo Paint o modo Filler Si es en modo paint cuando se
de un click con la barra debe pintar del color actual el caracter de la posición donde se encuentra. Trabajen con un caracter ASCII que cubra
casi todo el caracter con el color de frente para que puedan usar los 16 colores. Si se está en el modo filler se debe llamar el algoritmo de
rellenado (filler) a partir de la posición en que se encuentra y cambiar el color que había allí por el color actual. Debe llamarse recursivamente
con las posiciones colindantes si estas son del mismo color que se está cambiando. En los painters es la opción del baldecito de pintura que
sireve para rellenar.

Para efectos de no aumentar la complejidad de la tarea, no se tendrá ningún tipo de scroll ni similares y los bordes del área de trabajo de las
primeras 24 filas servirán como límites naturales para el algoritmo de rellenado.

En la documentación además de las tres cosas usuales deben explicar el algoritmo recursivo implementado. Recuerden que todo esto de la
documentación va al inicio del mismo fuente entre comentarios.

En la barra del menú deben estar a la izquierda las opciones de Acerca de y ayuda, cambiar a modo paint, cambiar a modo filler y salir al
sistema operativo. Además en esa barra a la derecha debe estar una paleta con los 16 colores para que pueda seleccionarse el color actual.
Cada color de la paleta debe ser de al menos dos caracteres de ancho. El color actual debe indicarse en esa misma barra, además de en
cual modo estamos (paint o filler) Sean ingeniosos para que todo quepa en una sola fila, aprovechen los colores y caracteres. 
