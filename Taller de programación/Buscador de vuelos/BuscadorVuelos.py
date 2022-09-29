from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random,string

#------------------------------------------------Generar ID
#E: Ninguna 
#S:Un número de ID consecutivo 
#R:Ninguna
def ID():
        archivo="archivos\ID.txt"
        numID=int(abrir(archivo))
        sumID=nuevoID(archivo,numID+1)
        return numID

#-------------------------------------------------Añadir Aerolinea
#E:Un string (Aerolinea)
#S:Añade una nueva aerolinea con su respectivo ID 
#R:La aerolinea no puede ser un string vacío
def añadirAerolineas(aerolinea):
        if aerolinea!="":
                archivo="archivos\Aerolineas.txt"
                if not existe(aerolinea):
                        añadir(archivo,[ID(),aerolinea])
                        messagebox.showinfo("Añadir contenido", "Se ha añadido una nueva aerolinea")
                else:
                        messagebox.showinfo("Error", "La aerolinea ya existe")
        else:
                messagebox.showinfo("Error", "Debe ingresar una aerolinea")

#-------------------------------------------------Largo de una lista
#E:Una lista(lista)
#S:La cantidad de elementos de una lista
#R:La entrada debe ser una lista
def largo(lista):
        res=0
        while lista!=[]:
                lista=lista[1:]
                res+=1
        return res
#-------------------------------------------------Añadir contenido a un .txt
#E:Un string(archivo) y una lista(contenido)
#S:Agrega el contenido de una lista en un archivo .txt
#R:El archivo debe ser un string y el contenido una lista
def añadir(archivo,contenido):
        txt=open(archivo,"a")
        while contenido!=[]:
                if largo(contenido)>1:
                        txt.write(str(contenido[0])+",")
                else:
                        txt.write(str(contenido[0])+"\n")
                contenido=contenido[1:]
        txt.close()
        messagebox.showinfo("Añadir contenido", "El contenido ha sido añadido")
        
#-------------------------------------------------Modificar el ID del archivo .txt
#E:un string (archivo) y un número(contenido)
#S:Crea un nuevo Id y lo guarda en un archivo .txt
#R:El archivo debe ser un string y el contenido una número       
def nuevoID(archivo,contenido):
         txt=open(archivo,"w")
         txt.write(str(contenido))
         txt.close()
         
#-------------------------------------------------Verificar existencia 
#E:un string (nuevo)
#S:Verifica si una aerolinea ya existe en e archivo .txt
#R:Nuevo debe ser un string
def existe(nuevo):
        txt=crearLista("archivos\Aerolineas.txt")
        while txt!=[]:
                if nuevo==txt[0][1]:
                        return True
                txt=txt[1:]
        return False

#-------------------------------------------------Obtener el id de una aerolinea
#E:un string (aerolinea)
#S:retorna el ID que le pertenece a una aerolinea dentro de un archivo .txt
#R:aerolinea debe ser un string
def obtenerID(aerolinea):
        txt=crearLista("archivos\Aerolineas.txt")         
        res=[]
        while txt!=[]:
                if aerolinea==txt[0][1]:
                        return txt[0][0]
                txt=txt[1:]
        return ""

#-------------------------------------------------Escribir contenido en un txt
#E:un string (archivo), una lista(contenido) y una ventana(root)
#S:elimina el contenido de un archivo  .txt para escribir uno nuevo y refresar la ventana
#R:archivo debe ser un string, contenido debe ser una lista y root una ventana (Tk())              
def escribir(archivo,contenido,root):
        txt=open(archivo,"w")
        while contenido!=[]:
                if archivo == "archivos\Aerolineas.txt":
                        txt.write(contenido[0].split(",")[0]+","+contenido[0].split(",")[1]+"\n")
                elif archivo=="archivos\Vuelos.txt":
                        txt.write(contenido[0][0]+","+contenido[0][1]+","+contenido[0][2]+","+contenido[0][3]+","+contenido[0][4]+","+contenido[0][5]+","+contenido[0][6]+","+contenido[0][7]+"\n")                    
                contenido=contenido[1:]
        txt.close()
        return actualizar(archivo,root)

