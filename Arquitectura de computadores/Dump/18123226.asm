;-----------------------------------------------------------------------------------------------------
;										TAREA DEL DUMP
;-----------------------------------------------------------------------------------------------------
;			ARQUITECTURA DE COMPUTADORES
;
;			GRUPO 2
;
;			ESTUDIANTE: ADRIÁN DARÍO VARGAS MONTOYA
;
;			PROFESOR: KIRSTEIN GATJENS SOTO
;
;			CARNE: 2018123226
;-----------------------------------------------------------------------------------------------------
;										MANUAL DE USUARIO
;-----------------------------------------------------------------------------------------------------
;Este programa realiza el dup o vaciado de un archivo linea por linea 
;Para poder utlizar el programa se debe introducir el path de la siguiente manera
;>18123226 x:\carpeta\archivo.txt
;El programa creará un archivo con el mismo nombre pero con la extensión .DUMP
;
;El archivo .DUMP tiene el siguiente formato
;>1- El puntero del archivo representado en un número de cinco dígitos
;>2- Presenta un dump de dos grupos de 8 bytes separados por 3 espacios
;En caso de error el programa presenta una ayuda o un mensaje con el error correspondiente
;-----------------------------------------------------------------------------------------------------
;									ANÁLISIS DE RESULTADOS
;-----------------------------------------------------------------------------------------------------
;Vaciado del DUMP: B
;Validaciones:	B
;Tabla con los caracteres ASCII: E
;Mensajes de error: B
;-----------------------------------------------------------------------------------------------------

;Programa que realiza el dump o vaciado de un archivo que se ingrese su dirección en la línea de comandos
datos segment 
	miniAcercade	db "PROGRAMA QUE REALIZA DUMP DE UN ARCHIVO", 10, 13					
					db "PROGRAMA CREADO POR DARIO VARGAS MONTOYA", 10, 13,"$"		

	msjAyuda	db "No se ha ingresado ningun archivo en la linea de comandos",10,13
				db "Debe ingresar el path de la siguiente forma",10,13
				db "18123226 c:\carpeta\archivo.txt$"

	msjErr1 db "No se encontró el archivo o el path es incorrecto$"
	msjErr2 db "Hubo un error mientras se creaba el archivo de salida$"
	msjErr3 db "Hubo un error al leer el archivo :c$"
	msjExito db "Archivo creado con éxito$" 
	extension db 4, "DUMP"

	nombArchiv db 20 dup (0)
	path db 260 dup(0)
	handleS dw ?
	handleE dw ?

	puntero db 5 dup("0")

	bufferE db 16 dup('x'), 10, 13, '$'
	bufferS db 57 dup('x'), 10, 13, '$'
datos endS

pila segment stack 'stack'
	dw 256 dup(?)
pila ends

codigo segment
assume cs:codigo, ds:datos, ss:pila

valEnt proc
;Procedimiento que valida la entrada de la linea de comandos
;Recibe en [es] un puntero al PSP
	push cx
	push dx
	push si
	
	xor cx, cx
	mov cl, byte ptr es:[80h]				;Número de bytes en la línea de comandos.
	
	mov si, 82h								;Inicio del string sin el espacio		
	cmp cx, 0								;No se ha ingresado nada en la entrada?
	je ayuda								;Si

	add si, cx								;Apunta al final del string
	call obtNomA							;Obtener nombre del archivo	
	dec si									;Apunta al caracter delimitador
	mov byte ptr es:[si], 0					;Cambia el caracter delimitador a 0
	

	mov ah, 02h				
	mov si, 82h								;Apunta al inicio del string
	lea di, path		

	;Guarda en una variable el string de la linea de comandos en formato like c
	conv_LikeC:	mov dl, byte ptr es:[si]	;Mueve a [dl] el caracter actual
				mov byte ptr [di], dl		;Mueve al [di] el caracter actual		 			
				inc si
				inc di					
				int 21h
				cmp dl, 0					;Finalizo la cadena?
				jne conv_LikeC
	jmp fin_ValEnt

	ayuda:	mov ah, 09h
			lea dx, msjAyuda
			int 21h
			jmp fin

	fin_ValEnt:	pop si
				pop dx
				pop cx
				ret

