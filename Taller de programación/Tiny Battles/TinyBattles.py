from tkinter import *
from PIL import Image, ImageTk
import random
import time
class ventana_principal:
    def __init__(self,master):
        self.master = master
        self.bg = Label(self.master)
        self.bg.place(x = -2, y = -2)
        self.master.attributes("-fullscreen",True)
        self.turno = True
        self.escenario = 1
        self.matriz_batalla = []
        self.matriz_botones = []
        self.personajes_muertos_j1 = []
        self.personajes_muertos_j2 = []
        self.widgets_tumbnails = []
        self.widgets_stats_j1 = []
        self.widgets_stats_j2 = []
        self.widgets_batalla = []        
        #self.personajes_j1 = [['soporte', [4, 5, 4, 4,0]], ['defenza', [3, 1, 1, 4,0]], ['daño', [6, 2, 2, 4,0]], ['defenza', [5, 2, 3, 4,0]], ['soporte', [1, 2, 2, 1,0]], ['defenza', [1, 1, 4, 4,0]], ['defenza', [5, 1, 4, 2,0]], ['defenza', [2, 1, 7, 3,0]], ['defenza', [2, 2, 1, 2,0]], ['defenza', [1, 1, 5, 4,0]]]
        #self.personajes_j2 = [['soporte', [4, 5, 4, 4,0]], ['defenza', [3, 1, 1, 4,0]], ['daño', [6, 2, 2, 4,0]], ['defenza', [5, 2, 3, 4,0]], ['soporte', [1, 2, 2, 1,0]], ['defenza', [1, 1, 4, 4,0]], ['defenza', [5, 1, 4, 2,0]], ['defenza', [2, 1, 7, 3,0]], ['defenza', [2, 2, 1, 2,0]], ['defenza', [1, 1, 5, 4,0]]]
        self.personajes_j1 = []
        self.personajes_j2 = []


    def menu(self):
        self.bg.lift()
        imagen = ImageTk.PhotoImage(Image.open("Recursos\Interfaz\Fondo_patalla_pricipal.png").resize((1366,768 ), Image.ANTIALIAS))
        self.bg["image"] = imagen
        self.bg.image= imagen
        self.salir = Button(self.master, text = "Salir",font = ("Arial",24),width = 20, command = lambda: self.master.destroy()).place(x = 495, y = 600)
        self.jugar = Button(self.master, text = "Jugar",font = ("Arial",24),width = 20, command = lambda: self.elegir_escenario()) 
        self.jugar.place(x = 495, y = 500)

    def elegir_escenario(self):
        self.bg.lift()
        atras = Button(self.master, text = "Atras",command = lambda: self.menu()).place(x = 0, y = 0)
        self.personajes_j1 = []
        self.personajes_j2 = []

        imagen = ImageTk.PhotoImage(Image.open("Recursos\Escenarios\Escenario_1.png").resize((440,380), Image.ANTIALIAS))   
        self.escenario_1 = Button(self.master,command = lambda: self.crear_personaje(1))
        self.escenario_1["image"] = imagen
        self.escenario_1.image = imagen     
        self.escenario_1.place(x = 10 , y = 170)

        imagen = ImageTk.PhotoImage(Image.open("Recursos\Escenarios\Escenario_2.png").resize((440,380), Image.ANTIALIAS))  
        self.escenario_2 = Button(self.master, command = lambda: self.crear_personaje(2))
        self.escenario_2["image"] = imagen
        self.escenario_2.image = imagen 
        self.escenario_2.place(x = 460, y = 170)

        imagen = ImageTk.PhotoImage(Image.open("Recursos\Escenarios\Escenario_3.png").resize((440,380), Image.ANTIALIAS))  
        self.escenario_3 = Button(self.master,command = lambda: self.crear_personaje(3))
        self.escenario_3["image"] = imagen
        self.escenario_3.image = imagen         
        self.escenario_3.place(x = 910, y = 170)

    def crear_personaje(self,numero_escenario):
        self.bg.lift()
        self.escenario = numero_escenario
        self.atras = Button(self.master, text = "atras",command = lambda: self.elegir_escenario()).place(x = 0, y = 0)
        self.separador = Label(self.master, bg ="gray",height = 100).place(x = 683, y = 0)
        if self.personajes_j1 != [] or self.personajes_j2 != [] :
            self.personajes_j1 = []
            self.personajes_j2 = []
            
        if self.escenario  == 1:
            self.daño_img_j1 = ImageTk.PhotoImage(Image.open("Recursos\Personajes\daño_j1_1.png").resize((65,70)))
            self.defenza_img_j1 = ImageTk.PhotoImage(Image.open("Recursos\Personajes\defenza_j1_1.png").resize((65,70)))
            self.soporte_img_j1 = ImageTk.PhotoImage(Image.open("Recursos\Personajes\soporte_j1_1.png").resize((65,70)))

            self.daño_img_j2 = ImageTk.PhotoImage(Image.open("Recursos\Personajes\daño_j2_1.png").resize((65,70)))
            self.defenza_img_j2 = ImageTk.PhotoImage(Image.open("Recursos\Personajes\defenza_j2_1.png").resize((65,70)))
            self.soporte_img_j2 = ImageTk.PhotoImage(Image.open("Recursos\Personajes\soporte_j2_1.png").resize((65,70)))
            
        elif self.escenario == 2:
            #Cambiar nombre del archivo
            self.daño_img_j1 = ImageTk.PhotoImage(Image.open("Recursos\Personajes\daño_j1_2.png").resize((65,70)))
            self.defenza_img_j1 = ImageTk.PhotoImage(Image.open("Recursos\Personajes\defenza_j1_2.png").resize((65,70)))
            self.soporte_img_j1 = ImageTk.PhotoImage(Image.open("Recursos\Personajes\soporte_j1_2.png").resize((65,70)))
            
            self.daño_img_j2 = ImageTk.PhotoImage(Image.open("Recursos\Personajes\daño_j2_2.png").resize((65,70)))
            self.defenza_img_j2 = ImageTk.PhotoImage(Image.open("Recursos\Personajes\defenza_j2_2.png").resize((65,70)))
            self.soporte_img_j2 = ImageTk.PhotoImage(Image.open("Recursos\Personajes\soporte_j2_2.png").resize((65,70)))
            
        else:
            #Cambiar nombre del archivo
            self.daño_img_j1 = ImageTk.PhotoImage(Image.open("Recursos\Personajes\daño_j1_3.png").resize((65,70)))
            self.defenza_img_j1 = ImageTk.PhotoImage(Image.open("Recursos\Personajes\defenza_j1_3.png").resize((65,70)))
            self.soporte_img_j1 = ImageTk.PhotoImage(Image.open("Recursos\Personajes\soporte_j1_3.png").resize((65,70)))

            self.daño_img_j2 = ImageTk.PhotoImage(Image.open("Recursos\Personajes\daño_j2_3.png").resize((65,70)))
            self.defenza_img_j2 = ImageTk.PhotoImage(Image.open("Recursos\Personajes\defenza_j2_3.png").resize((65,70)))
            self.soporte_img_j2 = ImageTk.PhotoImage(Image.open("Recursos\Personajes\soporte_j2_3.png").resize((65,70)))

        self.daño_stats = [6,3,5,4,0]
        self.defenza_stats = [5,2,7,4,0]
        self.soporte_stats = [4,6,4,4,0]
        
        # Crear personaje jugador 1
        jugador_1 = Label(self.master, text = "Jugador 1").place(x = 100, y = 50)
        self.skill_points_j1 = 1000
        self.label_skill_j1 = Label(self.master, text ="Skill points: " + str(self.skill_points_j1))
        self.label_skill_j1.place(x = 200, y = 50)

        #Personajes J1
        self.daño = Button(self.master, image = self.daño_img_j1, command = lambda: self.añadir_personaje("daño","j1",self.daño_stats))
        self.daño.place(x = 100, y = 150)
        self.defenza = Button(self.master, image = self.defenza_img_j1, command = lambda: self.añadir_personaje("defenza","j1",self.defenza_stats))
        self.defenza.place(x = 200, y = 150 )
        self.soporte = Button(self.master,image = self.soporte_img_j1, command = lambda: self.añadir_personaje("soporte","j1",self.soporte_stats))
        self.soporte.place(x = 300, y = 150)
        
        # Crear personaje jugador 2
        jugador_2 = Label(self.master, text = "Jugador 2").place(x = 1200, y = 50)
        self.skill_points_j2 = 1000
        self.label_skill_j2 = Label(self.master, text ="Skill points: " + str(self.skill_points_j2))
        self.label_skill_j2.place(x = 1070, y = 50)

        #Personajes J2
        self.daño = Button(self.master, image = self.daño_img_j2, command = lambda: self.añadir_personaje("daño","j2",self.daño_stats))
        self.daño.place(x = 1200, y = 150)
        self.defenza = Button(self.master, image = self.defenza_img_j2, command = lambda: self.añadir_personaje("defenza","j2",self.defenza_stats))
        self.defenza.place(x = 1100, y = 150 )
        self.soporte = Button(self.master,image = self.soporte_img_j2, command = lambda: self.añadir_personaje("soporte","j2",self.soporte_stats))
        self.soporte.place(x = 1000, y = 150)


        #Tumbnails        
        self.x_j1 = 20
        self.y_j1 = 400

        self.x_j2 = 740
        self.y_j2 = 400

        self.lista_tumbnails_j1 = []
        self.lista_tumbnails_j2 = []


        self.iniciar = Button(self.master, text = "Iniciar Juego", state = DISABLED, command = lambda: self.iniciar_juego())
        self.iniciar.place(x = 1200, y = 700)


        


    def añadir_personaje(self,tipo,jugador,max_stats):            
        if jugador == "j1":
            if self.skill_points_j1 != 0:
                self.personajes_j1 += [[tipo,self.crear_stats(max_stats)]]
                self.skill_points_j1 -= 100
                self.label_skill_j1["text"] = "Skill points: "+ str(self.skill_points_j1)
                self.crear_tumbnails(tipo,jugador)
            else:
                print("El jugador 1 no puede crear más personajes")
                
        else:
            if self.skill_points_j2 != 0:
                self.personajes_j2 += [[tipo,self.crear_stats(max_stats)]]
                self.skill_points_j2 -= 100
                self.label_skill_j2["text"] = "Skill points: "+ str(self.skill_points_j2)
                self.crear_tumbnails(tipo,jugador)
            else:
                print("El jugador 2 no puede crear más personajes")

    def crear_tumbnails(self,tipo,jugador):
        pos_matriz = len(eval("self.personajes_"+str(jugador)))
        tumbnail =  eval("self."+str(tipo)+"_img_"+jugador)
        
        if self.skill_points_j1 == 0  and self.skill_points_j2 == 0:
            self.iniciar["state"] = "normal"
        
        if jugador == "j1":
            if self.espacio_vacio(jugador):
                len_lista = len(self.lista_tumbnails_j1)
                self.x = 20
                self.y = 400
                for i in range(0,len_lista):
                    if self.lista_tumbnails_j1[i] == []:
                        self.tumbnail = Button(self.master,image = tumbnail,command = lambda: self.eliminar_tumbnail(i,jugador)) 
                        self.tumbnail.place(x = self.x, y = self.y)
                        self.lista_tumbnails_j1[i] = self.tumbnail                      
                    if self.x < 580:
                        self.x +=  70
                    else:
                        self.x = 20
                        self.y += 80
                        
            else:
                pos_lista = len(self.personajes_j1)-1
                self.tumbnail = Button(self.master,image = tumbnail,command = lambda: self.eliminar_tumbnail(pos_lista,jugador)) 
                self.tumbnail.place(x = self.x_j1, y = self.y_j1)
                self.lista_tumbnails_j1 += [self.tumbnail]
                if self.x_j1 < 580:
                    self.x_j1 +=  70
                else:
                    self.x_j1 = 20
                    self.y_j1 += 80
        else:
            if self.espacio_vacio(jugador):
                len_lista = len(self.lista_tumbnails_j2)
                self.x = 740
                self.y = 400
                for i in range(0,len_lista):
                    if self.lista_tumbnails_j2[i] == []:
                        self.tumbnail = Button(self.master,image = tumbnail,command = lambda: self.eliminar_tumbnail(i,jugador)) 
                        self.tumbnail.place(x = self.x, y = self.y)
                        self.lista_tumbnails_j2[i] = self.tumbnail                      
                    if self.x < 1260:
                        self.x +=  70
                    else:
                        self.x = 740
                        self.y += 80
            else:
                pos_lista = len(self.personajes_j2)-1
                self.tumbnail = Button(self.master,image = tumbnail,command = lambda: self.eliminar_tumbnail(pos_lista,jugador)) 
                self.tumbnail.place(x = self.x_j2, y = self.y_j2)
                self.lista_tumbnails_j2 += [self.tumbnail]
                
                if self.x_j2 < 1260:
                    self.x_j2 +=  70
                else:
                    self.x_j2 = 740
                    self.y_j2 += 80

    def espacio_vacio(self,jugador):
        if jugador == "j1":
            for i in self.lista_tumbnails_j1:
                if i == []:
                    return True
            return False
        else:
            for i in self.lista_tumbnails_j2:
                if i == []:
                    return True
            return False            
            
    def eliminar_tumbnail(self,pos,jugador):
        if jugador == "j1":
            self.lista_tumbnails_j1[pos].destroy()
            self.lista_tumbnails_j1[pos] = []
            self.personajes_j1.pop(pos)
            self.skill_points_j1 += 100
            self.label_skill_j1["text"] = "skill points: "+str(self.skill_points_j1)
            if self.skill_points_j1 != 0 or self.skill_points_j2 != 0:
                self.iniciar["state"] = "disabled"
            

        else:
            self.lista_tumbnails_j2[pos].destroy()
            self.lista_tumbnails_j2[pos] = []
            self.personajes_j2.pop(pos)
            self.skill_points_j2 += 100
            self.label_skill_j2["text"] = "skill points: "+str(self.skill_points_j2)
            if self.skill_points_j1 != 0 or self.skill_points_j2 != 0:
                self.iniciar["state"] = "disabled"
            
            
    def crear_stats(self,max_stats):
        stats = []
        for i in max_stats:
            if i != 0:
                stats += [random.randint(1,i)]
            else:
                stats += [i]
        return stats
    
    def iniciar_juego(self):
        self.bg.lift()
        imagen = ImageTk.PhotoImage(Image.open("Recursos\Escenarios\Escenario_"+str(self.escenario)+".png").resize((1366,768 ), Image.ANTIALIAS))
        self.bg["image"] = imagen
        self.bg.image = imagen
        self.matriz_vacia()
        self.botones_tablero ()
        self.tumbnails_jugadores()
        
    def tumbnails_jugadores(self):
        x_j1 = 0
        y_j1 = 80
        for i in range(10):
            imagen = PhotoImage(file = "Recursos\Interfaz\\"+str(self.personajes_j1[i][0])+".png")
            self.tumbnail_pj = Button(image = imagen,command = lambda i=i:self.mostrar_stats(i,"j1"))
            self.tumbnail_pj.image = imagen
            self.tumbnail_pj.place(x = x_j1, y = y_j1) 
            if x_j1 < 220:
                   x_j1 +=  55
            else:
                x_j1 = 0
                y_j1 += 55

        x_j2 = 1090
        y_j2 = 80
        for i in range(10):
            imagen = PhotoImage(file = "Recursos\Interfaz\\"+str(self.personajes_j2[i][0])+".png")
            self.tumbnail_pj = Button(image = imagen,command = lambda i=i:self.mostrar_stats(i,"j2"))
            self.tumbnail_pj.image = imagen
            self.tumbnail_pj.place(x = x_j2, y = y_j2)
            if x_j2 < 1300:
                   x_j2 +=  55
            else:
                x_j2 = 1090
                y_j2 += 55          
            
    def mostrar_stats(self,pos,jugador):
        if jugador == "j1":
            stats =["Fuerza","Inteligencia","Defenza","Ataque","Combates ganados"]
            texto_stats = "\n\n\n\n\n\n\n\n\n\n\n\n\n"
            for i in range(len(self.personajes_j1[pos][1])):
                texto_stats += str(stats[i])+" : "+str(self.personajes_j1[pos][1][i])+"\n\n"
                
                
            self.menu_stats_j1 = Label(self.master,text = texto_stats, height = 31, width = 39)
            self.menu_stats_j1.place(x = 0, y = 220)
            ruta = "Recursos\Personajes\\"+str(self.personajes_j1[pos][0])+"_j1_1.png"
            imagen = ImageTk.PhotoImage(Image.open(ruta).resize((170, 200), Image.ANTIALIAS))
            self.miniatura = Label(self.master,image = imagen)
            self.miniatura.place(x = 50, y = 220)
            cerrar = Button(self.master,text = "X",command = lambda:self.cerrar_widgets("self.widgets_stats_j1"))
            cerrar.place (x = 262, y = 220)
            self.miniatura.image = imagen
            self.widgets_stats_j1 +=[self.menu_stats_j1,self.miniatura,cerrar]
        else:
            stats =["Fuerza","Inteligencia","Defenza","Ataque","Combates ganados"]
            texto_stats = "\n\n\n\n\n\n\n\n\n\n\n\n\n"
            for i in range(len(self.personajes_j1[pos][1])):
                texto_stats += str(stats[i])+" : "+str(self.personajes_j2[pos][1][i])+"\n\n"
                            
            self.menu_stats_j2 = Label(self.master, text = texto_stats,height = 31, width = 39)
            self.menu_stats_j2.place(x = 1086, y = 220)
            ruta = "Recursos\Personajes\\"+str(self.personajes_j1[pos][0])+"_j2_1.png"
            imagen = ImageTk.PhotoImage(Image.open(ruta).resize((170, 200), Image.ANTIALIAS))
            self.miniatura = Label(self.master,image = imagen)
            self.miniatura.place(x = 1150, y = 220)
            cerrar = Button(self.master,text = "X",command = lambda:self.cerrar_widgets("self.widgets_stats_j2"))
            cerrar.place (x = 1086, y = 220)
            self.miniatura.image = imagen
            self.widgets_stats_j2 += [self.menu_stats_j2,self.miniatura,cerrar]
            
    def cerrar_widgets(self,nombre):
        variable = eval(nombre)
        for i in variable:
            i.destroy()
        
    def botones_tablero (self):
        self.label_turno = Label(self.master,text = "Presiona jugar para iniciar ",font = ("Arial",25))
        self.label_turno.place(x= 550, y = 20)
        self.label_j1 = Label(self.master,text = "Jugador 1",font = ("Arial",25)).place(x= 63, y = 20)
        self.label_j2 = Label(self.master,text = "Jugador 2",font = ("Arial",25)).place(x= 1153, y = 20)
        self.jugar = Button(self.master, text = "Jugar", font = ("Arial", 14), command = lambda:self.posicion_aleatorea()).place(x = 540, y = 700)
        self.terminar = Button(self.master, text = "Terminar Juego",font = ("Arial",14), command = lambda: self.finalizar_juego()).place(x = 670, y = 700)
        self.vector_botones = []
        x = 440
        y = 180
        for i in range(6):
            for j in range(7):
                boton = Button(self.master,bg ="white", height = 5,width = 9)
                boton.place(x = x, y = y)
                if x < 870:
                   x +=  72
                else:
                    x = 440
                    y += 85
                self.vector_botones += [boton]
            self.matriz_botones += [self.vector_botones]
            self.vector_botones = []    
  
            
    def matriz_vacia(self):
        self.vector = []
        for i in range(6):
            for j in range(7):
                self.vector += [[]]
            self.matriz_batalla += [self.vector]
            self.vector = []
        self.crear_obstaculos()
        

    def crear_obstaculos(self):
        obstaculos = 0
        while obstaculos < 10:
            i = random.randint(0,5)
            j = random.randint(0,6)
            if self.matriz_batalla[i][j] != "x":
                self.matriz_batalla[i][j] = "x"
                obstaculos += 1

    def posicion_aleatorea(self):
        self.reiniciar_matriz()
        self.reiniciar_botones()         
        if self.turno:
            self.label_turno["text"] = "Turno del jugador 1"
            i = len(self.personajes_j1)-1
            while i >= 0:
                i_j1 = random.randint(0,5)
                j_j1 = random.randint(0,6)
                if self.matriz_batalla[i_j1][j_j1] == []:
                    self.matriz_batalla[i_j1][j_j1] = ["j1",i]
                    i -= 1
                    
            i = len(self.personajes_j2)-1
            while i >= 0:
                i_j1 = random.randint(0,5)
                j_j1 = random.randint(0,6)
                if self.matriz_batalla[i_j1][j_j1] == []:
                    self.matriz_batalla[i_j1][j_j1] = ["j2",i]
                    i -= 1
                elif self.matriz_batalla[i_j1][j_j1] != "x":
                    if len(self.matriz_batalla[i_j1][j_j1]) == 2 and self.matriz_batalla[i_j1][j_j1][0] == "j1":
                        temp = self.matriz_batalla[i_j1][j_j1]
                        temp += ["j2",i]
                        i-=1
            self.actualizar_botones()
            self.turno = False        

        else:
            self.label_turno["text"] = "Turno del jugador 2"
            i = len(self.personajes_j1)-1
            while i >= 0:
                i_j1 = random.randint(0,5)
                j_j1 = random.randint(0,6)
                if self.matriz_batalla[i_j1][j_j1] == []:
                    self.matriz_batalla[i_j1][j_j1] = ["j1",i]
                    i -= 1
                    
            i = len(self.personajes_j2)-1
            while i >= 0:
                i_j1 = random.randint(0,5)
                j_j1 = random.randint(0,6)
                if self.matriz_batalla[i_j1][j_j1] == []:
                    self.matriz_batalla[i_j1][j_j1] = ["j2",i]
                    i -= 1
                elif self.matriz_batalla[i_j1][j_j1] != "x":
                    if len(self.matriz_batalla[i_j1][j_j1]) == 2 and self.matriz_batalla[i_j1][j_j1][0] == "j1":
                        temp = self.matriz_batalla[i_j1][j_j1]
                        temp += ["j2",i]
                        i-=1
            self.actualizar_botones()                        
            self.turno = True
        self.gane()
                    
            
    def reiniciar_matriz(self):
        for i in range(6):
            for j in range(7):
                if self.matriz_batalla[i][j] != "x":
                    if self.matriz_batalla[i][j] != []:
                        self.matriz_batalla[i][j] = []
                        
    def actualizar_botones(self):
        for i in range(6):
            for j in range(7):
                if self.matriz_batalla[i][j] != "x" and self.matriz_batalla[i][j] != []:
                    if len(self.matriz_batalla[i][j])  == 2:
                        if self.matriz_batalla[i][j][0] == "j1":
                            pos = self.matriz_batalla[i][j][1]
                            rol = self.personajes_j1[pos][0]
                            imagen = ImageTk.PhotoImage(Image.open("Recursos\Personajes\\"+rol+"_j1_"+str(self.escenario)+".png").resize((100,100)))
                            self.matriz_botones[i][j]["image"] = imagen
                            self.matriz_botones[i][j]["width"] = 67
                            self.matriz_botones[i][j]["height"] = 80
                            self.matriz_botones[i][j].image = imagen
                        else:
                            pos = self.matriz_batalla[i][j][1]
                            rol = self.personajes_j2[pos][0]
                            imagen = ImageTk.PhotoImage(Image.open("Recursos\Personajes\\"+rol+"_j2_"+str(self.escenario)+".png").resize((100,100)))
                            self.matriz_botones[i][j]["image"] = imagen
                            self.matriz_botones[i][j]["width"] = 67
                            self.matriz_botones[i][j]["height"] = 80
                            self.matriz_botones[i][j].image = imagen
                    else:
                        if self.turno:
                            pos = self.matriz_batalla[i][j][1]
                            pos_2 = self.matriz_batalla[i][j][3]
                            imagen = ImageTk.PhotoImage(Image.open("Recursos\Escenarios\Batalla.png").resize((100,100)))
                            self.matriz_botones[i][j]["width"] = 67
                            self.matriz_botones[i][j]["height"] = 80
                            self.matriz_botones[i][j]["image"] = imagen
                            self.matriz_botones[i][j].image = imagen      
                            self.matriz_botones[i][j]["command"] = lambda i=i,j=j:self.batalla(i,j)
                        else:
                            pos = self.matriz_batalla[i][j][1]
                            pos_2 = self.matriz_batalla[i][j][3]
                            imagen = ImageTk.PhotoImage(Image.open("Recursos\Escenarios\Batalla.png").resize((100,100)))
                            self.matriz_botones[i][j]["width"] = 67
                            self.matriz_botones[i][j]["height"] = 80
                            self.matriz_botones[i][j]["image"] = imagen
                            self.matriz_botones[i][j].image = imagen      
                            self.matriz_botones[i][j]["command"] = lambda i=i,j=j:self.batalla(i,j)
                else:
                    if self.matriz_batalla[i][j] == "x":
                        imagen = ImageTk.PhotoImage(Image.open("Recursos\Escenarios\Obstaculo_"+str(self.escenario)+".png").resize((100,100)))
                        self.matriz_botones[i][j]["width"] = 67
                        self.matriz_botones[i][j]["height"] = 80
                        self.matriz_botones[i][j]["image"] = imagen
                        self.matriz_botones[i][j].image = imagen                        
                        
                    else:
                        imagen = ImageTk.PhotoImage(Image.open("Recursos\Escenarios\Textura_"+str(self.escenario)+".png").resize((100,100)))
                        self.matriz_botones[i][j]["width"] = 67
                        self.matriz_botones[i][j]["height"] = 80
                        self.matriz_botones[i][j]["image"] = imagen
                        self.matriz_botones[i][j].image = imagen
                        
                        
    
                            
    def reiniciar_botones(self):
        for i in range(6):
            for j in range(7):
                if self.matriz_botones[i][j] != "x":
                    self.matriz_botones[i][j]["bg"] = "white"
                    self.matriz_botones[i][j]["image"] = ""
                    self.matriz_botones[i][j]["width"] = 9
                    self.matriz_botones[i][j]["height"] = 5
                    

                    
    def batalla(self,i,j):
        imagen = imagen = ImageTk.PhotoImage(Image.open("Recursos\Escenarios\Escenario_"+str(self.escenario)+".png").resize((1366,768 ), Image.ANTIALIAS))
        bg = Label(self.master)
        bg["image"] = imagen
        bg.image= imagen
        bg.place(x = 0, y = 0)
        if not self.turno:
            self.peleando = Label(self.master,text = "El jugador 1 esta peleando",font = ("Arial",25))
        else:
             self.peleando = Label(self.master,text = "El jugador 2 esta peleando",font = ("Arial",25))
             
        self.peleando.place(x= 500, y = 20) 
        self.label_j1 = Label(self.master,text = "Jugador 1",font = ("Arial",25))
        self.label_j1.place(x= 63, y = 20)
        self.label_j2 = Label(self.master,text = "Jugador 2",font = ("Arial",25))
        self.label_j2.place(x= 1153, y = 20)
        
        pos_j1 = self.matriz_batalla[i][j][1]
        pos_j2 = self.matriz_batalla[i][j][3]
        
        ruta = "Recursos\Personajes\\"+str(self.personajes_j1[pos_j1][0])+"_j1_1.png"
        imagen = ImageTk.PhotoImage(Image.open(ruta).resize((200, 230), Image.ANTIALIAS))
        self.label_batalla_j1 = Label(self.master,image = imagen)
        self.label_batalla_j1.place(x = 100, y = 200)
        self.label_batalla_j1.image = imagen

        stats =["Fuerza","Inteligencia","Defenza","Ataque","Combates ganados"]
        texto_stats = ""
        for i in range(len(self.personajes_j1[pos_j1][1])):
            texto_stats += str(stats[i])+" : "+str(self.personajes_j1[pos_j1][1][i])+"\n\n"

        self.stats_j1 = Label(self.master, text = texto_stats,width = 20)
        self.stats_j1.place(x = 0, y = 620)
        
        ruta = "Recursos\Personajes\\"+str(self.personajes_j2[pos_j2][0])+"_j2_1.png"
        imagen = ImageTk.PhotoImage(Image.open(ruta).resize((200, 230), Image.ANTIALIAS))
        self.label_batalla_j2 = Label(self.master,image = imagen)
        self.label_batalla_j2.place(x = 1070, y = 200)
        self.label_batalla_j2.image = imagen
        
        stats =["Fuerza","Inteligencia","Defenza","Ataque","Combates ganados"]
        texto_stats = ""
        for i in range(len(self.personajes_j2[pos_j2][1])):
            texto_stats += str(stats[i])+" : "+str(self.personajes_j2[pos_j2][1][i])+"\n\n"

        self.stats_j2 = Label(self.master, text = texto_stats,width = 20)
        self.stats_j2.place(x = 1220, y = 620)

        self.pelear = Button(self.master, text = "Pelear", font = ("Arial", 14),width = 10,command = lambda:self.combate(pos_j1,pos_j2))
        self.pelear.place(x = 550, y = 720)

        self.huir = Button(self.master, text = "Huir", font = ("Arial", 14),width = 10, command = lambda:self.cerrar_widgets("self.widgets_batalla"))
        self.huir.place(x = 700, y = 720)
        self.widgets_batalla += [self.peleando,self.label_j1,self.label_j2,self.label_batalla_j1,self.stats_j1,
                                 self.stats_j2,self.label_batalla_j2,self.label_batalla_j2,self.pelear,self.huir,bg]

    
        
    def combate(self,pos_j1,pos_j2):

        self.soldado_j1 = self.personajes_j1[pos_j1]
        stats_j1 = self.personajes_j1[pos_j1][1]
        rol_j1 = self.personajes_j1[pos_j1][0]
        suma_stats_j1 = self.sumar_stats(stats_j1)
        fuerza_j1 = self.personajes_j1[pos_j1][1][0]
        inteligencia_j1 = self.personajes_j1[pos_j1][1][1]
        defenza_j1 = self.personajes_j1[pos_j1][1][2]
        ataque_j1 = self.personajes_j1[pos_j1][1][3]
        combates_ganados_j1 = self.personajes_j1[pos_j1][1][4]
        
        self.soldado_j2 = self.personajes_j2[pos_j2][1]
        stats_j2 = self.personajes_j2[pos_j2][1]
        rol_j2 = self.personajes_j2[pos_j1][0]
        suma_stats_j2 = self.sumar_stats(stats_j2)
        fuerza_j2 = self.personajes_j2[pos_j2][1][0]
        inteligencia_j2 = self.personajes_j2[pos_j2][1][1]
        defenza_j2 = self.personajes_j2[pos_j2][1][2]
        ataque_j2 = self.personajes_j2[pos_j2][1][3]
        combates_ganados_j2 = self.personajes_j2[pos_j2][1][4]

        if not self.turno:
            indice_daño_j1 = self.calcular_daño(suma_stats_j1,suma_stats_j2,inteligencia_j1,defenza_j1,fuerza_j2,ataque_j2)
            indice_defenza_j2 = int(suma_stats_j2 * ((suma_stats_j2*(inteligencia_j2*defenza_j2))//(suma_stats_j1*(fuerza_j1*ataque_j1))))
            if indice_daño_j1 > indice_defenza_j2:
                self.personajes_muertos_j2 += self.personajes_j2[pos_j2]
                self.personajes_j2.pop(pos_j2)
                combates_ganados_j1 += 1
                self.personajes_j1[pos_j1][1][4] = combates_ganados_j1
                
                self.cuadro_dialogo("Ganó el jugador 1")
            else:
                self.cuadro_dialogo("El jugador 2 esquivó el ataque")
                
                
        else:
            indice_daño_j2 = self.calcular_daño(suma_stats_j2,suma_stats_j1,inteligencia_j2,defenza_j2,fuerza_j1,ataque_j1)
            indice_defenza_j1 = int(suma_stats_j1 * ((suma_stats_j1*(inteligencia_j1*defenza_j1))//(suma_stats_j2*(fuerza_j2*ataque_j2))))
            if indice_daño_j2 > indice_defenza_j1:
                self.personajes_muertos_j1 += self.personajes_j1[pos_j1]
                self.personajes_j1.pop(pos_j1)
                combates_ganados_j2 += 1
                self.personajes_j2[pos_j2][1][4] = combates_ganados_j2
                self.cuadro_dialogo("Ganó el jugador 2")
            else:
                self.cuadro_dialogo("Ganó el jugador 2")

    def cuadro_dialogo(self,mensaje):
        cuadro  = Label(self.master, text = mensaje, font = ("Arial",24),width = 40, height = 5)
        cuadro.place(x = 300, y = 500)
        self.widgets_batalla += [cuadro]
        self.master.update()
        self.deshabilitar_botones()
        time.sleep(5)
        self.cerrar_widgets("self.widgets_batalla")

    def gane (self):
        if  len(self.personajes_j1) == 0:
            self.bg.lift()
            self.label_gane = Label(self.master, text ="El jugador 2 ha ganado", font = ("Arial",40)).place(x = 400, y = 300)
            self.reiniciar = Button(self.master, text = "Jugar de nuevo", font = ("Arial",14), command = lambda: self.menu()).place(x = 400, y = 300)
            
            
        elif len(self.personajes_j2) == 0:
            self.bg.lift()
            self.label_gane = Label(self.master, text ="El jugador 1 ha ganado", font = ("Arial",40)).place(x = 400, y = 300)
            self.reiniciar = Button(self.master, text = "Jugar de nuevo", font = ("Arial",14), command = lambda: self.menu()).place(x = 400, y = 300)
            
            
    def deshabilitar_botones(self):
        for i in range(6):
            for j in range(7):
                self.matriz_botones[i][j]["command"] =lambda: None
        

    def calcular_daño(self,rol_j1,rol_j2,suma_stats_j1,fuerza_j1,ataque_j1,defenza_j2):
            if rol_j1 == rol_j2:
                critica = random.randint (85,100)
                daño = 0.1 * 1.5* critica * (((0.1*suma_stats_j1+1)*(fuerza_j1*ataque_j1)//25*defenza_j2)+2)
                
            else:
                critica = random.randint (85,100)
                daño = 0.1 * 1* critica * (((0.1*suma_stats_j1+1)*(fuerza_j1*ataque_j1)//25*defenza_j2)+2)
                
            return int(daño)
                       
        
    def sumar_stats(self,stats):
        sumatoria_stats = 0
        for i in stats:
            sumatoria_stats += i
        return sumatoria_stats
            
            
##        if not self.turno:
##            
##            
##        else:

    
        
                
            
            
            

root = Tk()
aplicacion = ventana_principal(root)
aplicacion.menu()
#aplicacion.iniciar_juego(1)
#aplicacion.crear_personaje(1)
#aplicacion.iniciar_juego()