#-------------------------------------------------Actualizar Ventana
#E:un string (archivo) y una ventana(root)
#S:Actualiza el menu de eliminar archivo
#R:archivo debe ser un string, y root una ventana(Tk())
def actualizar(archivo,root):
        return menuEliminar(archivo,root)


#-------------------------------------------------Abrir archivo txt
#E:un string (archivo) y una ventana(root)
#S:Actualiza el menu de eliminar archivo
#R:archivo debe ser un string, y root una ventana(Tk())        
def abrir(archivo):
        txt=open(archivo,"r")
        contenido=txt.read()
        return contenido

#-------------------------------------------------Crear lista de un archivo .txt
#E:un string (archivo)
#S:Una lista con los elementos de un archivo.txt
#R:archivo debe ser un string con la ruta del archivo .txt
def crearLista(archivo):
        txt=open(archivo,"r")
        contenido=txt.read()
        lista=contenido.split("\n")
        resultado=recortar(lista)
        return limpiarLista(resultado)

#-------------------------------------------------Limpiar lista de comillas
#E:una lista(lista)
#S:una nueva lista sin comillas dobles dentro de sus elmentos
#R:lista debe ser una lista     
def limpiarLista(lista):
        res=[]
        while lista!=[]:
                if lista[0]!=[''] :
                        res+=[lista[0]]
                lista=lista[1:]
        return res

#-------------------------------------------------Recortar string
#E:una lista (lista)
#S:Una lista de listas con string separados por comas (,)
#R:lista debe ser una lista
def recortar(lista):
        res=[]
        while lista!=[]:
                res+=[lista[0].split(",")]
                lista=lista[1:]
        return res

#-------------------------------------------------Mostrar aerolineas
#E:una lista
#S:una lista con los nombres de las aerolineas
#R:lista debe ser una lista
def mostrarAerolineas(lista):
        res=[]
        while lista!=[]:
                res+=[lista[0][1]]
                lista=lista[1:]
        return res

#-------------------------------------------------Generar número de vuelo
#E:un numero (n)
#S:un número de vuelo de 4 a 8 digito con caracteres y números aleatoreos
#R:n debe ser un número entero
def numeroVuelo(n):
        alfanumerico=''.join(random.choices(string.ascii_uppercase  + string.digits, k=n))
        return alfanumerico

#-------------------------------------------------Generar un número random
#E:Ninguna
#S:Una lista con los elementos de un archivo.txt
#R:archivo debe ser un string con la ruta del archivo .txt
def numeroRandom():
        return random.randint(4,8)

#-------------------------------------------------Lista de años
#E:Ninguna
#S:Una lista con años que abarcan de 1990 hasta 2050
#R:Ninguna
def listaAño():
        año=1990
        res=[]
        while año<2050:
                res+=[año]
                año+=1
        return res



#-------------------------------------------------Añadir Vuelos
#E:numero devuelo,dia,mes año,origen,destino,hora de partida, hora de llegada, id y el precio (strings)
#S:añade nuevos vuelos a un archivo .txt
#R:Ninguna
def vuelos(numeroVuelo,dia,mes,año,origen,destino,horaPartida,horaLlegada,ID,Precio):
        if dia!="" and mes!="" and año!="" and origen!="" and destino!="" and horaPartida !="" and horaLlegada!="" and ID!="" and Precio!="":
                if destino!=origen:
                        fecha=dia+"/"+mes+"/"+año
                        archivo="archivos\Vuelos.txt"
                        aerolineas=crearLista("archivos\Aerolineas.txt")
                        contenido=[numeroVuelo,fecha,origen,destino,horaPartida,horaLlegada,ID,Precio]
                        añadirVuelos=añadir(archivo,contenido)
                else:
                        messagebox.showinfo("Error", "El origen y el destino no pueden ser el mismo")
                        
        else:
                messagebox.showinfo("Error", "Ningún parámetro puede estar vacío ")
                