valEnt endp

obtNomA proc
;Procedimiento que obtiene el nombre del archivo

	push cx
	push di
	push dx
	push es
	push si
	xor cx, cx
	lea di, nombArchiv
	mov si, 80h									;Desplazamiento del tamaño del string de la linea de comandos
	mov cl, byte ptr es:[si]						;Tamaño del el string de la linea de comandos
	add si, cx									;Desplaza el si al final del string
	sub si, 1
	
	mov cx, 13									;Tamaño máximo archivo DOS + 1 para verificar "\"
	obtNom:	dec si
			cmp byte ptr es:[si-1], "\"
			je guardNom
			loop obtNom

	guardNom:	mov al, byte ptr es:[si]	
				mov byte ptr ds:[di], al
				inc di
				inc si
				cmp al, "."
				je cambExt
				jne guardNom
	; jmp error0 

	cambExt:	lea si, extension		
				mov cl, byte ptr ds:[si]
				inc si
				mov ax, ds
				mov es, ax
				rep movsb
	pop si
	pop es
	pop dx
	pop di
	pop cx
	ret
obtNomA endp

obtDump proc
;Obtiene el Dump del archivo que se esta leyendo
;Recibe en el [si] el la cadena de caracteres a transformar
;Recibe en el [di] donde se guardara el resultado

	mov bx, 16
	sigByte:	mov al, byte ptr[si]	;Byte actual a convertir
				inc si					;Siguiente byte
				inc cx					;Num de bytes leido
				; cmp cx, 8
				cmp ax, 15
				jl agrCero 

	byteToHex:	xor dx, dx				;Limpio el residuo
				div bx					;Convierto byte a hexadecimal
				call numToHex
				push dx					;Guardo el valor en la pila
				jmp cicloDump

	agrEsp:	push cx						;Guardo el valor de cx
			push ax						;Guardo el valor de ax
			mov al, " "					;Caracter
			mov cx, 3					;Cantidad de veces que se imprimirá el espacio
			rep stosb					;Guarda lo de al en el desplazamiento de memoria
			pop ax						;Recupera el valor de ax
			pop cx						;Recupera el valor de cx
			jmp cicloDump2				

	valEsp:		mov byte ptr ds:[di], " "
				inc di
				jmp cicloDump2

	;Agrega cero en caso de un número menor a 15
	agrCero:	xor dx, dx				;Convierte a número			
				div bx
				push dx					;Guardo el valor en la pila
				push ax

	cicloDump:	cmp ax, 0				
				jne byteToHex			;mientras [ax]>[bx] convierte a hex 
				mov ax, cx				;Copia el contador de caracteres 
				mov cx, 2				;Cantidad de caracteres a copiar

	;Copia dos caracteres en memoria
	vaciarDump:	pop dx						;Recupera el valor de dx
				mov byte ptr ds:[di], dl	;Mueve [dl] al desplazamiento de memoria
				inc di						;Siguiente espacio a guardar
				loop vaciarDump			

	;Compara el contador de bytes para agregar un espacio según sea necesario
				cmp ax, 8					;Si se contaron 8 bytes
				je agrEsp					;Agrega tres espacios
				cmp ax,16					;Si no se contaron 16 caracteres
				jne valEsp					;Agrega un espacio

	cicloDump2:	mov cx, ax				;Recupera el contador
				cmp cx, 16				;Se leyeron 16 bytes?
				jne sigByte				


	ret
obtDump endp

numToHex proc
;Convierte un número decimal en su representacion hexadecimal
;Solo puede convertir números de máximo dos unidades
;Recibe en [dx] el número a convertir
;Devuelve en [dx] la representación en ascii

	cmp dx, 10				;[dx] <= 10
	jle num					;Si	
	jg letra				;No

	num:	add dx, "0"					;Lo convierte a número
			ret

	letra:	add dx, "7"					;Lo convierte a letra
			ret
numToHex endp

