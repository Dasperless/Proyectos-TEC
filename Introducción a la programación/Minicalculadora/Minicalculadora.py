from tkinter import *
#Primero se realiza la interfáz gráfica.
root=Tk()
frame=Frame(root)
frame.pack()
#------------------Pantalla
resdisplay=StringVar()
resdisplay.set("0")
display=Entry(frame,textvariable=resdisplay,state=DISABLED)
display.grid(row=1, column=1, padx=5, pady=5,columnspan=4)
display.config(background="white", fg="#000000", justify="right")

#-------------------operaciones

#E:Un número y un string
#S:El resultaod de la operación
#R:No tiene restricciones
def click(num,op):

#obtener lo que se encuentra en la pantalla      
      obt_pantalla=resdisplay.get()

#Si la calculadora esta en cero concatena el operador matemático al cero para evitar errores
      if obt_pantalla=="0" and  num in {"-","+","/","//","%","*","**"} :
            resdisplay.set(obt_pantalla+num)

#Pone en 0 el display si se borra todos los strings y el display queda en 0
      elif obt_pantalla=="0" and num!="":
            resdisplay.set(num)

#Borra todo lo que se encuentra en el display y setea un 0

      elif op=="CE":
            resdisplay.set("0")

# Borra los números y operadores.Borra un espacio si el operador tiene 1 de largo y borra 2 espacios si el operador es de dos espacios
      elif op=="C":
            if len(obt_pantalla)>1:
                  if obt_pantalla[-2:] in {"//","**"}:
                        resdisplay.set(obt_pantalla[0:-2])
                  else:
                        resdisplay.set(obt_pantalla[0:-1])
            else:
                  resdisplay.set("0")

# Reemplaza el signo para evitar errores matemáticos si se seleccionan signos diferentes
      elif obt_pantalla[-1] in {"-","+","/","%","*"} and num in {"-","+","/","%","*","//","**"}:
            if obt_pantalla[-2:] in {"//","**"}:
                  resdisplay.set(obt_pantalla[0:-2]+num)
            else:
                  resdisplay.set(obt_pantalla[0:-1]+num)

#Si op diferente a igual concatena los numeros y los operadores sin repetirlos 
      elif op!="=" or  obt_pantalla[-1] in {"-","+","/","%","*","-1*("} and num in {"-","+","/","%","*","-1*("}:
            if  num in {"**","//","."} and obt_pantalla[-1] in {"*","/","."}:
            	resdisplay.set(obt_pantalla)
            elif obt_pantalla[-5:]=="-1*(" and num=="-1*(":
            	resdisplay.set(obt_pantalla)
            elif obt_pantalla[-1]=="(" and num==")":
            	resdisplay.set(obt_pantalla+"0"+num)
            elif "." in  resdisplay.get() and num==".":
            	resdisplay.set(obt_pantalla)
            else:
                resdisplay.set(obt_pantalla+num)
      else:
            try:
                  try:
                        try:
                              operacion=eval(obt_pantalla)
                              resdisplay.set(operacion)
                              
                        except TypeError:
                              print("Debe colocar todos los operadores matemáticas ejemplo: 3*(2+5)")
                  except ZeroDivisionError:
                        print("No se puede dividir por cero ")

            except SyntaxError:
                  print("Error de sintaxis")



#------------------Botones 2
elevar=Button(frame,text="**",width=4,command=lambda:click("**",""))
elevar.grid(row=2,column=1)
divent=Button(frame,text="//",width=4,command=lambda:click("//",""))
divent.grid(row=2,column=2)
modulo=Button(frame,text="%",width=4,command=lambda:click("%",""))
modulo.grid(row=2,column=3)
parent=Button(frame,text="(",width=4,command=lambda:click("(",""))
parent.grid(row=2,column=4)

#------------------Botones 3
CE=Button(frame, text="CE",width=4,command=lambda:click("","CE"))
CE.grid(row=3,column=1)
C=Button(frame,text="C",width=4,command=lambda:click("","C"))
C.grid(row=3,column=2)
div=Button(frame,text="/",width=4,command=lambda:click("/",""))
div.grid(row=3,column=3)
parent1=Button(frame,text=")",width=4,command=lambda:click(")",""))
parent1.grid(row=3,column=4)
#-----------------Botones 4
b7=Button(frame,text="7",width=4, command=lambda:click("7",""))
b7.grid(row=4,column=1)
b8=Button(frame,text="8",width=4,command=lambda:click("8",""))
b8.grid(row=4,column=2)
b9=Button(frame,text="9",width=4,command=lambda:click("9",""))
b9.grid(row=4,column=3)
mult=Button(frame,text="*",width=4,command=lambda:click("*",""))
mult.grid(row=4,column=4)

#-----------------Botones 5
b4=Button(frame,text="4",width=4,command=lambda:click("4",""))
b4.grid(row=5,column=1)
b5=Button(frame,text="5",width=4,command=lambda:click("5",""))
b5.grid(row=5,column=2)
b6=Button(frame,text="6",width=4,command=lambda:click("6",""))
b6.grid(row=5,column=3)
resta=Button(frame,text="-",width=4,command=lambda:click("-",""))
resta.grid(row=5,column=4)

#-----------------Botones 6
b1=Button(frame,text="1",width=4,command=lambda:click("1",""))
b1.grid(row=6,column=1)
b2=Button(frame,text="2",width=4,command=lambda:click("2",""))
b2.grid(row=6,column=2)
b3=Button(frame,text="3",width=4,command=lambda:click("3",""))
b3.grid(row=6,column=3)
suma=Button(frame,text="+",width=4,command=lambda:click("+",""))
suma.grid(row=6,column=4)

#-----------------Botones 7
minus=Button(frame,text="(-)",width=4,command=lambda:click("-1*(",""))
minus.grid(row=7,column=1)
b0=Button(frame,text="0",width=4,command=lambda:click("0",""))
b0.grid(row=7,column=2)
punto=Button(frame,text=".",width=4,command=lambda:click(".",""))
punto.grid(row=7,column=3)
igual=Button(frame,text="=",width=4,command=lambda:click("","="))
igual.grid(row=7,column=4)


root.mainloop()
