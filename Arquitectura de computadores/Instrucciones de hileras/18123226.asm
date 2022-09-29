datos segment
    p1 db "hola mundo.",0 ;10
    p2 db 39,"Ser o no ser string esa es la cuestion."
    p3 db "HOLA MUNDO",0
    p4 db 39,"SER O NO SER STRING ESA ES LA CUESTION."
    p5 db "ABCD",0
    p6 db "ABCDE",0
    p7 db "ABCD",0
    p8 db 4,"ABCD",0
    p9 db 4,"abcd",0
    find db "D",0
    destino db 128 dup (0)
datos ends

pila segment stack 'stack'
    dw 128 dup(?)
pila ends 

codigo segment
    assume cs:codigo, ds:datos, ss:pila

;--------------------------------------------------------------------------------
;Imprime en la salida estándar un string like C
;Recibe el string en el puntero DS:[SI]
prnstrC proc
;--------------------------------------------------------------------------------
push ds
push dx
push si
mov ah,02h  
ciclo_prnstrC:  mov dl,byte ptr [si]
                int 21h
                inc si
                cmp dl,0
                jne ciclo_prnstrC
pop si
pop dx
pop ds
ret
prnstrC endp

;--------------------------------------------------------------------------------
;Imprime en la salida estándar un string like Pascal
;Recibe el string en el puntero DS:[SI]
prnstrP proc
;--------------------------------------------------------------------------------
push ds
push dx
push cx
push si
mov ah,02h
xor ch,ch
mov cl, byte ptr [si]
; mov dl,cl
; int 21h
inc si
ciclo_prnstrP:  mov dl, byte ptr[si]
                int 21h
                inc si
                loop ciclo_prnstrP
pop si
pop cx
pop dx
pop ds
ret
prnstrP endp

;--------------------------------------------------------------------------------
;Recibe  punteros a memoria y copia el destino a la fuente en formato like C
;Recibe 2 punteros, el puntero fuente [si] y el destino [di]
cpystrC proc
;--------------------------------------------------------------------------------
push dx
push es
push si

mov ax,ds
mov es,ax
ciclo_cpystrC:  movsb   
                cmp byte ptr[si-1],0
                jne ciclo_cpystrC
pop si
pop es
pop dx
ret
cpystrC endp

;--------------------------------------------------------------------------------
;Recibe  punteros a memoria y copia el destino a la fuente en formato like Pascal
;Recibe 2 punteros, el puntero fuente [si] y el destino [di]
cpystrP proc
;--------------------------------------------------------------------------------
push ax
push es

xor ch,ch  
mov ax,ds
mov es,ax    
cld 
mov cl,byte ptr [si]
rep movsb

pop es
pop ax
ret
cpystrP endp

;--------------------------------------------------------------------------------
;Retorna la longitud de un string en formato like C
;Recibe el string en el puntero en el puntero DS:[si]
;Retorna la longitud en CX
lengthC proc
;-------------------------------------------------------------------------------- 
push si
xor cx,cx
xor ah,ah   
ciclo_lengthC:  inc cx
                inc si
                cmp byte ptr ds:[si],0
                jne ciclo_lengthC 
pop si
ret
lengthC endp

;--------------------------------------------------------------------------------
;Retorna la longitud de un string en formato like Pascal.
;Recibe el string en el puntero en el puntero DS:[si]
;Retorna la longitud en CX
lengthP proc
;-------------------------------------------------------------------------------- 
push si
xor cx,cx
mov cl,byte ptr[si]
pop si
ret
lengthP endp

;--------------------------------------------------------------------------------
;Pasa de minusculas a mayusculas un string like C
;Recibe el string en el puntero en el puntero DS:[si]
UpperCaseC proc
;-------------------------------------------------------------------------------- 
ciclo_UpperCaseC:       cmp byte ptr[si],0
                        je fin_UpperCaseC

                        cmp byte ptr[si],"a"
                        jge es_minusculaC
                        inc si
                        jmp ciclo_UpperCaseC

