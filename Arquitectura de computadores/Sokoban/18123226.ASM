;-----------------------------------------------------------------------------------------------------
;				TAREA Sokoban
;-----------------------------------------------------------------------------------------------------
;			ARQUITECTURA DE COMPUTADORES
;
;			GRUPO 2
;
;			ESTUDIANTE: ADRIÁN DARÍO VARGAS MONTOYA
;
;			PROFESOR: KIRSTEIN GÄTJENS SOTO
;
;			CARNE: 2018123226
;-----------------------------------------------------------------------------------------------------
;				MANUAL DE USUARIO
;-----------------------------------------------------------------------------------------------------
;>Para iniciar el programa es necesario el uso de dosbox
;>Debe colocarse los archivos txt en una carpeta llamada niveles para poder funcionar
;>Controles
;r = reinicia el juego
;s = siguiente nivel
;a = anterior nivel
;Esc = salir del juego
;-----------------------------------------------------------------------------------------------------
;				ANÁLISIS DE RESULTADOS
;-----------------------------------------------------------------------------------------------------
;Jugar el nivel actual: E
;Resetear el nivel: B
;Pasar al nivel siguiente o Regresar al anterior:C
;Desplegar los highscores para el nivel actual: F
;Acerca de y ayuda: F
;Salir del juego:A
;-----------------------------------------------------------------------------------------------------
datos segment
;Variables del juego
	empujes		dw 2 dup (0)
	movimientos	dw 2 dup (0)
	nivel 		dw 2 dup (0)
	handleE 	dw ?						;Manejador del juego
	nombNivel 	db "niveles\soko000.txt"	;Path de los niveles
	fila 		db 0              			;Fila actual de la pantalla
    columna 	db 0              			;Columna actual de la pantalla
	num 		db 4 dup(0)					;Variable que almacena un contador en ascii
	juego 		db 2000 dup("#")			;Matriz del juego
	posBod		dw 2 dup(0)

;Labels 
	msjEmpujes 	db "Empujes:",0
	msjMov		db "Movimientos:",0
	msjNvlAct	db "Nivel:",0
	msjSigNvl	db "Siguiente nivel: s",0
	msjAntNvl	db "Anterior nivel: a",0
	msjReincr	db "Reiniciar nivel: r",0
	msjAyuda	db "Hacerca de y ayuda: h",0

;Mensajes de error que se muestran en pantalla
	msjError1 	db "No se ha encontrado el nivel",10,13,"$"
	msjError2	db "El nivel actual no es jugable",10,13,"$"

;Caracteres y colores que se muestran en pantalla
	espBlancoC 	db ' ', 00H 		;Espacio en blanco de color negro que representa un espacio en blanco
	muroC 		db '.', 40h			;Espacio de color rojo que representa el muro
	cajaC		db '#', 07h			;Numeral de color gris y fondo negro que representa una caja
	cajaD		db '*', 70h			;Numeral de color gris y fondo negro que representa una caja
	bodegueroC	db 64, 07h 			;Inicio de texto con fondo negro y de color gris que representa el bodeguero
	casillaC	db 178, 70h 		;Caracter grafico de color blanco con fondo negro
	bodegueroD	db 64, 70h

	; PAUSA1 dw 1000
	; PAUSA2 dw 10000
datos endS

pila segment stack 'stack'
	dw 256 dup(?)				;Se puede cambiar la pila
pila ends

codigo segment
	assume cs:codigo, ds:datos, ss:pila

;-------------------------------------------------
;Procedimiento que convierte de int a ascii
;Recibe en el [ax] el numero.
;Devuelve el numero en un espacio en memoria (num)
;-------------------------------------------------
	enteroAscii proc
		push cx
		push di
		push dx

		mov cx, 3							;Es un numero de 3 digitos
		mov bx, 10						
		xor dx,dx 
		ciclo_conv:		div bx				;Convierto el numero a ascii
						add dx, "0"
						push dx
						xor dx,dx
						loop ciclo_conv

		mov cx, 3
		mov ah,02h
		lea di, num
		fin_conv:	pop dx					;Copio el numero a una variable
					mov byte ptr[di], dl
					inc di
					loop fin_conv
		pop dx
		pop di
		pop cx
		ret
	enteroAscii endp

