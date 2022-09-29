;-----------------------------------------------------------------------------------------------------
;				TAREA CheCOM
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
;>Para utilizar el programa debe compilarlode la siguiente manera
;	+tasm 18123226 
;>Luego, para crear el archivo .COM se debe linkear de la siguiente maner
;	+tlink 18123226 /t
;>Para crear el cheque debe ingresar el nombre y el apellido a quien se le hará el cheque, por último
;Se ingresa el monto a pagar. Por ejemplo:
;	+18123226 Dario Vargas 6000
;>Luego de esto se le mostrará el cheque
;>En caso de que no se ingrese nada en consola se mostrará un acerca de y el formato que se utiliza 
;para mostra el cheque-
;-----------------------------------------------------------------------------------------------------
;				ANÁLISIS DE RESULTADOS
;-----------------------------------------------------------------------------------------------------
;Recibir el nombre y el monto a quien se le extiende el cheque: B
;Desplegar caracteres ASCII de rayita para mostrar el chque: B
;Desplegar la fecha: B
;Desplegar el monto en letras como números: A
;-----------------------------------------------------------------------------------------------------
todo segment

 assume  cs:todo, ds:todo, ss:todo

 org 100h
		 
start: jmp inicio 

	Receptor    db 40 dup(0)																		    ;A quien se dirige el cheque
	MsjError    db "[Error]: Se debe ingresar el nombre y el monto",10,13                                ;Mensaje de error
				db "Los datos se ingresan de la siguiente forma: [nombre] [apellido] [monto]",10,13,"$"	;Mensaje de error con ayuda

	NomBanco    db "BANCO DE LA GRATITUD DEL UNIVERSO",10,13,"$"										;Nombre del banco
	Emisor      db "CLIENTE EMISOR: DARIO VARGAS",10,13,"$"												;El cliente emisor
	AcercaDe    db "PROGRAMA QUE IMPRIME UN CHEQUE",10,13
				db "PROGRAMA CREADO POR DARIO VARGAS MONTOYA",10,13,10,13,"$"							    

	MsjReceptor db "RECEPTOR: $"
	MsjFecha	db "FECHA: $"
	MsjMonto	db "MONTO: $"

	Date		dw 6 dup(0)
	
	num			db 8 dup(0)

	Cero		db "CERO $"
	Uno			db "UNO $"
	Dos 		db "DOS $"
	Tres 		db "TRES $"
	Cuatro 		db "CUATRO $"
	Cinco 		db "CINCO $"
	Seis 		db "SEIS $"
	Siete 		db "SIETE $"
	Ocho 		db "OCHO $"
	Nueve 		db "NUEVE $"
	Diez 		db "DIEZ $"

	Once		db "ONCE $"
	Doce		db "DOCE $"
	Trece		db "TRECE $"
	Catorce		db "CATORCE $"
	Quince		db "QUINCE $"

	Veinte		db "VEINTE $"
	Veinti		db "VEINTI$"
	Treinta 	db "TREINTA $"
	Cuarenta	db "CUARENTA $"
	Cincuenta	db " CINCUENTA $"
	Sesenta		db "SESENTA $"
	Setenta 	db "SETENTA $"
	Ochenta 	db "OCHENTA $"
	Noventa		db "NOVENTA $"

	Cien			db "CIEN $"
	Doscientos		db "DOSCIENTOS $"
	Trescientos		db "TRESCIENTOS $"
	Cuatroscientos	db "CUATROSCIENTOS $"
	Quinientos		db "QUINIENTOS $"
	Seiscientos		db "SEISCIENTOS $"
	Setescientos	db "SETESCIENTOS $"
	Ochoscientos	db "OCHOSCIENTOS $"
	Novescientos	db "NOVESCIENTOS $"

	Mil			db "MIL $"
	Ciento		db "CIENTO $"
	Dieci		db "DIECI$"
	Y			db "Y $"


 R db "Auxilio!$"   
																	
 inicio:
		call VerifEntry
		cmp cx, 1 						;Existe error?
		je fin							;Finaliza el programa
		
		mov ah,02h
		mov dx, 205
		mov cx, 80
		L1:	int 21h
			loop L1 


		call printCheck

		call newLn
		mov ah, 02h
		mov dx, 205
		mov cx, 80
		L2:	int 21h
			loop L2 
	fin: 
		mov ax, 4C00h
		int 21h 

