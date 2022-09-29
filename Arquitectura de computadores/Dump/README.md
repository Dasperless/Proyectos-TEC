# Dump

La tarea consiste en realizar un pequeño programa que haga el dump o vaciado de un archivo. Un dump es para ver la información de
cualquier tipo de archivo, sin importar su formato, como una secuencia de bytes. Es útil para revisar ejecutables, pero debe poder usarse con
todo tipo de archivos.

Deben recibir la entrada por línea de comandos, para esta tarea sí deben validar que sea correcta igual que la anterior.

El nombre del archivo de entrada se debe recibir por la línea de comandos y lo que se reciba pasarlo a la rutina de abrir archivo así como
viene. Con esto nos aprovechamos de poder trabajar con path y con las reglas de la rutina. Recuerde que la línea de comandos es un string
Like Pascal y la rutina recibe uno Like C por lo que debe convertirlo (fabricarlo).

Si no se digita nada se debe desplegar la ayuda completa junto con el acerca de. Si el programa recibió cualquier cosa se despliega el mini
acerca de y luego un mensaje de comunicación del trabajo realizado.

El dump del archivo se debe grabar a un archivo de salida que se llame exactamente igual que el de entrada pero con la extensión cambiada
para que sea .DMP Este es un archivo de texto.

El archivo de vaciado debe tener varias líneas de texto con el vaciado completo del archivo. Al final del archivo se grabarán algunas
estadísticas.

En cada línea de texto de vaciado se vaciará el contenido de 16 bytes del archivo. Al inicio se debe desplegar el contador de posición del
archivo (file pointer, escrito en exactamente 5 dígitos). Luego tres espacios en blanco y luego grupos de ocho bytes separados por tres
espacios en blanco. El valor de cada byte se espera en hexadecimal y un espacio en blanco entre cada byte. Por ejemplo:
````
01024 4F 3E C1 D2 8A 76 21 32 AA BB CC DD EE FF 00 00
````

Deben generar como estadística una tabla con la cantidad de bytes de cada uno de los códigos ASCII. Solo se deben incluir en el archivo
aquellas cantidades que fueron diferentes a cero (o sea que de esos bytes sí había en el archivo). Para cada carácter deben desplegar su
dibujo ASCII, el código en hexadecimal, en decimal y la cantidad que había. 