;---------------------------------------------------	
;Procedimiento que carga un nivel de sokoban.
;Guarda el handle en un espacio en memoria (handleE)
;---------------------------------------------------
	cargJuego proc
		push di
		push si
		cargNivel: 		lea di, nombNivel
				  		add di,12		
						mov ax,word ptr nivel
						call enteroAscii
						lea si,	num	
						mov cx,3	

		cicl_cargNvl:	mov al,byte ptr[si]
						mov byte ptr[di],al
						inc di
						inc si
						loop cicl_cargNvl

		abrirNvl:	lea dx, nombNivel		;Abrimos el archivo en modo lectura
					mov ax, 3D00h			
					int 21h					
					jc error1				;Ocurrió un error?
					mov handleE, ax			;Mueve el handle a su respectiva area de memoria

		cargNivl:	mov ah, 3fh
					mov bx, handleE
					mov cx, 2000
					lea dx, juego
					int 21h

		mov ah, 3Eh 						;Cerramos el archivo
		mov bx, handleE
		int 21h

		call revNivel
		cmp cx, 0
		jne error2

		pop si
		pop di
		ret 

		error1:	mov ah,09h			;El nivel no existe
				lea dx, msjError1				
				int 21h
				inc nivel
				jmp cargNivel

		error2: mov ah,09h			;El nivel no es jugable
				lea dx, msjError2 
				int 21h
				inc nivel 
				jmp cargNivel
	cargJuego endp

;---------------------------------------------------	
;Procedimiento muestra las opciones del sokoban 
;en la pantalla
;---------------------------------------------------
	mostrFunc proc
		push ax
		push cx
		push dx
		push di
		push si
		mov fila, 0 
		mov columna, 0
		xor cx, cx

		mov di,104
		cambFun:	cmp cx, 0
					lea si, msjEmpujes
					je ciclo_mostr

					mov di, 264
					cmp cx, 1
					lea si, msjMov
					je ciclo_mostr

					mov di, 424
					cmp cx, 2 
					lea si, msjNvlAct
					je ciclo_mostr

					mov di, 584
					cmp cx, 3
					lea si, msjAntNvl
					je ciclo_mostr

					mov di, 744
					cmp cx, 4
					lea si, msjSigNvl
					je ciclo_mostr

					mov di, 904
					cmp cx, 5
					lea si, msjReincr
					je ciclo_mostr

					mov di, 1064
					cmp cx, 6
					lea si, msjAyuda
					je ciclo_mostr
					jmp fin_mostFun

		ciclo_mostr:	mov dl, byte ptr [si]
						mov byte ptr es:[di], dl
						inc si
						add di,2
						cmp byte ptr [si], 0
						jne ciclo_mostr

						cmp cx, 0
						je contEmp
						cmp cx, 1
						je contMov
						cmp cx, 2
						je contNvl
						inc cx
						jmp cambFun

		contNvl:	mov ax, nivel
					call enteroAscii
					inc cx
					lea si, num
					jmp mostEst

		contMov:	mov ax, movimientos
					call enteroAscii
					inc cx
					lea si,num
					jmp mostEst

		contEmp:	mov ax, empujes
					call enteroAscii
					inc cx
					lea si, num
					jmp mostEst

		mostEst:	mov dl, byte ptr [si]
					mov byte ptr es:[di], dl
					inc si
					add di, 2
					cmp byte ptr [si], 0
					jne mostEst
					jmp cambFun

		fin_mostFun:	pop si
						pop di
						pop dx
						pop cx
						pop ax
						ret
	mostrFunc endp

;----------------------------------------------------------------	
;Procedimiento que muestra el nivel en pantalla
;Recibe en un area en memoria el nivel de sokoban
;Devuelve en pantalla el nivel.
;----------------------------------------------------------------
	mostrNivel proc
		push ax
		push dx
		push si
		push di

		mov ax, 0003h	
		int 10h

		mov ax, 0B800H
		mov es, ax		;Video Ram Segment
		mov di, 0		;Posición 0 del juego
		lea si, juego	;Puntero al juego
		xor dx,dx
		cicl_mostT:	mov dl, byte ptr [si]		;Muestra en pantalla un color segun el caracter
					cmp dx, "."
					je eBlanco
					cmp dx, "M"
					je muro
					cmp dx, "X"
					je caja
					cmp dx, "*"
					je caja2
					cmp dx, "K"
					je bodeguero
					cmp dx, "+"
					je bodeguero2
					cmp dx, "O"
					je casilla
					cmp dx, 10
					je sigfila
					cmp dx, "#"
					jne sigCaract
					call mostrFunc
					jmp fin_mjuego

		eBlanco:	mov dx, word ptr [espBlancoC]
					jmp sigCaract	

		muro:		mov dx, word ptr [muroC]
					jmp sigCaract
		
		caja:		mov dx, word ptr [cajaC]
					jmp sigCaract

		caja2:		mov dx, word ptr [cajaD]
					jmp sigCaract		

		bodeguero:	mov dx, word ptr [bodegueroC]
					jmp sigCaract

		bodeguero2:	mov dx, word ptr [bodegueroD]
					jmp sigCaract
		
		casilla:	mov dx, word ptr [casillaC]
					jmp sigCaract

		sigCaract:	mov al, 160             ;Calculamos BX = FIL*160+Col*2 
        			mul fila 	            
        			xor bh, bh  	        
        			mov bl, columna         
        			shl bx, 1        	    
        			add bx, ax          	
					mov di, bx

					mov word ptr es:[di], dx
					inc si
					inc columna
					xor dx, dx
					jmp cicl_mostT 

		sigfila:	inc si
					inc fila
					mov columna, 0
					jmp cicl_mostT		

		fin_mjuego:	mov word ptr fila, 0
					mov word ptr columna, 0
					pop di		
					pop si
					pop dx
					pop ax
					ret
	mostrNivel endp