obtPuntero proc
;Devuelve el puntero de archivo en un numero de 5 dígitos.
;Recibe en [ax] el número 
;Recibe en [si] un desplazamiento donde se guardará la cadena ASCII
;Devuelve en [ax] el tamaño del número

	push si

	mov bx, 10				;Base a dividir
	obtDec:	xor dx, dx		;limpio el reciduo
			div bx
			add dx, "0"		;Convierte el residuo a base 10
			push dx			;Guarda la unidad en la pila
			inc cx			;Incrementa el largo del número
			cmp ax, 0		;ax == 0?
			jne obtDec		;Mientras [ax] != 0 div [ax] entre 10 

	add si, 5
	sub si, cx
	guardMem:	pop dx						;Recupero el valor dx
				mov byte ptr ds:[si], dl	;Guardo el caracter al puntero en memoria
				inc si
				loop guardMem				;Mientra [cx]!=0 guarda un caracter
	pop si
	ret
obtPuntero endp

crearDump proc
;Procedimiento que procesa la entrda del fichero y crea el dump

	leer:	mov ax, 3F00h	;Funcion de lectura de fichero o dispositivo        
			mov bx, handleE	;Mueve a bx el handle de entrada
			mov cx, 16		
			lea dx, bufferE	;Buffer de entrada
			int 21h            
			jc error3  

			cmp ax, 16
			jl eof
			push cx
	
;Obtiene el puntero actual 
	mov ax, 4201h	;Funcion de DOS para obtener el puntero actual
	mov bx, handleE	;Handle de archivo de entrada
	mov cx, 0 		;Bytes más significativos	
	mov dx, 0		;Byte menos significativos
	int 21h

	lea si, puntero
	call obtPuntero

;Guarda en el buffer de salida una cadena con el puntero en 5 digitos
	lea di, bufferS	;Desplasamiento del buffer de salida 
	; push ds
	; pop es
	mov cx, 5		;Cantidad de dígitos del puntero de archivo
	rep movsb 		;Se copian en el buffer la posicion del puntero

	mov cx, 3		
	mov al, " "		
	rep stosb		;Agrega 3 espacios

	call obtDump	;Obtiene el dump y lo guarda en el buffer de salida

;Escribe en el archivo de salida lo del buffer

	pop cx		;Recupera el valor de cx
	mov ax, cx	
	sub ax, 2	;Cantidad de espacios
	shl cx, 1	;Byte que cuesta almacenar el dump en el archivo
	add cx, ax	;Suma la cantida de espacios a la 
	add cx, 11	;Suma puntero y espacios del formato
	add cx, 2	;Le suma los caracteres de salto de linea

	mov ah, 40h
	lea dx, bufferS
	mov bx, handleS
	int 21h
	jmp leer
	
	eof:	ret

	error3: mov ah, 09h
			lea dx, msjErr3
			int 21h
			ret
crearDump endp

main:	mov ax, datos	;protocolo de inicialización del programa.	
		mov ds, ax	

		mov ax, pila
		mov ss, ax

		call valEnt			

;Abre el archivo
		lea dx, path		;path del archivo de entrada
		mov ax, 3D00h		;Funcion de abrir fichero en modo leectura				
		int 21h				
		jc error1			;Ocurrió un error?
		mov handleE, ax		;Mueve el handle a su respectiva area de memoria


;Crea un fichero de salida
		lea dx, nombArchiv	;Mueve al dx el puntero a buffer de salida
		mov ah, 3Ch			;Funcion para crear fichero
		mov cx, 00h			;Atributo del fichero: normal
		int 21h            
		jc error2			;Hubo un error al crea el fichero?
		mov HandleS, ax   	;Handle de salida    

		push ds
		pop es

	call crearDump			;Crea el dump y escribe en el archivo
	

;Cierra los handle de los archivos
  cerrar:         
		mov bx, handleE   ; cerrar el archivo de entrada
		mov ah, 3Eh
		int 21h

		mov bx, handleS   ; cerrar el archivo de salida
		mov ah, 3Eh
		int 21h

		mov ah, 09h
		lea dx, miniAcercade
		int 21h
		lea dx, msjexito
		int 21h

		jmp fin

;Error al abrir el fichero
		error1:	mov ah, 09h
				lea dx, msjErr1
				int 21h
				jmp fin

;Error de al crear el archivo de salida
		error2: mov ah, 09h
				lea dx, msjErr2
				int 21h						


		
fin:	mov ax, 4C00h
		int 21h


codigo endS
end main