#-------------------------------------------------Login
#E:una ventana(Tk())
#S:Muestra una interfaz donde se elige el rol de administrador o de usuario
#R:root debe ser una ventana(Tk())                
def login(root):
        #------------------------Interfaz
        root.geometry("640x360")
        root.title("Buscador de vuelos")
        root.resizable(width=False, height=False)
        root.iconbitmap("interfaz\logo.ico")

        #----------------------Botones Login
        adminimg=PhotoImage(file = "interfaz\Admin1.png")
        usuarioimg=PhotoImage(file = "interfaz\ImgUsuario1.png")
        admin= Button(root, image=adminimg,width=320,height=360,command=lambda:administrador(Toplevel(root))).place(x=0,y=0)
        user=Button(root,image=usuarioimg,width=320,height=360,command=lambda:usuario(Toplevel(root))).place(x=320,y=0)
        root.mainloop()

#-------------------------------------------------Administrador
#E:una ventana (Tk())
#S:Genera una ventana donde se puede añadir vuelos y aerolineas además de varias opciones de gestion.
#R:root debe ser una ventana(Tk())
def administrador(root):
        root.geometry("660x320")
        root.title("Administración")
        root.resizable(width=False, height=False)
        root.iconbitmap("interfaz\logo.ico")

        incluiraerolineas=Label(root, text="Incluir aerolineas",font=("Century",14)).place(x=30,y=20)
        inputaerolineasstr=StringVar()
        inputaerolineas=Entry(root,textvariable=inputaerolineasstr,width=30).place(x=20,y=60)
        archivoAerolineas="archivos\Aerolineas.txt"
        aerolineasE=ttk.Button(root,text="Eliminar",command=lambda:menuEliminar(archivoAerolineas,Toplevel(root)))
        aerolineasE.place(x=20,y=80)
        aerolineasG=ttk.Button(root,text="Guardar",command=lambda:añadirAerolineas(inputaerolineasstr.get()))
        aerolineasG.place(x=100,y=80)

        incluirVuelos=Label(root,text="Incluir Vuelos",font=("Century",14)).place(x=290,y=180)

        dia=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
        dialbl=Label(root,text="Día").place(x=30,y=225)
        diastr=StringVar(root)
        diastr.set(dia[0])
        diaopt=ttk.Combobox(root,textvariable=diastr,values=dia,width=5)
        diaopt.place(x=20,y=250)

        mesLbl=Label(root,text="Mes").place(x=88,y=225)
        mes=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Set","Oct","Nov","Dic"]
        messtr=StringVar(root)
        messtr.set(mes[0])
        mesopt=ttk.Combobox(root,textvariable=messtr,values=mes,width=6)
        mesopt.place(x=78,y=250)
        
        listaAños=listaAño()
        añolbl=Label(root,text="Año").place(x=160,y=225)
        añosstr=StringVar(root)
        añosstr.set(listaAños[28])     
        año=ttk.Combobox(root,textvariable=añosstr,values=listaAños,width=6)
        año.place(x=142,y=250)

        listaCiudades=crearLista("archivos\Ciudades.txt")
        origenlbl=Label(root,text="Origen").place(x=218,y=225)
        origenstr=StringVar(root)
        origen=ttk.Combobox(root,textvariable=origenstr,values=listaCiudades,width=5)
        origen.place(x=212,y=250)

        destinolbl=Label(root,text="Destino").place(x=270,y=225)
        destinostr=StringVar(root)
        destino=ttk.Combobox(root,textvariable=destinostr,values=listaCiudades,width=5)
        destino.place(x=270,y=250)

        hora=["0100","0200","0300","0400","0500","0600","0700","0800","0900","1000","1200","1300","1400","1500","1600","1700","1800","1900","2000","2100","2200","2300","2400"]
        horaPartidalbl=Label(root,text="H. Partida").place(x=332,y=225)
        horaPartida=StringVar(root)
        horaPartida.set(hora[0])
        horaPartidaopt=ttk.Combobox(root,textvariable=horaPartida,values=hora,width=7)
        horaPartidaopt.place(x=330,y=250)

        HoraLlegadalbl=Label(root,text="H. Llegada").place(x=400,y=225)
        horaLlegada=StringVar(root)
        horaLlegada.set(hora[8])
        horaLlegadaopt=ttk.Combobox(root,textvariable=horaLlegada,values=hora,width=7)
        horaLlegadaopt.place(x=400,y=250)

        archivo="archivos\Aerolineas.txt"
        aerolinealbl=ttk.Label(root,text="Aerolinea").place(x=488,y=225)
        aerolineas=crearLista(archivo)
        mostrar=mostrarAerolineas(aerolineas)
        aerolinea=StringVar(root)
        aerolineastr=str(aerolinea.get().split(","))
        aerolineaopt=ttk.Combobox(root,textvariable=aerolinea,values=mostrar,width=13)
        aerolineaopt.place(x=470,y=250)

        preciolbl=Label(root,text="Precio ($) ").place(x=580,y=225)
        preciostr=IntVar(root,value=0)
        precio=ttk.Entry(root,textvariable=preciostr,width=10).place(x=576,y=250)

        archivoVuelos="archivos\Vuelos.txt"
        vuelosG=ttk.Button(root,text="Guardar",command=lambda:vuelos(numeroVuelo(numeroRandom()),diastr.get(),messtr.get(),añosstr.get(),origenstr.get(),destinostr.get(),horaPartida.get(),horaLlegada.get(),aerolineas[aerolineaopt.current()][0],preciostr.get())).place(x=100,y=280)
        vuelosE=ttk.Button(root,text="Eliminar",command=lambda:menuEliminar(archivoVuelos,Toplevel(root))).place(x=20,y=280)

        vUsuario=ttk.Button(root,text="Vuelos realizados por usuario",width=35).place(x=420,y=20)
        vNacionalidad=ttk.Button(root,text="Vuelos realizados por nacionalidad",width=35).place(x=420,y=50)
        ciudadesVisitadas=ttk.Button(root,text="5 ciudades más visitadas",width=35).place(x=420,y=80)