es_minusculaC:   cmp byte ptr[si],"z"
                jle mayuscula_UpperCaseC
                inc si
                jmp ciclo_UpperCaseC

mayuscula_UpperCaseC:   sub byte ptr[si]," "                       
                        mov dl,byte ptr[si]
                        inc si
                        jmp ciclo_UpperCaseC

fin_UpperCaseC: ret
UpperCaseC endp

;--------------------------------------------------------------------------------
;Pasa de minusculas a mayusculas un string like Pascal
;Recibe el string en el puntero en el puntero DS:[si]
UpperCaseP proc
;-------------------------------------------------------------------------------- 
xor cx,cx
mov cl,byte ptr[si]
inc si
ciclo_UpperCaseP:       cmp byte ptr[si],"a"
                        jge es_minusculaP
                        inc si
                        loop ciclo_UpperCaseC

es_minusculaP:   cmp byte ptr[si],"z"
                jle mayuscula_UpperCaseC
                inc si
                loop ciclo_UpperCaseC

mayuscula_UpperCaseP:   sub byte ptr[si]," "                       
                        mov dl,byte ptr[si]
                        inc si
                        loop ciclo_UpperCaseP

fin_UpperCaseP: ret
UpperCaseP endp

;--------------------------------------------------------------------------------
;Pasa de mayusculas a minusculas un string like C
;Recibe el string en el puntero en el puntero DS:[si]
LowerCaseC proc
;-------------------------------------------------------------------------------- 
ciclo_lowerCaseC:       cmp byte ptr[si],0
                        je fin_LowerCaseC

                        cmp byte ptr[si],"A"
                        jge es_mayusculaC
                        inc si
                        jmp ciclo_lowerCaseC

es_mayusculaC:  cmp byte ptr[si],"Z"
                jle minuscula_lowercaseC
                inc si
                jmp ciclo_lowerCaseC

minuscula_lowercaseC:   add byte ptr[si]," "                       
                        mov dl,byte ptr[si]
                        inc si
                        jmp ciclo_lowerCaseC

fin_LowerCaseC: ret
LowerCaseC endp

;--------------------------------------------------------------------------------
;Pasa de mayusculas a minusculas un string like Pascal
;Recibe el string en el puntero en el puntero DS:[si]
LowerCaseP proc
;-------------------------------------------------------------------------------- 
xor cx,cx
mov cl,byte ptr[si]
inc si
ciclo_lowerCaseP:       cmp byte ptr[si],"A"
                        jge es_mayusculaP
                        inc si
                        loop ciclo_lowerCaseP

es_mayusculaP:  cmp byte ptr[si],"Z"
                jle minuscula_lowercaseP
                inc si
                loop ciclo_lowerCaseP

minuscula_lowercaseP:   add byte ptr[si]," "                       
                        mov dl,byte ptr[si]
                        inc si
                        loop ciclo_lowerCaseP

fin_LowerCaseP: ret
LowerCaseP endp

;--------------------------------------------------------------------------------
;Concatena 2 strings en formato like C.
;Recibe los strings a concatenar en si y bx.
;Retorna la concatenacion en di.
;Se asume que el di tiene suficiente espacio para almacenarlo.
ConcatC proc
;-------------------------------------------------------------------------------- 
 
; push ax
; push bx
; push es
; push si
mov ax,ds
mov es,ax
cld
copiarSi_ConcatC:       cmp byte ptr[si],0
                        mov dl,byte ptr[si]
                        je copiarBX_ConcatC
                        ; je fin_ConcatC
                        movsb 
                        jmp copiarSi_ConcatC

copiarBX_ConcatC:       cmp byte ptr[bx],0
                        je fin_ConcatC
                        mov al,byte ptr[bx]
                        stosb
                        inc bx
                        jmp copiarSi_ConcatC

fin_ConcatC:    ;pop si
                ; pop es
                ; pop bx
                ; pop ax
                ret
ConcatC endp

