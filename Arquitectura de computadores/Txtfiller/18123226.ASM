;-----------------------------------------------------------------------------------------------------
;				TAREA TXTFILLER
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
;Para inciar el programa debe escribir el nombre del archivo despues de compilarlo
;>en el menu de abajo a la izquierda se podra salir del programa, abrir el menu de ayuda, el acerca de
;y por ultimo la funcion de pintar y de rellenar en la consola.
;>para pintar en la consola debe presionar la tecla de espacio
;>Para seleccionar un color debe presionar el cursor encima del color deseado
;-----------------------------------------------------------------------------------------------------
;				ALGORITMO RECURSIVO
;-----------------------------------------------------------------------------------------------------
;1-Calcula la posicion segun la fila y la columna actual
;2-Si la posicion actual no es igual al color objetivo termina el algoritmo
;3-Si la columna esta entre 0 y 80 finaliza el algoritmo
;4-Si la fila esta entre 0 y 23 finaliza el algoritmo
;5-Si la posicion actual es igual al color objetivo mueve el color a reemplazar a la posiciona actual
;6-LLama a la funcion recursivamente en la anterior y siguiente fila y columna segun la posicion actual
;-----------------------------------------------------------------------------------------------------
;				ANÁLISIS DE RESULTADOS
;-----------------------------------------------------------------------------------------------------
;Menu del usuario: B
;Funcionamiento del curosr: B
;Modo paint: A
;Modo filler: A
;-----------------------------------------------------------------------------------------------------
datos segment
	FIL			DB	12
	COL			DB	40
	CURSOR		DB	" ",0A0H
	MATRIX		DW	2000 dup(0)
	CLOSEICON	DB	"x",47H
	ABOUTICON	DB	"i",17H
	HELPICON	DB	"?",71H
	PAINTICON	DB	"P",70H
	FILLERICON	DB	"F",70H
	COLRPAL		DB 	" ",00H
	ISFILL		DB 	0

	ABOUTMSJ	DB "PROGRAMA QUE REALIZA LA FUNCION DE BOTE DE PINTURA EN MODO TEXTO", 10, 13					
				DB "PROGRAMA CREADO POR DARIO VARGAS MONTOYA", 10, 13,"$"
	HELPMSJ		DB "PARA HACER FUNCIONAR EL PROGRAMA SE MUEVE CON LAS FLECHAS DEL TECLADO",10,13
				DB "EL MENU DE ABAJO TIENE DIFERENTES OPCIONES, SALIR, EL ACERCA DE, AYUDA",10,13
				DB "BOTON DE MODO PINTAR Y MODO LLENAR, LA P ES DE PINTAR Y F DE LLENAR.", 10,13
				DB "PRECIONAS LA BARRA ESPACIADORA PARA QUE PINTE EN LA CONSOLA, PARA ELEGIR UN",10,13
				DB "COLO DEBES PRECIONAR LA BARRA ESPACIADORA ENCIMA DEL COLOR.$"
datos endS

pila segment stack 'stack'
	dw 2048 dup(?)			
pila ends

codigo segment
	assume cs:codigo, ds:datos, ss:pila

;---------------------------------------------------	
;Procedimiento calcula la posicion actual en la 
;pantalla
;---------------------------------------------------
	calcPos proc 
			 push ax

			mov al, 160
			mul FIL
			xor bh, bh
			mov bl, COL
			shl bx, 1
			add bx, ax	 

			pop ax
			ret	
	calcPos endp

	screens proc
		mov ax, 0003h
		int 10h
		mov ah,09h
		cmp cx, 3
		je hprogrm
		cmp cx, 2

		aboutp:	lea dx, ABOUTMSJ
				int 21h
				jmp iskeypress	
		
		hprogrm:lea dx, HELPMSJ
				int 21h
				jmp iskeypress	
		
		
		ret
	screens endp