#-------------------------------------------------Menu eliminar
#E:un string(archivo) y una ventana (Tk())
#S:Genera un combobox con los elementos que se desea eliminar.
#R:archivo debe ser un string y una ruta de un archivo txt, root debe ser una ventana (Tk())
def menuEliminar(archivo,root):
        if archivo=="archivos\Aerolineas.txt":
                lista=mostrarAerolineas(crearLista(archivo))
        else:
                lista=crearLista(archivo)
        eliminarstr=StringVar(root)
        if archivo!="archivos\Vuelos.txt":
                eliminarlist=ttk.Combobox(root,textvariable=eliminarstr,values=lista)
                botonE=ttk.Button(root,text="Eliminar",command=lambda:eliminarAerolineas(obtenerID(eliminarstr.get()),lista,archivo,root))
        else:
                eliminarlist=ttk.Combobox(root,textvariable=eliminarstr,values=lista,width=45)
                botonE=ttk.Button(root,text="Eliminar",command=lambda:eliminarVuelos(eliminarstr.get().split(" ")[6],lista,archivo,root))
        eliminarlist.pack()
        botonE.pack()
        pos=eliminarlist.current()
        root.mainloop()

#-------------------------------------------------Eliminar vuelos
#E:un Id, una lista, una ruta de un archivo, y una ventana
#S:Elimina un vuelo y verifica si se encuentra en reservaciones
#R:ID debe ser un número convertido en un string. lista debe ser una lista. archivo una ruta de un archivo.txt  y root una ventana
def eliminarVuelos(ID,lista,archivo,root):
        res=[]
        modificarReservaciones=[]
     
        archivo1="archivos\Reservaciones.txt"
        listaReservaciones=crearLista(archivo1)


        while lista!=[]:
                if ID!=lista[0][6]:
                        res+=[lista[0]]
                if existeEnReservaciones(ID):
                        while listaReservaciones!=[]:                
                                if ID!=listaReservaciones[0][6]:
                                        modificarReservaciones+=[listaReservaciones[0]]
                                listaReservaciones=listaReservaciones[1:]                        
                lista=lista[1:]        
        txt=open(archivo1,"w")        
        while modificarReservaciones!=[]:
                txt.write(modificarReservaciones[0][0]+","+modificarReservaciones[0][1]+","+modificarReservaciones[0][2]+","+modificarReservaciones[0][3]+","+modificarReservaciones[0][4]+","+modificarReservaciones[0][5]+","+modificarReservaciones[0][6]+","+modificarReservaciones[0][7]+","+modificarReservaciones[0][8]+","+modificarReservaciones[0][9]+","+modificarReservaciones[0][10]+","+modificarReservaciones[0][11]+","+modificarReservaciones[0][12]+"\n")
                modificarReservaciones=modificarReservaciones[1:]                        
        txt.close()
        root.destroy()
        return escribir(archivo,res,Tk())        
                