;--------------------------------------------------------------------------------
;Concatena 2 strings en formato like Pascal.
;Recibe los strings a concatenar en si y bx.
;Retorna la concatenacion en di.
;Se asume que el di tiene suficiente espacio para almacenarlo.
ConcatP proc
;-------------------------------------------------------------------------------- 
 
push ax
push bx
push es
push si
mov ax,ds
mov es,ax 

mov al,byte ptr ds:[si]         ;Mueve a [al] el tamaño del primer string
add al,byte ptr [bx]            ;Suma en [al] el tamaño del segundo sting
mov byte ptr es:[di],al         ;Mueve a [di] el tamaño del nuevo string
inc di
inc si
inc bx

xor ch,ch
mov cl,byte ptr ds:[si-1]
rep movsb

xor ch,ch
mov cl,byte ptr ds:[bx-1]
mov si,bx
rep movsb


fin_ConcatP:    pop si
                pop es
                pop bx
                pop ax
                ret
ConcatP endp

;--------------------------------------------------------------------------------
;Compara el string el tamaño del string en SI con el de DI.
;Regresa 1 si es mayor, 0 si es igual y -1 menor.
;Recibe el primer string en el  ES:[si] y el segundo en ES:[SI]
cmpstrC proc
;-------------------------------------------------------------------------------- 
push di
push si
verif_cmpstrC:  mov al,byte ptr[si]     
                mov dl,byte ptr[di]
                cmp al,0                ;Final strig?
                jne sig_cmpstrC         ;no
                cmp dl,0                ;Final del string2?
                jne sig_cmpstrC         ;no
                jmp bandera_cmpstrC     ;si, termina con ZF=1

sig_cmpstrC:    inc si                  ;Incrementa el si
                inc di                  ;Incrementa el di
                cmp al,dl               ;Son iguales?
                je verif_cmpstrC        ;si: continua le ciclo
                                        ;No: termiana con banderas activadas                

bandera_cmpstrC:        jz igual_cmpstrC        ;Son iguales
                        jnz menor_cmpstrC       ;No son iguales

igual_cmpstrC:  mov al,0       
                jmp fin_cmpstrC

menor_cmpstrC:  jnc mayor_cmpstrC        ;Es mayor?
                mov al,-1               ;No
                jmp fin_cmpstrC

mayor_cmpstrC:  mov al,1                        
                jmp fin_cmpstrC 

fin_cmpstrC:    pop di
                pop si
                ret
cmpstrC endp

;--------------------------------------------------------------------------------
;Compara el string el tamaño del string en SI con el de DI.
;Regresa 1 si es mayor, 0 si es igual y -1 menor.
;Recibe el primer string en el  ES:[si] y el segundo en ES:[SI]
cmpstrP proc
;-------------------------------------------------------------------------------- 
push cx
push di
push dx
push es
push si
mov ax,ds
mov es,ax
mov al,byte ptr[si]     ;Tamaño del primer string.
mov dl,byte ptr[di]     ;Tamaño del segundo string
cmp al,dl               ;Es el primer string mayor que el segundo?
jge  mayor_cmpstrP        ;Si
jl menor_cmpstrP        ;No        

mayor_cmpstrP:  mov cl,al
                jmp verif_cmpstrP

menor_cmpstrP:  mov cl,dl
                jmp verif_cmpstrP

verif_cmpstrP:  cld     ;Direccion = avanzar
                xor ch,ch
                rep cmpsb   
                jb es_menor
                jz es_igual
                ja es_mayor

es_menor:       mov al,-1
                jmp fin_cmpstrP

es_igual:       mov al,0
                jmp fin_cmpstrP

es_mayor:       mov al,1
                jmp fin_cmpstrP

fin_cmpstrP:    pop si
                pop es
                pop dx
                pop di
                pop cx
                ret
cmpstrP endp

;--------------------------------------------------------------------------------
;Regresa la posición de un caracter en un string en formato like C
;Recibe el string en [si] y el caracter a buscar en [Al]
;La posición se retorna en [CL]
findcharC proc
;--------------------------------------------------------------------------------
push di
push si

mov dx,ds
mov es,dx

