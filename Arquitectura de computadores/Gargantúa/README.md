# Gargantua
Programa que hace cálculos con números gigantes.
La tarea consiste en realizar un pequeño programa que haga cálculos con números gigantes.
Deben recibir la entrada por línea de comandos, y para esta tarea sí deben validar que sea correcta.
Se trabajará con números en bases diferentes de la 2 a la 36, para trabajar los dígitos con letras mayúsculas y los dígitos usuales.
Un número siempre se escribirá como la base en dos caracteres un guión y la secuencia de dígitos correspondiente, terminado en un guión:
2-1111- 10-2020- 16-F8A5E2- 36-ZORRO45-
Se tendrá una longitud máxima de 32 dígitos. El primer guión que separa la base del número no se debe almacenar. El último guión sí porque indica
el final del número, excepto si es un número que gaste los 32 dígitos.
Esperamos que sea claro que el número tiene una representación textual para permitir el almacenamiento de números gigantes.
Las opciones que deben manejar son las siguientes:
-h despliega la ayuda. Esta también se debe desplegar junto con el acerca de si no hay opciones digitadas, al igual que en todas las tareas.
-s suma dos números:
-s 16 2-101 8-10
Debiera responder
16-D
Las opciones -r -d y -m restan, multiplican y dividen y funcionan de forma análoga a la suma. Recuerde que es división entera por lo que en ese caso
debe dar dos datos de respuesta (cociente y residuo).
La dificultad de la tarea está claramente en la implementación de los algoritmos para manejar cálculos con ese tipo de números.
El reporte de errores debiera ser con un mensaje sensato a la salida estándar. Ejemplos:
División por cero.
Dígito inválido en la base xx.
Caracter no válido en la entrada: X 