#-------------------------------------------------Eliminar Aerolineas
#E:Un D, una lista, una ruta de un archivo y una ventana
#S:Elimina una aerolinea y verifica si se encuentra en otro archivo.txt para eliminarlo
#R:lista debe ser una lista, el id un número convertido en un string y root una ventana     
def eliminarAerolineas(ID,lista,archivo,root):
        res=[]
        modificarVuelos=[]
        modificarReservaciones=[]
        
        archivo1="archivos\Vuelos.txt"
        listaVuelos=crearLista(archivo1)

        archivo2="archivos\Reservaciones.txt"
        listaReservaciones=crearLista(archivo2)
        
        while lista!=[]:
                if obtenerID(lista[0])!=ID:
                        res+=[lista[0]]
                if existeEnVuelos(obtenerID(lista[0])):
                        while listaVuelos!=[]:
                                if ID!=listaVuelos[0][6]:
                                        modificarVuelos+=[listaVuelos[0]]
                                listaVuelos=listaVuelos[1:]
                if existeEnReservaciones(obtenerID(lista[0])):
                        while listaReservaciones!=[]:
                                if ID!=listaReservaciones[0][6]:
                                        modificarReservaciones+=[listaReservaciones[0]]                                        
                                listaReservaciones=listaReservaciones[1:]
                lista=lista[1:]
        archivo="archivos\Vuelos.txt"
        txt=open(archivo,"w")        
        while modificarVuelos!=[]:
                txt.write(modificarVuelos[0][0]+","+modificarVuelos[0][1]+","+modificarVuelos[0][2]+","+modificarVuelos[0][3]+","+modificarVuelos[0][4]+","+modificarVuelos[0][5]+","+modificarVuelos[0][6]+","+modificarVuelos[0][7]+"\n")
                modificarVuelos=modificarVuelos[1:]
        txt.close()
        
        archivo="archivos\Reservaciones.txt"
        txt=open(archivo,"w")        
        while modificarReservaciones!=[]:
                txt.write(modificarReservaciones[0][0]+","+modificarReservaciones[0][1]+","+modificarReservaciones[0][2]+","+modificarReservaciones[0][3]+","+modificarReservaciones[0][4]+","+modificarReservaciones[0][5]+","+modificarReservaciones[0][6]+","+modificarReservaciones[0][7]+","+modificarReservaciones[0][8]+","+modificarReservaciones[0][9]+","+modificarReservaciones[0][10]+","+modificarReservaciones[0][11]+","+modificarReservaciones[0][12]+"\n")
                modificarReservaciones=modificarReservaciones[1:]                        
        txt.close()

        archivo="archivos\Aerolineas.txt"
        root.destroy()
        return escribir(archivo,listaID(res),Tk())