mov di,si
call lengthC 
add di,cx
dec di
std
xor ch,ch
repne scasb
jnz not_found
jz found

not_found:      mov cl,-1
                jmp fin_findcharC

found:  jmp fin_findcharC

fin_findcharC:    pop si
        pop di
        ret
findcharC endp


;--------------------------------------------------------------------------------
;Regresa la posición de un caracter en un string en formato like Pascal
;Recibe el string en [si] y el caracter a buscar en [Al]
;La posición se retorna en [CL]
findcharP proc
;--------------------------------------------------------------------------------
push di
push es
push si

mov dx,ds
mov es,dx

xor dx,dx
xor cx,cx
mov di,si
mov cl,byte ptr[di]
add di,cx

std
repne scasb
jnz notfound_findcharP
jmp fin_findcharP
notfound_findcharP:     mov cl,-1
                        jmp fin_findcharP

fin_findcharP:  pop si
                pop es
                pop di
                ret

findcharP endp
main:   mov ax, pila
        mov ss, ax
        mov ax, datos
        mov ds,ax


;--------------------------------------------------------------------------------
; prnstr
;--------------------------------------------------------------------------------
        ; lea si,p1     
        ; call prnstrC  

        ; lea si,p2
        ; call prnstrP

;--------------------------------------------------------------------------------
; cpystr
;--------------------------------------------------------------------------------        
        ; lea si, p1
        ; lea di,destino
        ; call cpystrC

        ; lea si,destino    
        ; call prnstrC 

        ; lea si, p2
        ; lea di,destino
        ; call cpystrP        

        ; lea si,destino    
        ; call prnstrP
;--------------------------------------------------------------------------------
; length
;--------------------------------------------------------------------------------   
        ; lea si, p1
        ; lea di,destino
        ; call lengthC    
        ; mov ah,02h
        ; mov dl,cl
        ; int 21h   

        ; lea si, p2
        ; lea di,destino
        ; call lengthP
        ; mov ah,02h
        ; mov dl,cl
        ; int 21h   
;--------------------------------------------------------------------------------
; UpperCase
        ; lea bx,p4
;--------------------------------------------------------------------------------  
        ; lea si,p1
        ; call UpperCaseC
        ; lea si,p1
        ; call prnstrC

        ; lea si,p2
        ; call UpperCaseP
        ; lea si,p2
        ; call prnstrP     

;--------------------------------------------------------------------------------
; LowerCase
;--------------------------------------------------------------------------------  
        ; lea si,p3
        ; call LowerCaseC
        ; lea si,p3
        ; call prnstrC

        ; lea si,p4
        ; call LowerCaseP
        ; lea si,p4
        ; call prnstrP

;--------------------------------------------------------------------------------
; Concat
;--------------------------------------------------------------------------------  
        ; lea si,p1
        ; lea bx,p3
        ; lea di,destino
        ; call ConcatC
        ; lea si,destino
        ; call prnstrC

        ; lea si,p2
        ; lea di,destino
        ; call ConcatP
        ; lea si,destino
        ; call prnstrP  

;--------------------------------------------------------------------------------
; Cmpstr
;--------------------------------------------------------------------------------                
        ; lea si,p7
        ; lea di,p5
        ; call cmpstrC
        ; mov ah,02h
        ; mov dl,al
        ; add dl,"0"
        ; int 21h

        ; lea si,p8
        ; lea di,p9
        ; call cmpstrP
        ; mov ah,02h
        ; mov dl,al
        ; add dl,"0"
        ; int 21h        
;--------------------------------------------------------------------------------
; Findchar
;--------------------------------------------------------------------------------  
        ; mov al,find
        ; lea si,p5
        ; call findcharC
        ; mov dl,cl
        ; add dl,"0"
        ; mov ah,02h
        ; int 21h

        ; mov al,find
        ; lea si,p8
        ; call findcharP
        ; mov dl,cl
        ; add dl,"0"
        ; mov ah,02h
        ; int 21h

fin:    mov ax,4c00h
        int 21h
codigo ends
end main