;---------------------------------------------------	
;Procedimiento que mueve el cursor
;Recibe: SI = Dirección de la matriz 
;Devuelve: El cursor en pantalla, si se preciona la 
;tecla enter modifica la matriz con el color actual
;del cursor.
;---------------------------------------------------
	 movCursor proc
		call calcPos					
		mov ax, word ptr CURSOR					
		mov word ptr es:[bx], ax	
		iskeypress: mov ah, 01h				
					int 16h
					jnz iskeypress					
					mov ah, 00h 
					int 16h
					
					cmp al, "f"
					je fill
					cmp al, 32					;Espacio
					je click					
					cmp ah, 50h 				;Flecha abajo
					je up 
					cmp ah, 48h 				;flecha arriba
					je down 
					cmp ah, 4Bh 				;Flecha izquierda
					je left 
					cmp ah, 4Dh 				;Flecha dereacha
					je right
					cmp al, 27					;Escape
					je endMovCursor				
					jmp iskeypress				

			click:	xor ah, ah
					mov al, byte ptr FIL
					cmp ax, 24
					je fRow
					mov ax, word ptr ISFILL
					cmp ax, 1
					je fill
					mov ax, word ptr CURSOR		;Cursor en ax
					mov word ptr [si+bx], ax	;Movemos a la matriz 
					jmp updtCursor				

			fRow:	call calcPos
					lea si, MATRIX
					call functions
					cmp cx, 1 
					je endMovCursor
					call screens
					jmp updtCursor

			fill:	xor ax, ax
					lea si, word ptr MATRIX
					mov al, byte ptr FIL
					push ax					;Fila
					mov al, byte ptr COL			
					push ax					;Columna
					mov ax, word ptr CURSOR		
					push ax					;Color de reemplazo
					call calcPos
					mov ax, word ptr [si+bx]
					push ax				;Color objetivo
					call floodFill
					jmp updtCursor

			up:		inc FIL						;Siguiente fila
					jmp updtCursor

			down:	dec FIL						;Anterior fila
					jmp updtCursor

			left:	dec COL						;Anterior columna
					jmp updtCursor
					
			right:	inc COL						;Siguiente columna
					jmp updtCursor

			updtCursor:		call calcPos				;Calcula la posicion actualizada
							mov ax, word ptr CURSOR		;Cursor en ax
							lea si, MATRIX
							call displayMatrix			;actualizamos la pantalla
							mov word ptr es:[bx], ax	;Movemos al cursor la pantalla 
							jmp iskeypress
			endMovCursor:	ret
	 movCursor endp

;---------------------------------------------------	
;Procedimiento que muestra en pantalla lo que se 
;encuentra en una matriz dada.
;Recibe: ES = Direccion de la pantalla
;Recibe: SI = Direccion de la matriz
;---------------------------------------------------
	displayMatrix proc
		push ax
		push di
		push cx
		push si

		mov ah, 00h
		mov al, 03h
		int 10h

		mov di, 0
		xor cx, cx
		L1Matrix:								;Coloca el caracter de la matriz en pantalla
					mov ax, word ptr [si]		;Caracter de la matriz
					mov word ptr es:[di], ax	;Coloca el caracter en pantalla
					add si, 2
					add di, 2
					inc cx
					cmp Cx, 2000
					jne L1Matrix 
		;3840 Direccion de la posicion [24][0]
		lea si, MATRIX		;Direccion matriz
		add si, 0F02H		;fila 24, columna 0 en la matriz
		mov di, 0F02H		;fila 24, columna 0	en la pantalla
		mov cx,0			;bandera de icono
		L2MenuLeft: cmp cx, 0	
					je close
					cmp cx, 1
					je about
					cmp cx, 2
					je help 
					cmp cx, 3
					je modPaint
					cmp cx, 4
					je modFiller 
					add si, 20
					add di, 20
					jmp menuRight

		close:		mov ax, word ptr CLOSEICON
					jmp next

		about:		mov ax, word ptr ABOUTICON
					jmp next

		help:		mov ax, word ptr HELPICON
					jmp next

		modPaint:	mov ax, word ptr PAINTICON
					jmp next

		modFiller:	mov ax, word ptr FILLERICON
					jmp next

		next:		inc cx
					mov word ptr es:[di], ax
					mov word ptr [si], ax
					add si, 4
					add di, 4
					jmp L2MenuLeft
		menuRight:
		mov cx, 15		
		xor ax, ax
		mov dx, 2000H
		L3:		push cx
				add dh,10
				mov cx, 2
		L4:		mov word ptr es:[di], dx
				mov word ptr [si], dx
				add si, 2
				add di, 2
				loop L4             
				pop cx
				loop L3
		
		endDP:
			pop si
			pop cx
			pop di
			pop ax
			ret
	displayMatrix endp

