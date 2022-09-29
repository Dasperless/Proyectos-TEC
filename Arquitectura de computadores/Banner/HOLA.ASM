DATOS SEGMENT
    HOLAMUNDO DB "HOLA MUNDO COMO ESTAN$"
DATOS ENDS

PILA SEGMENT stack 'stack'
    DW 256 DUP(?)
PILA ENDS

CODIGO SEGMENT
    ASSUME DS:DATOS, SS:PILA, CS:CODIGO
    MAIN: 
		mov ax, pila				;Mueve lo que tiene en la pila a [ax]
		mov ss, ax					;Mueve la pila al Stack Segment.
		mov ax, datos				
		mov ds, ax

        LEA DX, HOLAMUNDO
        MOV AH, 09H
        INT 21H
    FINAL:
        mov ax, 4C00h
		int 21h 
CODIGO ENDS
END MAIN