#-------------------------------------------------Verificar si existe en vuelos
#E:un ID
#S:Retorna un valor booleano si el id se encuentra en en un txt
#R:El id debe ser un número convertido en un string
def existeEnVuelos(ID):
        archivo="archivos\Vuelos.txt"
        listaVuelos=crearLista(archivo)
        while listaVuelos!=[]:
                if ID==listaVuelos[0][6]:
                        return True
                listaVuelos=listaVuelos[1:]
        return False        

#-------------------------------------------------Verificar si existe en reservaciones
#E:el id de una aerolinea
#S:retorna un valor booleano si la id de la aerolinea se encuentra o no en reservaciones
#R:la Aerolinea debe ser un número convertido en un string
def existeEnReservaciones(Aerolinea):
        archivo="archivos\Reservaciones.txt"
        listaReservaciones=crearLista(archivo)
        while listaReservaciones!=[]:
                if Aerolinea==listaReservaciones[0][6]:
                        return True
                listaReservaciones=listaReservaciones[1:]
        return False
                
def listaID(lista):
        res=[]
        while lista!=[]:
                res+=[obtenerID(lista[0])+","+lista[0]]
                lista=lista[1:]
        return res
#-------------------------------------------------Usuarios
#E:una ventana
#S:Muestra una interfáz de usuario, donde muestra un buscador en el cual se va a poder filtrar los vuelos
#R:root debe ser una ventana
def usuario(root):

        #------------------------Interfaz
        root.title("Buscador de vuelos")
        root.geometry("620x60")
        root.resizable(width=False, height=False)
        root.iconbitmap("interfaz\logo.ico")

        x=4
        y=25
        encabezado=Label(root,text="Día").place(x=8,y=0)
        dialist=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
        diastr=StringVar()
        dia=ttk.Combobox(root,textvariable=diastr,values=dialist,width=2)
        dia.place(x=x,y=y)
        x+=38

        meslbl=Label(root,text="Mes").place(x=52,y=0)
        meslist=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Set","Oct","Nov","Dic"]
        messtr=StringVar()
        mes=ttk.Combobox(root,textvariable=messtr,values=meslist,width=4).place(x=x,y=y)
        x+=50

        listaAños=listaAño()
        añolbl=Label(root,text="Año").place(x=x+15,y=0)
        añosstr=StringVar(root)  
        año=ttk.Combobox(root,textvariable=añosstr,values=listaAños,width=6)
        año.place(x=x,y=y)
        x+=62

        aerolineaslbl=Label(root,text="Aerolineas").place(x=x+44,y=0)
        listaAerolineas=crearLista("archivos\Aerolineas.txt")
        mostrar=mostrarAerolineas(listaAerolineas)
        aerolineasstr=StringVar()
        aerolineas=ttk.Combobox(root,textvariable=aerolineasstr,values=mostrar)
        aerolineas.place(x=x,y=y)
        x+=146

        listaCiudades=crearLista("archivos\Ciudades.txt")
        origenlbl=Label(root,text="Origen").place(x=x+4,y=0)
        origenstr=StringVar()
        origen=ttk.Combobox(root,textvariable=origenstr,values=listaCiudades,width=5)
        origen.place(x=x,y=y)
        x+=56

        destinolbl=Label(root,text="Destino").place(x=x,y=0)
        destinostr=StringVar()
        destino=ttk.Combobox(root,textvariable=destinostr,values=listaCiudades,width=5)
        destino.place(x=x,y=y)
        x+=58

        rangoPrecioslbl=Label(root,text="Rango de precios").place(x=x-4,y=0)
        rangoPreciosint=IntVar()
        rangoPreciosint.set(0)
        rangoPrecios=Entry(root,textvariable=rangoPreciosint,width=14).place(x=x,y=y)
        x+=106

        buscar=ttk.Button(root,text="Buscar",command=lambda:filtro(root,diastr.get(),messtr.get(),añosstr.get(),obtenerID(aerolineasstr.get()),origenstr.get(),destinostr.get(),rangoPreciosint.get())).place(x=x ,y=y-4)