;---------------------------------------------------	
;Procedimiento que interpreta las funciones en 
;pantalla.
;Recibe: BX = Posicion
;Recibe: SI = Direccion de la matriz
;---------------------------------------------------
	functions proc
		mov ax, word ptr[si+bx]
		cmp ax, 0
		je endF
		cmp ax, word ptr CLOSEICON
		je closeprog
		cmp ax, word ptr ABOUTICON
		je aboutscrn
		cmp ax, word ptr HELPICON
		je helpscrn
		cmp ax, word ptr PAINTICON 
		je switch
		cmp ax, word ptr FILLERICON
		je switch

		getcolor:	mov word ptr CURSOR, ax
					jmp endF

		switch:		mov ax, word ptr ISFILL
					cmp ax, 1
					je switch2paint
					jmp swtich2fill

		swtich2fill:	mov ISFILL, 1
						jmp endF

		switch2paint:	mov ISFILL, 0
						jmp endF

		closeprog:	mov cx, 1
					jmp endF

		aboutscrn:	mov cx, 2
					jmp endF
		
		helpscrn: mov cx, 3
		
		endF:
			ret
	functions endp
;---------------------------------------------------	
;Procedimiento que simula un bote de pintura
;Recibe: Direccion del arreglo
;Recibe: Fila actual
;Recibe: Columna actual
;Recibe: Color objetivo
;Recibe: Color de reemplazo
;Devuelve: El algoritmo de bote de pintura
;---------------------------------------------------
	floodFill proc
		push bp
		mov bp, sp

		mov cx, [bp+8]	;Columna
		mov dx, [bp+10]	;Fila
		
		calcPosFF:	mov al, 160		;Calcula la posición
					mul dl
					xor bh, bh
					mov bl, cl
					shl bx, 1
					add bx, ax

		mov dx, [bp+4]				;Color objetivo
		cmp word ptr [si+bx], dx	;El color es igual al color objetivo?
		jne endFF					

		mov cx, [bp+8]				;Columna
		cmp cx, 0					;La columna es 0?
		jl endFF					;Retornar
		cmp cx, 80					;La columna es 80?
		jge endFF					;Retornar

		mov cx, [bp+10]				;Fila
		cmp cx, 0					;La fila es 0?
		jl endFF
		cmp cx, 23 					;La columna es 23?
		jg endFF

		mov dx, [bp+6]				;Color de reemplazo 
		mov word ptr[si+bx], dx		;Reemplazar el color de la posicion actual

		downFF:						;llamada recursiva par abajo
				mov ax, [bp+10]		;Fila
				mov bx, [bp+8]		;Columna
				mov cx, [bp+6]		;Color de reemplazo
				mov dx, [bp+4]		;Color objetivo
				inc ax
				push ax
				push bx
				push cx
				push dx
				call floodFill

		upFF:						;llamada recursiva par arriba
				mov ax, [bp+10]		;Fila
				mov bx, [bp+8]		;Columna
				mov cx, [bp+6]		;Color de reemplazo
				mov dx, [bp+4]		;Color objetivo
				dec ax				
				push ax
				push bx
				push cx
				push dx
				call floodFill

		rightFF:					;llamada recursiva par derecha
				mov ax, [bp+10]		;Fila
				mov bx, [bp+8]		;Columna
				mov cx, [bp+6]		;Color de reemplazo
				mov dx, [bp+4]		;Color objetivo
				inc bx
				push ax
				push bx
				push cx
				push dx
				call floodFill
		leftFF:						;llamada recursiva par izquierda
				mov ax, [bp+10]		;Fila
				mov bx, [bp+8]		;Columna
				mov cx, [bp+6]		;Color de reemplazo
				mov dx, [bp+4]		;Color objetivo
				dec bx
				push ax
				push bx
				push cx
				push dx
				call floodFill

		endFF: 	pop bp
				ret	8
	
	floodFill endp 

MAIN:	mov ax, datos
		mov ds, ax
		mov ax, pila
		mov ss, ax

		mov ax, 0B800H
		mov es, ax

		mov ah, 00h
		mov al, 03h
		int 10h
		call movCursor

FINAL:
	mov ax, 4C00h
	int 21h 


codigo ends
end main