;------------------------------------------------------------------------			
;Procedimiento que revisa si se puede jugar el nivel 
;Recibe en un area de memoria (juego) el nivel a jugar
;Devuelve en el [cx] un 0 si es jugable, de lo contrario devuelve un 1
;------------------------------------------------------------------------		
	revNivel proc
		xor ax,ax								;cajas
		xor bx,bx								;casillas de acomodo
		xor dx,dx								;Bodegero

		lea si, byte ptr juego
		cicl_rvNivl:	cmp byte ptr[si], "X"	;Reviso si existen bodegueros, cajas o casillos y las sumo
						je exCaja
						cmp byte ptr[si], "O"
						je exCasAcom
						cmp byte ptr[si], "K"
						je exBodgero
						jmp sigCarctRN

		exCaja:	inc ax					;Existe caja			
				jmp sigCarctRN

		exCasAcom:	inc bx				;Existe casilla de acomodo
					jmp sigCarctRN

		exBodgero:	inc dx				;Existe bodeguero
					mov word ptr posBod, si
					jmp sigCarctRN

		sigCarctRN: inc si					;Siguiente caracter
					cmp byte ptr[si], "#"
					jne cicl_rvNivl

		vrfCajCas:	cmp ax,bx				;Hay la misma cantidad de casillas que cajas?
					jne errNvl				;No
											;Si
		vrfBodeg:	cmp dx, 1 				;Hay un bodeguero?
					je fin_vrfNvl			;Si
					jne errNvl				;No
		
		fin_vrfNvl:	mov cx, 0	;Finalizo con exito
					ret
						
		errNvl:	mov cx, 1		;Codigo de error (El nivel no es jugable)
				ret

	revNivel endp

;----------------------------------------------------------------	
;Procedimiento que empieza el juego
;Recibe: en un area de memoria la posicion del bodeguero (posBod)
;Devuelve: la posicion actualizada del bodeguero y los muestra
;En pantalla
;----------------------------------------------------------------
	empJuego proc
		mov si, posBod		;Posicion del bodeguero

		movJuego: 	mov ax, 0001h   ;Z=0 SI CARACTER INGRESADO, CARACTER EN AL, CODIGO DE RASTREO EN AH
					int 16h
					jz movJuego
					jmp haytecla

		reset:	mov empujes, 0
				mov movimientos, 0
				call cargJuego
				call mostrNivel
				mov si, posBod
				jmp movJuego

		sig:	inc nivel
				jmp reset

		ant:	dec nivel
				jmp reset
								

		haytecla:	cmp al, 27
					jz finJuego
					cmp al, "r"
					jz reset
					cmp al, "s"
					jz sig
					cmp al, "a"
					jz ant
					cmp al,0
					jz flechas
					jmp movJuego

		flechas:	cmp ah, 50h ;Flecha abajo
					je abajo 
					cmp ah, 48h ;flecha arriba
					je arriba 
					cmp ah, 4Bh ;Flecha izquierda
					je izquierda 
					cmp ah, 4Dh ;Flecha dereacha
					je derecha 
					jmp movJuego

		arriba:		mov dl, byte ptr[si]
					mov cx, 1
					call calcMov
					jmp repetir

		abajo:		mov dl, byte ptr[si]
					mov cx, 2
					call calcMov
					jmp repetir

		izquierda:	mov dl, byte ptr[si]
					mov cx, 3
					call calcMov
					jmp repetir

		derecha:	mov dl, byte ptr[si]
					mov cx, 4
					call calcMov
					jmp repetir

		repetir:	cmp byte ptr[si], "*"
					je mostrar
					cmp byte ptr[si], "+"
					je mostrar					
					mov byte ptr [si], "K"
		mostrar:	call mostrNivel
					jmp movJuego

		finJuego:	mov ax, 0003h	
					int 10h
					ret
	empJuego endp