#-------------------------------------------------Filtros
#E:una ventana (root),dia,mes,año,aerolinea,origen,destino,rango de precios
#S:retorna a un filtro dependiendo de los datos ingresados y lo muestra
#R:root debe ser una ventana. dia, mes, año, aerolinea, origen,destino y rango de precios debe ser string
def filtro(root,dia,mes,año,aerolinea,origen,destino,rangoPrecios):
        if isinstance(rangoPrecios,int):
                if dia!="" and mes!="" and año!="" and aerolinea!="" and origen!="" and destino!="":
                        filtro1=listaFiltrada(dia,mes,año,aerolinea,origen,destino,1)
                        return mostrarResultado(Toplevel(root),filtro1)
                elif dia!="" and mes!="" and año!=""  and aerolinea=="" and origen!="" and destino!="":
                        filtro2=listaFiltrada(dia,mes,año,aerolinea,origen,destino,2)
                        return mostrarResultado(Toplevel(root),filtro2)
                elif dia=="" and mes=="" and año==""and aerolinea=="" and origen!="" and destino!="":
                        filtro3=listaFiltrada(dia,mes,año,aerolinea,origen,destino,3)
                        return mostrarResultado(Toplevel(root),filtro3)
                elif dia=="" and mes=="" and año==""   and aerolinea!="" and origen!="" and destino!="":
                        filtro4=listaFiltrada(dia,mes,año,aerolinea,origen,destino,4)
                        return mostrarResultado(Toplevel(root),filtro4)
                else:
                        messagebox.showinfo("Error", "Ingrese una búsqueda válida")
        else:
                messagebox.showinfo("Error", "El rango de precios debe ser un número")

#-------------------------------------------------Aplicar búsqueda
#E:dia, mes, año, aerolinea, origen, destino y el tipo de filtro
#S:retorna una lista filtrada segun el tipo de filtro
#R: dia, mes, año, aerolinea, origen,destino y rango de precios debe ser string . tipo de filtro debe ser un número entero            
def listaFiltrada(dia,mes,año,aerolinea,origen,destino,tipoFiltro):
        listaVuelos=crearLista("archivos\Vuelos.txt")
        res=[]
        if tipoFiltro == 1:
                while listaVuelos!=[]:
                        if listaFecha(listaVuelos[0][1])[0]==dia and listaFecha(listaVuelos[0][1])[1]==mes and listaFecha(listaVuelos[0][1])[2]==año and listaVuelos[0][6]==aerolinea and listaVuelos[0][2]==origen and listaVuelos[0][3]==destino:
                                res+=[listaVuelos[0]]
                        listaVuelos=listaVuelos[1:]
                return res
        elif tipoFiltro == 2:
                while listaVuelos!=[]:
                        
                        if listaFecha(listaVuelos[0][1])[0]==dia and listaFecha(listaVuelos[0][1])[1]==mes and listaFecha(listaVuelos[0][1])[2]==año and listaVuelos[0][2]==origen and listaVuelos[0][3]==destino:
                                res+=[listaVuelos[0]]
                        listaVuelos=listaVuelos[1:]
                return res
        elif tipoFiltro == 3:
                while listaVuelos!=[]:
                        if listaVuelos[0][2]==origen and listaVuelos[0][3]==destino:
                                res+=[listaVuelos[0]]
                        listaVuelos=listaVuelos[1:]
                return res
        elif tipoFiltro==4:
                while listaVuelos!=[]:
                        if listaVuelos[0][6]==aerolinea and listaVuelos[0][2]==origen and listaVuelos[0][3]==destino:
                                res+=[listaVuelos[0]]
                        listaVuelos=listaVuelos[1:]
                return res