;-------------------------------------------------
;Procedimiento que convierte de int a ascii
;Recibe en el [ax] el numero.
;-------------------------------------------------
	ItoA proc
		push bx
		push dx
		push di
					
		xor dx, dx 
		xor cx, cx
		mov bx, 10
		ciclo_conv:		div bx				;Convierto el numero a ascii
						add dx, "0"
						push dx
						xor dx,dx
						inc cx
						cmp ax, 0
						jne ciclo_conv

		mov bx, cx
		lea di, num
		fin_conv:	pop dx					;Copio el numero a una variable
					mov byte ptr[di], dl
					inc di
					loop fin_conv
		mov cx, bx
		pop di
		pop dx
		pop bx	
		ret
	ItoA endp
	
;-------------------------------------------------
;Procedimiento que imprime espacios
;-------------------------------------------------
	newLn proc
		push ax
		push dx
			xor dx,dx
			mov ah, 02h
			mov dl, 10
			int 21h
			mov dl, 13
			int 21h
		pop dx
		pop ax
		ret
	newLn endp

;---------------------------------------------------	
;Procedimiento que Obtiene la fecha 
;Retorna la fecha en una área de memoria (Date)
;---------------------------------------------------
	getDate proc
		push ax
		push cx
		push dx
		push es
		push si

			mov ah, 2Ah
			int 21h

			mov bx, cx
			lea di, Date

			xor ah, ah
			mov al, dl 								;Convierte el dia
			call ItoA
			lea si, num

			LD1:	mov al, byte ptr [si]
					mov byte ptr [di], al
					inc di
					inc si
					loop LD1

			mov byte ptr [di], "/"					;Coloca la barra de la fecha
			inc di									;Incrementa el puntero en el area de memoria

			xor ah, ah								
			mov al, dh								;Convierte el mes
			call ItoA
			lea si, num	
			LD2:	mov al, byte ptr [si]
					mov byte ptr [di], al
					inc di
					inc si
					loop LD1										

			mov byte ptr [di], "/"					;Coloca la barra de la fecha
			inc di									;Incrementa el puntero en el area de memoria

			mov ax, bx								;Convierte el año
			call ItoA
			xor ah, ah
			lea si, num
			LD3:	mov al, byte ptr [si]
					mov byte ptr [di], al
					inc di
					inc si
					loop LD3
			
			mov byte ptr [di], "$"

		pop si
		pop es
		pop dx
		pop cx
		pop ax
		ret
	getDate endp

;---------------------------------------------------	
;Imprime las unidades 
;---------------------------------------------------
	printU proc
		cmp byte ptr es:[si], "0"
		je Zero
		cmp byte ptr es:[si], "1"
		je One	
		cmp byte ptr es:[si], "2"
		je Two
		cmp byte ptr es:[si], "3"
		je Three
		cmp byte ptr es:[si], "4"
		je Four
		cmp byte ptr es:[si], "5"
		je Five
		cmp byte ptr es:[si], "6"
		je Six
		cmp byte ptr es:[si], "7"
		je Seven
		cmp byte ptr es:[si], "8"
		je Eight
		cmp byte ptr es:[si], "9"
		je Nine

		Zero:	cmp byte ptr es:[si-1], " "
				jne endU
				lea dx, Cero
				jmp PrntU

		One:	lea dx, Uno	
				jmp PrntU

		Two:	lea dx, Dos
				jmp PrntU
		
		Three:	lea dx, Tres
				jmp PrntU

		Four:	lea dx, Cuatro
				jmp PrntU

		Five:	lea dx, Cinco	
				jmp PrntU

		Six:	lea dx, Seis
				jmp PrntU
		
		Seven:	lea dx, Siete
				jmp PrntU
		
		Eight:	lea dx, Ocho
				jmp PrntU
		
		Nine:	lea dx, Nueve
				jmp PrntU

		PrntU:	int 21h
		endU:	ret
	printU endp

