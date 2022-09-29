;-----------------------------------------------------------------------------------------------------
;										TAREA GARGANTUA
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
; +Para el funcionamiento de este programa se necesita DOSBox,Tlink y TASM
; +Se ingresa en la consola de DOSBox el siguiente Comando para compilarlo
;
; >tasm 18123226
;
; +Luego se enlaza de la siguiente manera
;
; >tlink 18123226
;
; +Luego para poder realizar las operaciones se debe realizar de la siguiente forma
;	>[Operacion] [Base del resultado] [Base primer número]-[Número]- [Base segundo número]-[Número]-
;
; +Por ejemplo:	
; >18123226 -s 15 2-101- 10-60-
;+El programa debería regresar el resultado de la siguiente forma
; >16-41
;+El formato del resultado es [Base del resultado]-[Resultado]
;-----------------------------------------------------------------------------------------------------
;									ANÁLISIS DE RESULTADOS
;-----------------------------------------------------------------------------------------------------
;MOSTRAR EL RESULTADO: B
;CREAR CALCULOS CON NÚMEROS GRANDES: E
;MOSTRAR ERRORES: D
;-----------------------------------------------------------------------------------------------------

datos segment
	Ayuda	db "PROGRAMA QUE REALIZA CALCULOS",10,13									;Mini acerca de.
			db "PROGRAMA CREADO POR DARIO VARGAS MONTOYA",10,13			;Mini acerca de.
			db "Uso: 18123226 [-Opcion] [Base] [Base-num-] [Base-num-]",10,13		;Instrucciones.
			db "Opciones:",10,13
			db	09,"-h",09,"Muestra la ayuda del programa.",10,13
			db	09,"-s",09,"Suma dos numeros de cualquier base.",10,13
			db	09,"-r",09,"Resta dos numeros de cualquier base.",10,13
			db	09,"-m",09,"Multiplica dos numeros de cualquier base.",10,13
			db	09,"-d",09,"Divide dos numeros de cualquier base.",10,13,"$"
			 
	MsjError db "Error$"
	ErrorConversion db "Error de conversion$"
	MsjCarctNoVal db "Caracter no valido en la entrada: $"
	MSJDivCero	db "Division por cero$"
	
	Operacion db 2 dup(0) 															;Caracter ASCII con la letra de la Operacion.
	BaseRes db 3 dup(0)																;Base de la respuesta de la Operacion.
	BaseNum1 db 8 dup(0)															;Base del primer numero.
	BaseNum2 db 8 dup(0)															;Base del segundo numero.
	Num1 db 33 dup(0)																;Valor del primer numero.
	Num2 db 33 dup(0)	
	Res dd 32 dup(0)																;Valor del segundo numero.
datos endS

pila segment stack 'stack'
	dw 512 dup(?)
pila ends