;----------------------------------------------------------------	
;Procedimiento que calcula el movimiento en la matriz del sokoban
;Recibe:la posicion del bodeguero en el [si] y en el [cx] el 
;movimiento que se desea realizar
;Devuelve: la posicion del bodeguero en la fila de arriba o de 
;abajo en el [si]
;----------------------------------------------------------------
	calcMov proc
		push ax
		push di
		push dx

		xor ax, ax
		xor dx, dx

		mov di, si
		cmp cx, 1
		je filArriba
		cmp cx, 2
		je filAbajo
		cmp cx, 3
		je movizq
		cmp cx, 4
		je movderch

		filArriba:	dec di					;Busca encontrar el final de la fila para contar las columnas
					cmp byte ptr[di], 0
					je fueraDeRango
					cmp byte ptr[di], 13
					jne filArriba
					jmp contArrb

		filAbajo:	dec di 					;Busca encontrar el inicio de la fila para contar las columnas
					cmp byte ptr[di], "#"
					je fueraDeRango
					cmp byte ptr[di], 10
					jne filAbajo
					jmp contAbj

		contArrb: 	dec di					;Cuenta desde el final hasta el inicio de la fila
					inc dx					
					cmp byte ptr[di], 0		;Si no existe otra fila termina
					je fueraDeRango
					cmp byte ptr[di], 10	;Se encontro el inicio de la fila?
					jne contArrb
					jmp restar

		contAbj:	inc di					;Cuenta desde el inicio hasta el final de la fila
					inc dx
					cmp byte ptr[di], "#"	;Si no existe la siguiente fila termina
					je fueraDeRango
					cmp byte ptr[di], 13	;Se encontro el final de la fila?
					jne contAbj
					jmp sumar

		fueraDeRango:	jmp fin_ContCol

		sumar:		inc dx
					mov di, si
					add di, dx 
					jmp verifMov

		restar:		inc dx
					mov di, si
					sub di, dx
					jmp verifMov

		movizq:		dec di
					jmp verifMov

		movderch:	inc di
					jmp verifMov
		
		verifMov:	cmp byte ptr[di], "O"
					je hayCasilla
					cmp byte ptr[di], "."
					je valido
					cmp byte ptr[di], "X"
					je calcpush
					cmp byte ptr[di], "*"
					je calcpush
					jmp fin_ContCol

		hayCasilla:	cmp byte ptr[si], "X"
					je cajaCas
					cmp byte ptr[si], "*"
					je cajaCas
					cmp byte ptr[si], "K"
					je bodeCas
					cmp byte ptr[si], "+"
					je bodeCas2
					jmp fin_ContCol

		bodeCas2:	mov byte ptr[di], "+"
					mov byte ptr[si], "O"
					mov si,di
					jmp fin_ContCol

		bodeCas:	mov byte ptr[di], "+"
					mov byte ptr[si], "."
					mov si, di
					jmp fin_ContCol

		cajaCas:	mov byte ptr[di], "*"
					mov si, di
					jmp fin_ContCol

		calcpush:	cmp byte ptr[si], "X"	;Si es una caja no se puede mover
					je fin_ContCol
					cmp byte ptr[si], "*"
					je fin_ContCol

					push si
					mov si, di
					call calcMov			
					cmp si, di				;SI = DI si hay muro o caja
					je pushInval			
					cmp byte ptr[si], "*"	;Es una caja dentro de una casilla?		
					je pushCas				;No cambiar el caracter
					mov byte ptr[si], "X"
		pushCas:	inc empujes
					pop si

					mov byte ptr[si], "."
					mov si, di
					jmp fin_ContCol

		bodCas3:	mov byte ptr[si], "O"
					jmp valido2

		valido:		cmp byte ptr[si], "+"
					je bodCas3
					mov byte ptr[si], "."
		valido2:	mov si, di
					inc movimientos
					jmp fin_ContCol

		pushInval:		pop si
		fin_ContCol:	pop dx
						pop di
						pop ax
						ret
	calcMov endp

MAIN:	mov ax,datos		;protocolumnao de incio
		mov ds,ax
		mov ax,pila
		mov ss,ax
		
		call cargJuego		;Cargamos el juego a memoria
		call mostrNivel		;Muestra el juego en pantalla
		call empJuego

FINAL:	mov ax, 4C00h
		int 21h 
codigo ends
end main