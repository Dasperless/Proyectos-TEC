; Este es un programa que recibe en la linea de comando un string
; lo despliega con una secuencia de colores en la primera fila de la pantalla

datos segment

    Rot db 128 dup(?)

datos ends

                  
pila segment stack 'stack'

    dw 256 dup (?)

pila ends


codigo segment

    assume  cs:codigo, ds:datos, ss:pila
                                                                             
 inicio: push ds
         pop es
         mov ax, datos
         mov ds, ax
         mov ax, pila
         mov ss, ax

         mov si, 80h                ;DIRECCION DEL PSP
         mov cl, byte ptr ES:[si]   ;CANTIDAD DE CARACTERES
         xor ch, ch                 ;LIMPIA EL CH
         push cx                    ;GUARDA EL CX           
         xor di, di                 ;LIMPIA EL DI
         inc si                     ;SIGUIENTE CARACTER (ESPACIO)   ;EJ:COMANDO [NOMBRE ARCHV] HOLA MUNDO
         inc si                     ;SIGUIENTE CARACTER (LETRA)
   cic1: mov al, byte ptr ES:[si]   
         mov byte ptr Rot[di], al 
         inc si
         inc di
         loop cic1

         mov ax, 0B800h             ;VIDEO RAM SEGMENT     
         mov es, ax                 ;MUEVE EL VIDEO RAM SEGMENT AL ES
         pop cx                     ;RECUPERA EL VALOR DE CX
         dec cx                     ;LE RESTA UNO [ESPACIO EN BLANCO]
         xor di, di                 ;LIMPIA EL DI
         mov ah, 1                  
         mov si, 152
         
   cic2: mov al, byte ptr Rot[di]   ;MUEVE A [AL] EL CARACTER
         mov word ptr Es:[si], Ax   ;MUEVE  A LA PANTALLA EL CARACTER
         inc di
         
         add si,2 
         
         inc ah
         cmp ah,15
         jbe siga
         mov ah, 1           
   siga: loop cic2

         mov ax, 4C00h
         int 21h
     
codigo ends

end inicio