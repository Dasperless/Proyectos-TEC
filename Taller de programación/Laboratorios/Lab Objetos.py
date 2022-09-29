#--------------------------------------------Citas medicas
class Citas:
    def __init__(self, NumeroCita, NombrePaciente,FechaCita):
        self.NumeroCita = NumeroCita
        self.NombrePaciente = NombrePaciente
        self.FechaCita = FechaCita
        self.ExamenesMedicos = []
        
        
    def RegistrarExamenes(self, MedicoSolicitante, NombreExamen, Tipo):
        self.ExamenesMedicos += [[MedicoSolicitante,NombreExamen, Tipo.upper()]]
        print("Se ha registrado el examen exitosamente")

    def PrimerUltimoExamen(self):
        if self.ExamenesMedicos == []:
            return "No hay exámenes previamente registrados."
        else:
            print(" -> Primer examen\n","Nombre: ", self.ExamenesMedicos[0][0])
            print("Nombre del examen: ",self.ExamenesMedicos[0][1])
            print("Tipo de examen:", self.ExamenesMedicos[0][2])
            print(" -> Último examen\n","Nombre: ", self.ExamenesMedicos[-1][0])
            print("\n","Nombre del examen: ",self.ExamenesMedicos[-1][1])
            print("Tipo de examen:", self.ExamenesMedicos[-1][2],"\n")


    def MostrarExamenes(self):
        if self.ExamenesMedicos == []:
            return "No hay exámenes previamente registrados."
        else:
            for i in range(len(self.ExamenesMedicos)):
                print(" Nombre: ", self.ExamenesMedicos[i][0],"\n","Nombre del examen: ",self.ExamenesMedicos[i][1],"\n","Tipo de examen:", self.ExamenesMedicos[i][2],"\n")

    def ExamenesUrgentes(self):
        if self.ExamenesMedicos == []:
            return "No hay exámenes previamente registrados."
        else:
            existe = False
            for i in range(len(self.ExamenesMedicos)):
                if self.ExamenesMedicos[i][2] == "URGENTE":
                     print(" Nombre: ", self.ExamenesMedicos[i][0])
                     print(" Nombre del examen: ",self.ExamenesMedicos[i][1])
                     print(" Tipo de examen:", self.ExamenesMedicos[i][2])
                     existe = True
                 
            if not existe:
                return "No hay citas urgentes"

    def InfoCita (self):
        print("Numero de cita: ", self.NumeroCita)
        print("Nombre del Paciente: ", self.NombrePaciente)
        print("Fecha: ", self.FechaCita)
        print("->Examenes Medicos")
        self.ExamenesUrgentes()

##                
###--------------------------------------------Incapacidades
class Incapacidad:
    def __init__(self, NombreColaborador, IdColaborador, FechaInicio, FechaFinal, MontoSubsidio):
        self.NombreColaborador = NombreColaborador
        self.IdColaborador = IdColaborador
        self.FechaInicio = FechaInicio
        self.FechaFinal = FechaFinal
        self.MontoSubsidio = MontoSubsidio
        self.Estado = "POR PAGAR"

    def MontoPagar(self):
        monto = self.FechaInicio-self.FechaFinal * self.MontoSubsidio
        print(monto)

    def PagarIncapacidad(self):
        if self.Estado == "POR PAGAR":
            self.Estado = "PAGADO"
        else:
            print("No puede pagarse una incapacidad que ha sido pagada previamente")

    def infoIncapacidad(self):
        print("Nombre del colaborador: ", self.NombreColaborador)
        print("Identificacion del colaborador: ",self.IdColaborador)
        print("Fecha de incio",self.FechaInicio)
        print("Fecha Final",self.FechaFinal)
        print("Monto del subsidio",self.MontoSubsidio)
        print("Estado",self.Estado)
        

    
        
    