;---------------------------------------------------	
;Imprime las decenas
;---------------------------------------------------
	printD proc
		cmp byte ptr es:[si], "1"
		je OneD	
		jmp addY

		OneD:	cmp byte ptr es:[si+1], "0"
				je Ten
				cmp byte ptr es:[si+1], "1"
				je Eleven
				cmp byte ptr es:[si+1], "2"
				je Twelve 
				cmp byte ptr es:[si+1], "3"
				je Thirteen
				cmp byte ptr es:[si+1], "4"
				je Fourteen	
				cmp byte ptr es:[si+1], "5"
				je Fifteen
				jmp DieciD


		Ten:	lea dx, Diez
				jmp prntD

		Eleven:	lea dx, Once
				jmp prntD

		Twelve:	lea dx, Doce
				jmp prntD

		Thirteen:	lea dx, Trece
					jmp prntD
					
		fourteen:	lea dx, Catorce
					jmp prntD

		Fifteen:	lea dx, Quince
					jmp prntD	

		addY:	cmp byte ptr es:[si], "2"
				je TwoD
				cmp byte ptr es:[si], "3"
				je ThreeD
				cmp byte ptr es:[si], "4"
				je FourD
				cmp byte ptr es:[si], "5"
				je FiveD
				cmp byte ptr es:[si], "6"
				je SixD
				cmp byte ptr es:[si], "7"
				je SevenD
				cmp byte ptr es:[si], "8"
				je EightD
				cmp byte ptr es:[si], "9"
				je NineD
				jmp ZeroD

		TwoD:	cmp byte ptr es:[si+1], "0"
				lea dx, Veinte
				je prntD
				lea dx, Veinti
				jmp prntNum


		ThreeD:	cmp byte ptr es:[si+1], "0"
				lea dx, Treinta
				je prntD
				jmp printY

		FourD:	cmp byte ptr es:[si+1], "0"
				lea dx, Cuarenta
				je prntD
				jmp printY

		FiveD:	cmp byte ptr es:[si+1], "0"
				lea dx, Cincuenta
				je prntD
				jmp printY

		SixD:	cmp byte ptr es:[si+1], "0"
				lea dx, Sesenta
				je prntD
				jmp printY

		SevenD:	cmp byte ptr es:[si+1], "0"
				lea dx, Setenta
				je prntD
				jmp printY

		EightD:	cmp byte ptr es:[si+1], "0"
				lea dx, Ochenta
				je prntD
				jmp printY

		NineD:	cmp byte ptr es:[si+1], "0"
				lea dx, Noventa
				je prntD
				jmp printY

		printY:	int 21h
				lea dx, Y
				jmp prntNum
		
		ZeroD:	cmp byte ptr es:[si+1],"0"
				je endD
				
				jne prntNum2

		DieciD:	lea dx, Dieci
				jmp prntNum

		prntD:	
				int 21h
		endD:	ret
					
		prntNum:	int 21h
					inc si
					call printU
					
					jmp endD


		
		prntNum2:	inc si
					call printU
					jmp endD
	printD endp