codigo segment
	assume cs:codigo, ds:datos, ss:pila	
	;--------------------------------------------------------------
	VerifError proc
	; Subrutina que imprime en la entrada estandar un error
	; Espera un numero en [cl] 
	;--------------------------------------------------------------
		push ax
		push dx
			xor ah,ah
			cmp cl,0	;No existe ningun error?
			je finError

			cmp cl,1	;Error al ingresar el comando?
			je caractNoValido

			caractNoValido:
				lea dx,MsjCarctNoVal				;Mueve a [dx] un puntero al mensaje de error
				mov ah,09h
				int 21h
				mov ah,02h
				mov dl,byte ptr es:[si]
				int 21h
				jmp fin 

			finError: 
				pop dx
				pop ax
				ret	
	VerifError endp

	;--------------------------------------------------------------
	VerifOperacion proc near
	; Subrutina que verifica la operación.
	; Incrementa el valor de [si].
	; Devuelve en [cl] 1 si hay error ó 0 si es exitoso.
	;--------------------------------------------------------------
		push dx
			cmp byte ptr es:[si],"-"	;Es el caracter un guion?
			jne errorOp			

			inc si						;Incrementa si para apuntar al siguiente caracter.
			cmp byte ptr es:[si],"h"	;Es el caracter una 'h' ?
			je mostrarAyuda				
				
			cmp byte ptr es:[si],"s"	;Es el caracter una 's' ?
			je finVerifOp					
				
			cmp byte ptr es:[si],"r"	;Es el caracter una 'r' ?
			je finVerifOp					
				
			cmp byte ptr es:[si],"m"	;Es el caracter una 'm' ?
			je finVerifOp					
			
			cmp byte ptr es:[si],"d"	;Es el caracter una 'd' ?
			je finVerifOp					
			
			jmp errorOp					;El caracter de la opción no es válida.
			
			finVerifOp:
				mov dl,byte ptr es:[si]	;Copia el caracter en [dl].
				lea di,Operacion		;Copia en [di] el puntero a un area de memoria.
				mov byte ptr [di],dl	;Copia en el area de memoria el caracter.
				mov cl,0				;Valor de retorno de exito.
				pop dx				
				ret

			errorOp:
				mov cl,1				;Valor de retorno de error
				pop dx
				ret

			mostrarAyuda:
				lea dx,Ayuda			
				mov ah,09h			
				int 21h				
				jmp fin						

	VerifOperacion endp

	;--------------------------------------------------------------------------------
	VerifBaseRes proc
	;Subrutina que verifica la base en la que se dara la respuesta del comando.
	;La rutina incrementa el valor de [si].
	;Se espera en [es] un puntero al PSP.
	;Se espera en [si] apuntando a la linea de comandos.
	;Devuelve en [cl] un 0 en caso de termine exitosoamente, un 1 en caso contrario.
	;--------------------------------------------------------------------------------
		push ax
		push di 
			
			inc si 						;Siguiente caracter, se espera un espacio 
			cmp byte ptr es:[si],' '	;Compara [dl] con un espacio
			jne errorBaseRes			;Si no es un espacio muestra error
			inc si						;Siguiente caracter, se espera un numero

			lea di,BaseRes					;Mueve a [di] un puntero a un área de memoria.
			xor ah,ah
			cicloVerifBaseRes:
				cmp byte ptr es:[si],0Dh	;Final de la linea de comandos?
				je errorBaseRes		
				cmp byte ptr es:[si],'9'	;Es el caracter un número?				
				jg errorBaseRes				
				cmp byte ptr es:[si],'0'	;Es el caracter un número?				
				jl errorBaseRes				
				mov al,byte ptr es:[si]		;Muevo en [al] el caracter en consola.
				mov byte ptr [di],al		;Muevo al area de memoria el caracter 
				inc si						
				inc di
				cmp byte ptr es:[si],' '	;Siguiente parametro del comando?
				jne cicloVerifBaseRes

			verifTamBase:
				mov byte ptr [di],0			;Termina el string en un caracter nulo.

				push si							;Se guarda el valor de [si].
				lea si,BaseRes					;Mueve a [di] el string a convertir.
				call StringToInt				;Convierte el string a entero.
				pop si							;Se restaura el valor de [si].
				
				cmp al,2						;Es una base permitida?
				jl errorBaseRes		
				cmp al,36						;Es una base permitida?
				jg errorBaseRes			
				jmp finVerifBaseRes				;Fin de la subrutina

			finVerifBaseRes:
				mov cl,0
				pop di
				pop ax
				ret
			
			errorBaseRes:
				mov cl,1
				pop di
				pop ax
				ret

				
	VerifBaseRes endp

	;-----------------------------------------------------------------------------------------------
	VerifCaracter proc
	;Subrutina para verificar el caracter que se haya ingresada sea un numero o letra permitida.
	;Recibe en [es] un puntero al PSP.
	;Recibe en [si] la direccion del acaracter a verificar.
	;Recibe en [dl] el numero que se esta verificando.
	;Devuelve en [cl] un 0 si terminó con exito, 1 en caso contrario.
	;-----------------------------------------------------------------------------------------------
		push dx
		push es
		push si
			cmp byte ptr es:[si],0Dh		;Existe un cracter de finalización?
			je caracter_invalido			
			
			xor dh,dh
			cmp dl,1
			je base_num1
			cmp dl,2
			je base_num2

			base_num1:
				push si				;Guarda el valor de [si]
				lea si,BaseNum1		;Mueve a [si] el área de memoria de la base del primer número.
				call StringToInt	;Convierte la base a entero.
				pop si				;Recupera el valor de [si]	
				jmp verifBaseLetra	;Verifica si la base pude usar letras.

			base_num2:
				push si				;Guarda el valor de [si]
				lea si,BaseNum2		;Mueve a [si] el área de memoria de la base del segundo número.
				call StringToInt	;Convierte la base a entero.
				pop si				;Recupera el valor de [si]
				jmp verifBaseLetra	;Verifica si la base puede usar letras

			verifBaseLetra:
				cmp al,16			;Es la base igual a 16?
				jl verif_numero		;Si es menor verifica los números.
				jge verif_letras	;Si es mayor o igual verifica si hay letras.	

			verif_letras:
				cmp byte ptr es:[si],'A'	;Es un número?
				jl verif_numero				
				cmp byte ptr es:[si],'Z'	;Es un número?
				jg caracter_invalido		
				jmp finVerifCaract			

			verif_numero:
				cmp byte ptr es:[si],'0'	;Es un número?
				jl caracter_invalido		
				cmp byte ptr es:[si],'9'	;Es un número?
				jg caracter_invalido		
				jmp finVerifCaract			
				
			caracter_invalido:
				mov cl,1
				pop si
				pop es
				pop dx
				ret

			finVerifCaract:
				mov cl,0
				pop si
				pop es
				pop dx
				ret
		
	VerifCaracter endp

	;--------------------------------------------------------------------------------------
	VerifNums proc
	;Subrutina que verifica el la base y el número ingresado en la linea de comandos.
	;Este subrutina incrementa el valor de [si].
	;Recibe [dl] el número que está verificando.
	;Devuelve en [cl] un 0 si es exitoso o un 1 si falla.
	;--------------------------------------------------------------------------------------
		push bx
		push dx
		push di

		cmp dl,1
		je verifBaseNum1
		cmp dl,2
		je verifBaseNum2

		verifBaseNum1:
			cmp byte ptr es:[si],' '	;Es el caracter actual un guión?
			jne errorVerifNums
			inc si						;Siguiente caracter, se espera un número.
			lea di,BaseNum1
			jmp ciclo_verifBaseN

		verifBaseNum2:
			cmp byte ptr es:[si],' '	;Es el caracter actual un guión?
			jne errorVerifNums
			inc si						;Siguiente caracter, se espera un número.
			lea di,BaseNum2
			jmp ciclo_verifBaseN

		ciclo_verifBaseN:
			cmp byte ptr es:[si],0Dh	;No se ingreso un número?
			je errorVerifNums
			cmp byte ptr es:[si],'0'	;Es un número?
			jl errorVerifNums
			cmp byte ptr es:[si],'9'	;Es un número?
			jg errorVerifNums

			mov bl,byte ptr es:[si]		;Mueve a [bl] el caracter actual.
			mov byte ptr [di],bl		;Copia en la memoria el caracter actual.			
			inc si
			inc di
			cmp byte ptr es:[si],'-'	;Es el caracter actual un gión?
			jne ciclo_verifBaseN			
			jmp MemNums

		MemNums:
			mov byte ptr [di],0
			cmp byte ptr es:[si],'-'	;Verifica inicio del número.
			inc si						;Siguiente caracter, se espera un número.
			cmp dl,1
			je verif_num1
			cmp dl,2
			je verif_num2

		verif_num1:
			lea di,Num1					;Se mueve [di] un puntero a un área de memoria.
			jmp ciclo_verifNum

		verif_num2:
			lea di,Num2					;Se mueve [di] un puntero a un área de memoria.
			jmp ciclo_verifNum

		ciclo_verifNum:
			call VerifCaracter
			call VerifError

			mov bl, byte ptr es:[si]	;Se mueve a [bl] el caracter actual.
			mov byte ptr [di],bl		;Mueve a un área de memoria el caracter actual.
			inc si
			inc di
			cmp byte ptr es:[si],'-'	;Ah finalizado el número.
			jne ciclo_verifNum
			jmp finCicloNum		

		errorVerifNums:
			mov cl,1					;Mueve a [cl] un 1 en caso de error.
			pop di
			pop bx
			pop dx
			ret 

		finCicloNum:
			mov byte ptr [di], 0
			inc si
			jmp finVerifNums		

		finVerifNums:						
			mov cl,0					;Mueve a [cl] un 0 en caso de exito.
			pop di
			pop bx
			pop dx
			ret				
	
	VerifNums endp

	;-----------------------------------------------------------
	VerifComando proc
	;Esta subrutina verifica si la linea de comandos se ingresó
	;Correctamente
	;Recibe en [es] el puntero al PSP
	;Recibe en el [si] apuntando al string
	;-----------------------------------------------------------
		push si
		push es
			mov si,82h				;Dirección del PSP
			cmp byte ptr es:[si],0	;No se ha ingresado un comando?
			je noArgumentos			
			op:									;Verifica el caracter de operación.
				call VerifOperacion				;LLama la rutina para verificar que la operación.
				call VerifError					;Verifica si existe errror.

			verif_base:
				call VerifBaseRes				;Rutina que verifica la base de la respuesta.
				call VerifError					;Verifica si existe error.

				push si
				lea si,BaseRes
				call StringToInt
				call LimpiarMem
				mov byte ptr[si],al
				pop si

			verif_Nums:		
				mov dl,1						;Verifica el primer número.
				call VerifNums					;Verifica el formato.
				call VerifError					;Verifica si existe error.

				push si
				lea si,BaseNum1
				call StringToInt
				call LimpiarMem
				mov byte ptr[si],al
				pop si

				mov dl,2						;Verifica el segundo número.
				call VerifNums					;Verifica el formato.
				call VerifError					;Verifica si existe error.
				push si
				lea si,BaseNum2
				call StringToInt
				call LimpiarMem
				mov byte ptr[si],al
				pop si

			finVerif:
				pop es
				pop si	
				ret
			
			noArgumentos:
				lea dx,Ayuda					
				mov ah,09h
				int 21h							;Imprime el mensaje en la salida estandar. 
				jmp fin
	VerifComando endp
	
	;-----------------------------------------------------------
	StringToInt proc
	; Función que convierte un string a un entero.
	; Recibe en [si] apuntando string a convertir.
	; Devuelve en [al] el valor en entero.
	; Devuelve en [cl] el largo del numero.
	;-----------------------------------------------------------
		push bx
		push dx
		push si
	
		xor ax,ax
		xor bx,bx
		xor cx,cx
		xor dx,dx
		
		mov bl,10
		sigDig:
			mov dl,byte ptr [si]	;Mueve el caracter a dl
			cmp dl,'-'				
			je finConv				;Finaliza si encuentra un guion
			cmp dl,0
			je finConv				;Finaliza si encuentra un caracter de finalizacion
			cmp dl,' '				
			je finConv				;Finaliza si es se encuentra un espacio
			cmp dl,'0'					
			jl errorConv			;Si el ASCII es menor a 48 muestra finaliza		
			cmp dl,'9'
			jg errorConv			;Si el caracter ASCII es mayor a 57 finaliza	
			sub dl,'0'				;Convierto de ASCII a decimal
			mul bl					;(al*bl)
			add al,dl				;(al+dl)	
			inc si					
			inc cx					;Decrementa el contador de caracteres de la linea de comandos
			jmp sigDig
			
		errorConv:
			lea dx,ErrorConversion		;Mueve a [dx] el mensaje de error
			mov ah,09h					;Instruccion para imprimir en la salida estandar
			int 21h					
			jmp fin 					;Finaliza el programa
			
		finConv:
			pop si
			pop dx
			pop bx
			ret
		
	StringToInt endp

	;------------------------------------------------------------------
	Potencia proc
	; Función que devuelve la la base elevada al exponente de potencia
	; Recibe en [bx] la base.
	; Recibe en [cx] la potencia.
	; Devuelve en [ax] la respuesta.
	;------------------------------------------------------------------
		push bx
		push cx
		push dx
			mov ax,1		
			cmp cx,0					;Es la potencia 0?
			je finPotencia		

			cicloPotencia:
				mul bx					;ax*bx
				loop cicloPotencia		;Mientras [cx] no sea 0 repetir
				
			finPotencia:
				pop dx
				pop cx
				pop bx
				ret
	Potencia endp

	;-----------------------------------------------------------
	len proc 
	; Función que cuenta la cantidad de digitos de un número.
	; Recibe en [si] un puntero a un área de memoria.
	; Devuelve en [cx] el tamaño del número.
	;-----------------------------------------------------------
		push si
		xor cx,cx
		
		cicloLen:	inc cx
					inc si
					cmp byte ptr[si],0
					jne cicloLen

		pop si
		ret
	len endp

	LimpiarMem proc
	;Limpia la memoria de un área de memoria y vuelve a apuntar al inicio
	;Recibe en [si] el puntero al área de memoria que se limpiará
	;--------------------------------------------------------------------
		push cx
		xor cx,cx
		ciclo_LimpiarMem:	mov byte ptr ds:[si],0
							inc si
							inc cl
							cmp byte ptr ds:[si],0
							jne ciclo_LimpiarMem
		sub si,cx	
		pop cx
		ret
	LimpiarMem endp

	;------------------------------------------------------------------
	ConvBase10 proc
	; Función que convierte número de cualquier base a base 10.
	; Recibe en [bl] la base del número.
	; Recibe en [si] un puntero al número.
	; Devuelve en [dx] el valor del número.
	;------------------------------------------------------------------
		push ax
		push bx
		push cx
		push si

		xor cx,cx
		xor dx,dx
		xor bh,bh
		call len	;Tamaño del número
		dec cl
		ciclo_ConvBase10:	call Potencia
							cmp byte ptr[si],"A"
							jge es_letra
							jmp es_num

		es_letra:	push bx				;Guardo el valor de [bx]
					xor bx,bx
					mov bl,byte ptr[si]
					sub bx,"7"			;Lo convierto a decimal
					jmp conv_base10

		es_num:	push bx					;Guardo el valor de [bx]
				mov bl,byte ptr[si]
				sub bx,"0"				;Lo convierto a decimal
				jmp conv_base10

		conv_base10:	push dx		;Guarda el valor de [dx]
						mul bx		;Multiplica [bx]*[ax]		
						pop dx		;Recupera el valor de [dx]
						add dx,ax	;Le suma al [dx] el resultado de [ax]
						inc si		;Siguiente caracter
						dec cx		
						pop bx		;Recupera el valor de [bx]
						cmp cx,0
						jge ciclo_ConvBase10
		pop si
		pop cx
		pop bx
		pop ax
		ret
	ConvBase10 endp
	
	;------------------------------------------------------------------
	mostrar_division proc
	;Recibe en [AX] el cociente
	;Recibe en [DX] el residuo
	;Recibe en [CX] la base del resultado
	;Recibe en [SI] un puntero donde se almacena el resultado
	;------------------------------------------------------------------
		push ax
		push cx
		push dx
		push si
			call ConvBaseRes
			push ax
			push dx
			mov ah,02h
			mov dl,09
			int 21h
			pop dx
			pop ax
			mov ax,dx
			call ConvBaseRes
		pop si
		pop dx
		pop cx
		pop ax
		ret
	mostrar_division endp	
	;--------------------------------------------------------------------------
	RealizarOperacion proc
	;Realiza la operación según lo ingresado en la consola.
	;Recibe en [al] un caracter con la operacion
	;Recibe en [bl] la base del primer número.
	;Recibe en [bh] la base del segundo número.
	;Recibe en [si] un puntero al string del primer número.
	;Recibe en [di] un puntero al string del segundo número.
	;Retorna la respuesta en 
	;--------------------------------------------------------------------------
		push ax
		push bx
		push di
		push es
		push si

		convertir_Base10:	push dx
							call ConvBase10		;Convierte el primer número a base 10
							mov es,dx 			;Mueve a [es] el resultado
							pop dx

							xchg bh,bl			;Intercambia la base 
							mov si,di			;Intercambia el puntero al numero.
							call ConvBase10		;Convierte el segundo número a base 10
							mov cx,es 			;Mueve a [cx] el valor del primer número.

							cmp al,"s"			;Es una suma?
							je suma
							cmp al,"r"			;Es una resta?	
							je resta
							cmp al,"m"			;Es una multiplicación?
							je multiplicacion
							cmp al,"d"			;Es una division?
							je division

		suma:	add cx,dx				;Suma el primer número con el segundo
				jmp fin_operacion

		resta:	sub cx,dx				;Resta el primer número con el segundo
				jmp fin_operacion		

		multiplicacion:	mov ax,es			;Mueve a [ax] el valor del primer número
						mul dx				;Multiplica [ax] con [dx]
						mov cx,ax			;Mueve a [cx] lo que hay en [ax]
						jmp fin_operacion		
						
		division:	mov ax,es			;Mueve el valor del primer número en [ax]
					mov cx,dx			;Mueve el valor del segundo número en [cx]
					cmp cx,0 
					je division_cero

					xor dx,dx
					div cx				;Divide lo que hay en [ax] con [cx]
					lea si,BaseRes
					mov cl,byte ptr ds:[si]
					lea si,Res
					call mostrar_division
					jmp fin

		division_cero:	mov ah,09h
						lea dx,MSJDivCero
						int 21h
						jmp fin_operacion

		fin_operacion:	pop si
						pop es
						pop di
						pop bx
						pop ax
			ret
	RealizarOperacion endp	

	;--------------------------------------------------------------------------
	print proc
	;Imprime el contenido de [si]
	;Recibe un puntero a un área de memoria en [si]
	;--------------------------------------------------------------------------
		push ax
		push dx
		push si
		mov ah,02h
		ciclo_print:	mov dl,byte ptr[si]
						int 21h
						dec si
						cmp byte ptr[si],0
						jne ciclo_print
		pop si
		pop dx
		pop ax
		ret
	print endp

	;--------------------------------------------------------------------------
	ConvBaseRes proc
	;Convierte de base 10 a la base que se desea.
	;Recibe en [ax] el número en base 10
	;Recibe en [cx] el la base en la que se dará la respuesta.
	;Recibe en [si] el puntero al area en memoria que se guardará
	;--------------------------------------------------------------------------
		push cx
		push bx
		push di
		push dx
		
		ciclo_ConvBaseRes:	xor dx,dx
							div cx
							cmp ax,0
							je fin_Conv
							cmp cx,10				;Es la base mayor a 10?
							jg mayor_diez			;Si
							jle menorigual_diez		;No

		menorigual_diez:	add dx,'0'		;Convierte el residuo a ASCII	
							jmp guardar_mem	;Guarda en el área de memoria el número

		mayor_diez:	cmp dx,10			;Es el residuo menor a 10?
					jl menorigual_diez	;Si
					add dx,55			;Si no,le suma 55 (representacion de número como letra)
					jmp guardar_mem

		guardar_mem:	mov word ptr[si],dx		;Mueve a si, el número convertido a ASCII
						inc si					;Siguiente digito
						cmp cx,ax				;Es el número menor a la base?
						jng ciclo_ConvBaseRes	;No
							
		mov word ptr[si],ax						;Mueve al área de memoria el dividendo
		cmp ax,10								;Es la base mayor a diez?
		jg sumar_siete							;No

		sumar_cero:	add byte ptr[si],'0'	;Convierte el número a ASCII
					inc si
					jmp agregar_base		;Agrega la base del número convertido

		sumar_siete:	add byte ptr[si],'7' 	;Convierte el número a ASCII
						inc si
		
		agregar_base:	mov ax,cx				;Mueve la base al dividendo
						mov cx,10
						mov byte ptr[si],"-"	
						inc si

		
		ciclo_AgrBase:	xor dx,dx				;Limpia el registro dx	
						div cx					;divide la base por 10
						mov byte ptr[si],dl		
						add byte ptr[si],"0"	;Número convertido a ASCII
						inc si						
						cmp ax,0				;Es el residuo 0?
						je fin_ConvBaseRes		;SI
						cmp ax,10				;Ya no se puede dividir?
						jng ciclo_AgrBase						 
		fin_Conv:
		mov byte ptr[si],dl		
		add byte ptr[si],"0"	;Número convertido

		fin_ConvBaseRes:	dec si
							call print

		pop dx
		pop di
		pop bx
		pop cx
		ret
	ConvBaseRes endp
	main:	
		mov ax, ds					;Mueve a [ax] un puntero al PSP
		mov es, ax 					;Mueve al [es] el puntero al PSP

		mov ax, pila				;Mueve lo que tiene en la pila a [ax]
		mov ss, ax					;Mueve la pila al Stack Segment.

		mov ax, datos				;Mueve al acumulador área de memoria de los datos.
		mov ds, ax					;Mueve al data segmet el áre de memoria que contiene las variables.

		call VerifComando			;Verifica si el comando fue ingresado correctamente 

		mov al,Operacion			;Caracter con la operación a realizar
		mov bl,BaseNum1				;Número de la base del primer número
		mov bh,BaseNum2				;Número de la base del segundo número.
		lea si,Num1					;Puntero al string del primer número.
		lea di,Num2					;Puntero al string del segundo número.
		call RealizarOperacion		;Realiza la operación	

		mov ax,cx					;Mueve lo que hay en el resultado del número en base 10 a [ax]
		lea si,BaseRes				;Mueve a [si] la base en la que se dará la respuesta
		mov cx, word ptr[si]		;Mueve a cx la base en la que se da la respuesta
		lea si,Res
		call ConvBaseRes			;Convierte el número a la base
		
	fin: 
		mov ax, 4C00h
		int 21h 

		
codigo ends
end main