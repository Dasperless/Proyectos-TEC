;-----------------------------------------------------------------------------------------------------
;										TAREA DEL BANNER
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
; +Se ingresa en la consola de DOSBox el siguiente comando para compilarlo
;
; >tasm 18123226
;
; +Luego se enlaza de la siguiente manera
;
; >tlink 18123226
;
; +Para iniciar el programa debe ingresar el nombre del archivo seguido del mensaje a desplegar
; Ejemplo:
; >18123226 hola mundo
;
;-----------------------------------------------------------------------------------------------------
;									ANÁLISIS DE RESULTADOS
;-----------------------------------------------------------------------------------------------------
;----------------------------------------------------------------------------------
datos segment
	TEXT DB 258 DUP("$") 
	AVISO1 DB "No se ha igresado ningun mensaje",10,10,13,"$"
	TAM DB 1 DUP(0)
	MINIACERCADE	DB "PROGRAMA QUE DESPLIEGA UN BANNER QUE CAMBIA DE COLOR",10,13
					DB "CREADO POR DARIO VARGAS",10,13
					DB "PARA USAR INGRESE EL NOMBRE DEL ARCHIVO SEGUIDO DEL MENSAJE",10,13
					DB ">18123226 HOLA MUNDO",10,13,"$"
	PAUSA1 dw 1000
	PAUSA2 dw 100 ; En total hace de pausa 10000x2000=20 000 000 de nops	
datos endS

pila segment stack 'stack'
	dw 256 dup(?)
pila ends

codigo segment
	assume cs:codigo, ds:datos, ss:pila

;PROCEDIMIENTO QUE COMPRUEBA LA ENTRADA 
;RECIBE EN EL [ES] LA DIRECCION AL PSP
;RECIBE EN EL [DI] UN PUNTERO A LA DIRECCION DE MEMORIA
;RECIBE EN EL [CX] LA CANTIDAD DE CARACTERES A LEER
;RECIBE EN EL [SI] UN PUNTERO AL PRIMER CARACTER
ENTRADA PROC 
	PUSH AX
	PUSH CX

	
	CMP CX, 0									;ES LA CANTIDAD DE CARACTERES 0?
	JE NOENTRADA								;SI
	DEC CX										;QUITA CONTADOR DEL CARACTER ESPACIO
	MOV BYTE PTR TAM, CL

	CICLO_ENTRADA:	MOV AL, BYTE PTR ES:[SI]	;CARACTER EN LA COSOLA
					MOV BYTE PTR DS:[DI], AL	;COPIA EL CARACTER EN LA VARIABLE
					INC SI						;SIGUIENTE CARACTER CONSOLA
					INC DI						;SIGUIENTE ESPACIO EN MEMORIA
					LOOP CICLO_ENTRADA

	FIN_ENTRADA:	MOV BYTE PTR[DI],"$"		;FINALIZO CON EXITO
					POP CX
					POP AX
					RET

	NOENTRADA:	MOV BYTE PTR[DI],"$"			;NO SE INGRESO ENTRADA
				MOV AH, 09H
				LEA DX, AVISO1
				INT 21H
				LEA DX, MINIACERCADE
				INT 21h
				MOV DX, 68
				POP CX
				POP AX
				RET
ENTRADA ENDP

;PROCEDIMIENTO QUE MUESTRA LOS CARACTERES EN PANTALLA Y LOS MUEVE
MOVIMIENTO PROC
	INIT :MOV AH, 00H									;MODO DE PANTALLA
	MOV AL, 03H									;MODO 80 X 25
	INT 10H

	MOV AX, 0B800H								;Video RAM segment
	MOV ES, AX									
	XOR DI, DI									
	MOV AH, 14 									;COLOR
	
	ULT_COL:	MOV SI, 158						;ULTIMA COLUMNA

	CICLO_MOV:	MOV DX, WORD PTR ES:[SI]     	;SALVAMOS PANTALLA
				MOV CL, TAM						;TAMAÑO DEL STRING 
				MOV BX, SI						;ESPACIO ACTUAL EN PANTALLA
				XOR DI, DI						;EMPEZAMOS DESDE EL PRIMER CARACTER
				
	DESPLEGAR:	MOV AL, BYTE PTR TEXT[DI]		;CARACTER DEL PSP
				MOV WORD PTR ES:[BX], AX		;SE MUESTRA EN PANTALLA	
				ADD BX, 2						;SIGUIENTE ESPACIO EN PANTALLA	
				CMP BX, 158						;STRING ES MAS GRANDE QUE LA PANTALLA?
				JG PAUSA						;SI, NO MUESTRA EL SIGUIENTE CARACTER
				INC DI							;SIGUIENTE CARACTER
				LOOP DESPLEGAR			

	

	PAUSA:	MOV CX, PAUSA1      				; Hacemos una pausa de 100 x 1000 nops
	P1:     PUSH CX
			MOV CX, PAUSA2
	P2:     NOP
			LOOP P2
			POP CX
			LOOP P1
	MOV WORD PTR ES:[BX-2], DX
	
	SUB SI, 2									;COLUMNA A LA IZQUIERDA
	CMP SI, 2 						
	JE INIT

	PUSH AX										;GUARDO EL VALOR DE AX
	MOV AH,01H									;COMPROBAR SI EL CARACTER DE ESCAPE SE PRECIONO
	INT 16H
	JNZ HAY_TECLA
	POP AX
	JMP CICLO_MOV 

	HAY_TECLA: 	XOR AH,AH
				INT 16H
				CMP AL, 27 
				JE FIN_MOV

				CMP AL, 32
				JE CAMBCOLOR
				JMP CICLO_MOV	
				
	CAMBCOLOR:	POP AX			;RECUPERA EL VALOR DE AX
				CMP AH, 15		;ES EL COLOR MAYOR A 15?
				JE PRIMCOLOR	;SI?
				INC AH			;NO, SIGUIENTE COLOR
				JMP CICLO_MOV	

	PRIMCOLOR:	MOV AH, 0
				JMP CICLO_MOV

	FIN_MOV:	POP AX
				RET
MOVIMIENTO ENDP

MAIN:
	MOV AX, DS					;DIRECCION DEL PSP
	MOV ES, AX	

	MOV AX, datos				;PROTOCOLO DE INICIALIZACION
	MOV DS, AX
	MOV AX, pila
	MOV SS, AX

	LEA DI, TEXT				;PUNTERO A LA VARIABLE
	MOV SI, 80H					;PUNTERO A CANTIDAD DE CARACTERES EN CONSOLA
	XOR CX, CX
	MOV CL, BYTE PTR ES:[SI]	;CANTIDAD DE CARACTERES
	MOV SI, 82H					;DIRECCION AL PRIMER CARACTER
	CALL ENTRADA
	CMP DX, 68
	JE FINAL
	CALL MOVIMIENTO




FINAL:
	mov ax, 4C00h
	int 21h 
	


codigo ends
end main