;---------------------------------------------------	
;Imprime las centenas
;---------------------------------------------------
	printC proc
		cmp byte ptr es:[si], "1"
		je oneH
		cmp byte ptr es:[si], "2"
		je twoH
		cmp byte ptr es:[si], "3"
		je threeH
		cmp byte ptr es:[si], "4"
		je	fourH
		cmp byte ptr es:[si], "5"
		je	fiveH
		cmp byte ptr es:[si], "6"
		je	sixH
		cmp byte ptr es:[si], "7"
		je	sevenH
		cmp byte ptr es:[si], "8"
		je	eightH
		cmp byte ptr es:[si], "9"
		je	nineH
		jmp zeroH

		oneH:	call isClosedNum
				cmp dx, 2
				lea dx, Ciento
				jnz prntNumC
				lea dx, Cien
				jmp prntH

		twoH:	call isClosedNum
				cmp dx, 2
				lea dx, Doscientos
				jnz prntNumC
				jmp prntH

		threeH:	call isClosedNum
				cmp dx, 2
				lea dx, Trescientos
				jnz prntNumC
				jmp prntH

		fourH: call isClosedNum
				cmp dx, 2
				lea dx, Cuatroscientos
				jnz prntNumC
				jmp prntH

		fiveH:	call isClosedNum
				cmp dx, 2
				lea dx, Quinientos
				jnz prntNumC
				jmp prntH

		sixH:call isClosedNum
				cmp dx, 2
				lea dx, Seiscientos
				jnz prntNumC
				jmp prntH

		sevenH:call isClosedNum
				cmp dx, 2
				lea dx, Setescientos
				jnz prntNumC
				jmp prntH
				
		eightH:	call isClosedNum
				cmp dx, 2
				lea dx, Ochoscientos
				jnz prntNumC
				jz prntH

		nineH:	call isClosedNum
				cmp dx, 2
				lea dx, Novescientos
				jnz prntNumC
				jz prntH

		prntNumC:	int 21h
					inc si
					call printD
					jmp zeroH

		prntH:	int 21h

		zeroH: ret
	printC endp

;---------------------------------------------------	
;Imprime las unidades de millar
;---------------------------------------------------
	printUM proc
		cmp byte ptr es:[si], "1"
		je printMil
		cmp byte ptr es:[si], "2"
		je twoUM
		cmp byte ptr es:[si], "3"
		je threeUM
		cmp byte ptr es:[si], "4"
		je	fourUM
		cmp byte ptr es:[si], "5"
		je	fiveUM
		cmp byte ptr es:[si], "6"
		je	sixUM
		cmp byte ptr es:[si], "7"
		je	sevenUM
		cmp byte ptr es:[si], "8"
		je	eightUM
		cmp byte ptr es:[si], "9"
		je	nineUM
		jmp printMil
		
		twoUM:	lea dx, Dos
				jmp prntUM

		threeUM:	lea dx, Tres
					jmp prntUM

		fourUM:	lea dx, Cuatro
				jmp prntUM
				
		fiveUM:	lea dx, Cinco
				jmp prntUM
		
		sixUM:	lea dx, Seis	
				jmp prntUM

		sevenUM:	lea dx, Siete
					jmp prntUM

		eightUM:	lea dx, Ocho
				jmp prntUM

		nineUM:	lea dx, Nueve
					
		prntUM:		int 21h
					jmp printMil

		printMil:	lea dx, Mil
					int 21h
		zeroUM:ret
	printUM endp

;---------------------------------------------------	
;Verifica que sea un numero cerrado
;Recibe: SI = Puntero al string del numero
;Retorna: DX = Unidades que se movio
;Retorna: SI = Apunta al digito que no es cero 
;---------------------------------------------------
	isClosedNum proc
		push ax
		xor dx, dx
		mov ax, si
		inc si
		cmp byte ptr es:[si], "0"
		jne EndIC

		LZ:	inc dx
			inc si
			cmp byte ptr es:[si], 0Dh
			je EndIC
			cmp byte ptr es:[si], "0"
			je LZ

		EndIC:	mov si, ax
				pop ax
				ret
	isClosedNum endp