#-------------------------------------------------Partir fecha
#E:una fecha
#S:retorna una lista con la fecha separada por /
#R:posFecha debe ser una fecha     
def listaFecha(posFecha):
        return posFecha.split("/")

#-------------------------------------------------Mostrar vuelos
#E:una ventana y una lista 
#S:muestra un listbox con todos los vuelos ya filtrados
#R:root debe ser una ventana y listaVuelos una lista   
def mostrarResultado(root,listaVuelos):
        scrollbar = Scrollbar(root)
        scrollbar.pack( side = RIGHT, fill = Y )
        root.geometry("720x480")
        root.resizable(width=False, height=False)
        mylist = Listbox(root, font=('Arial',20),yscrollcommand = scrollbar.set)
        mylist.insert(END,*listaVuelos)
        boton=ttk.Button(root,text="Recervar",command=lambda:reservarVuelos(Toplevel(root),listaVuelos[int(str(mylist.curselection())[1:-2])]))

        mylist.pack( fill = BOTH )
        boton.pack()
        scrollbar.config( command = mylist.yview )
        
#-------------------------------------------------Reservar vuelos
#E:una ventana y una lista
#S:Muestra un formulario para reservar el vuelo
#R:vuelos debe ser una lista 
def reservarVuelos(root,vuelos):
        root.resizable(width=False, height=False)
        archivo="archivos\Reservaciones.txt"
        pasaportelbl=Label(root,text="Pasaporte",font=("Arial",12)).pack()
        pasaportestr=StringVar()
        pasaporteopt=ttk.Entry(root,textvariable=pasaportestr)
        pasaporteopt.pack()

        nombrelbl=Label(root,text="Nombre",font=("Arial",12)).pack()
        nombrestr=StringVar()
        nombreopt=ttk.Entry(root,textvariable=nombrestr).pack()

        primerApellidolbl=Label(root,text="Primer Apellido",font=("Arial",12)).pack()
        primerApellidostr=StringVar()
        primerApellidoopt=ttk.Entry(root,textvariable=primerApellidostr)
        primerApellidoopt.pack()

        segundoApellidolbl=Label(root,text="Segundo Apellido",font=("Arial",12)).pack()
        segundoApellidostr=StringVar()
        segundoApellidoopt=ttk.Entry(root,textvariable=segundoApellidostr)
        segundoApellidoopt.pack()

        nacionalidadlbl=Label(root,text="Nacionalidad",font=("Arial",12)).pack()
        nacionalidadstr=StringVar()
        nacionalidadopt=ttk.Entry(root,textvariable=nacionalidadstr)
        nacionalidadopt.pack()

        sexolbl=Label(root,text="Sexo",font=("Arial",12)).pack()
        sexostr=StringVar
        sexolista=["Masculino","Femenino"]
        sexoopt=ttk.Combobox(root,textvariable=sexostr,values=sexolista)
        sexoopt.pack()

        reservar=ttk.Button(root,text="Reservar",command=lambda:añadirReservacion(vuelos,pasaportestr.get(),nombrestr.get(),primerApellidostr.get(),segundoApellidostr.get(),nacionalidadstr.get())).pack()

#-------------------------------------------------añadir una reservacion
#E:una lista. pasaporte, nombre, primer apelli, segundo apellido y nacionalidad (todos string)
#S:añade una reservación
#R:lista debe ser una lista. pasaporte, nombre, primer apellido, segundo apellido y nacionalidad deben ser strings
def añadirReservacion(lista,pasaporte,nombre,primerApellido,segundoApellido,nacionalidad):
        archivo="archivos\Reservaciones.txt"        
        res=[]
        while lista!=[]:
                res+=[lista[0]]
                lista=lista[1:]
        res+=[pasaporte,nombre,primerApellido,segundoApellido,nacionalidad]
        return añadir(archivo,res)

        





#administrador(Tk())
login(Tk())
##usuario(Tk())