;---------------------------------------------------	
;Procedimiento transforma un numero a palabra
;Recibe: cx = cantidad de unidades
;---------------------------------------------------	
	Num2Word proc
		mov ah, 09h
		LN2W:
			cmp cx, 1 
			je U
			cmp cx, 2
			je D
			cmp cx, 3
			je C 
			cmp cx, 4
			je UM
			cmp cx, 5
			je DC 

		U:	call printU
			jmp nextNum

		D:	call printD
			jmp nextNum
			
		C:	call printC
			jmp nextNum

		UM:	call printUM
			jmp nextNum

		DC: call printD
			lea dx, Mil
			int 21h
			dec cx
			jmp nextNum

		nextNum: 	dec cx
					inc si
					cmp cx, 0
					jg LN2W

		ret
	Num2Word endp

;---------------------------------------------------	
;Cuenta las unidades del monto ingresado en consola
;Retorna: cx = cantidad de unidades del monto 
;---------------------------------------------------		
	lenNum proc
		push es
		push si
		xor cx, cx
			LNum:
				inc cx
				inc si
				cmp byte ptr es:[si], 0Dh	;Caracter de finalizacion
				jne LNum
		pop si
		pop es
		ret 
	lenNum endp
;---------------------------------------------------	
;Verifica si se ingreso argumentos en la consola
;
;---------------------------------------------------	
	VerifEntry proc
			mov si, 80h					;Verifica que la entrada no este vacia
			mov cl, byte ptr es:[si]	;Mueve la cantidad de bytes ingresados en la consola 
			cmp cl, 0					;La cantidad de bytes ingresados es cero?
			je EntryError				;Si
			mov cx, 0					;Codigo de exito
			jmp endVerif				;No

		EntryError:
			mov ah, 09h			
			lea dx, AcercaDe		
			int 21h						;Imprime el acerca de
			lea dx, MsjError
			int 21h						;Imprime el mensaje de error
			mov cx, 1					;Codigo de error

		endVerif:	
			ret     
		
	VerifEntry endp

;---------------------------------------------------	
;Imprime el cheque en pantala
;---------------------------------------------------
	printCheck proc
		;Imprime el nombre del banco
				mov ah, 09h 				
				lea dx, NomBanco				
				int 21h							

		;Imprime el emisor
				Emi:	lea dx, Emisor
						int 21h

		;Imprime el receptor 
				add si, 2						
				lea di, Receptor				;Area de memoria donde se guarda el receptor 
				mov dx, 2						;Cantida de espacios que hay en la consola
				LName:							;Imprime el nombre del receptor
					mov al, byte ptr es:[si]	
					mov byte ptr [di], al		
					inc si
					inc di
					cmp al, " "					;Hay espacio?
					je espace					;Si 
					jne noEspace				;No
				espace:	dec dx
				noEspace:	cmp dx, 0			
							jne LName
				
				inc di
				mov byte ptr[di], "$"			;Caracter de finalizacion

				mov ah, 09h 				
				lea dx, MsjReceptor
				int 21h							;Imprime el label de receptor
				lea dx, Receptor
				int 21h							;Imprime el receptor

		;Imprime la fecha
				call newLn						;Imprime una nueva fila
				lea dx, MsjFecha							
				int 21h							;Imprime el label de la fecha
				call getDate					;Obtiene la fecha actual
				lea dx, Date					
				int 21h							;Imprime la fecha

		;Imprime la cantidad de dinero
				call newLn						;Nueva linea
				mov ah, 02h			
				mov dx, "$"			
				int 21h							;Imprime el signo de dolar
				mov dx, ":"					
				int 21h							;Imprime 2 puntos

			xor cx, cx
			lea di, num
			push si								;Guarda el valor de [si]
			LAmount:		
				mov ah, 02h				
				mov dl, byte ptr es:[si]
				mov byte ptr[di], dl
				int 21h							;Imprime el numero en pantalla
				inc di
				inc si
				inc cx
				cmp byte ptr es:[si], 0
				jne LAmount
			pop si								;Recupera el valor de [si]

		;Imprime la cantidad de dinero en palabras		
			call newLn 							;Nueva linea
			dec cx
			mov ah,09h					
			lea dx, MsjMonto            
			int 21h								;Imprime el label del monto

			call lenNum
			call Num2Word						
			ret
	printCheck endp


	 
todo ends

end start




















