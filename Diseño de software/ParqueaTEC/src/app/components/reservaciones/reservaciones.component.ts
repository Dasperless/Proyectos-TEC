import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { FacadeService } from 'src/app/services/facade.service';
import { Campo } from 'src/app/shared/template/Campo';
import { CampoVisitantes } from 'src/app/shared/template/CampoVisitantes';
import { CampoVehiculosOficiales } from 'src/app/shared/template/CampoVehiculosOficiales';
import { CampoEstandar } from 'src/app/shared/template/CampoEstandar';
import { CampoJefatura } from 'src/app/shared/template/CampoJefatura';
import { CampoDiscapacitado } from 'src/app/shared/template/CampoDiscapacitado';
import { elementAt } from 'rxjs';


@Component({
  selector: 'app-reservaciones',
  templateUrl: './reservaciones.component.html',
  styleUrls: ['./reservaciones.component.css']
})
export class ReservacionesComponent implements OnInit {
  currentView:string = "Reservar";
  headers:any = {
    numeroCampo: "Numero de campo",
    tipoEspacio: "Tipo de espacio",
    funcionario: "Funcionario",
    invitados: "Invitados",
    parqueo: "Parqueo",
    direccion: "Direccion",
    indicaciones: "Indicaciones",
    fecha:"Fecha",
    horaEntrada: "Hora de entrada",
    horaSalida: "Hora de salida"
  };

  ticket:any={};
  idFuncionario: any= this.route.snapshot.params['idFuncionario'];
  idParqueo: any= this.route.snapshot.params['idParqueo'];
  funcionario:any;
  parqueo:any;

  visitante:any = {};
  vehiculoOficial:any={};
  campos:Campo[] = [];
  reservas:any =null;
  reservas2:any =null;

  visitanteForm = this.formBuilder.group({
    nombre: ['', Validators.required],
    identificacion: ['', Validators.required],
    numeroVehiculo: ['', Validators.required],
    motivoVisita: ['', Validators.required],
    sitioDondeSeDirige: ['', Validators.required]
  });
  
  vehiculoOficialForm = this.formBuilder.group({
    placa: ['', Validators.required],
    modelo: ['', Validators.required],
    color: ['', Validators.required],
    chofer: ['', Validators.required]
  });

  reservacionForm = this.formBuilder.group({
    fechaReservacion: ['', Validators.required],
    horaEntrada: [' '],
    horaSalida: [' '],
  });

  constructor( 
    private route: ActivatedRoute,
    private facade: FacadeService,
    private formBuilder: FormBuilder
  ) { }

  ngOnInit(): void {
    // Funcionario
    this.facade
    .getFuncionarioById(this.idFuncionario)
    .subscribe(
      {
        next: (funcionario) => {
          this.funcionario = funcionario;
          // Parqueo
          this.facade
          .getParqueoById(this.idParqueo)
          .subscribe(
            {
              next: (parqueo) => {
                this.parqueo = parqueo;
                this.generarCampos(this.funcionario,this.parqueo);
              }
          });          
          this.generarCampos(this.funcionario,this.parqueo);
        }
    });
    //Traer reservaciones

  }



  

  /**
   * @param perfil Tipo de perfil del funcionario
   * @param espacios json con los espacios de la bd
   */
   generarCampos(funcionario:any,parqueo:any) {
    // Espacios que pueden usar
    let espacios = parqueo?.Espacios;
    let perfil = funcionario?.tipoPerfil;
    let tipoEspacio ={
      Funcionario:["Estandar"],
      Jefatura:["Visitante","Jefatura"],
      Operador:["Oficial"],
      Administrativo:["Visitante"]
    }
    let filtro = tipoEspacio[perfil as keyof typeof tipoEspacio];
    let espaciosFiltrados = this.facade.filtrarCampos(espacios,filtro);
    for(let espacio of espaciosFiltrados) {
      let campo:any;
      switch(espacio.tipo) {
        case "Estandar":
          campo = new CampoEstandar(espacio, funcionario,parqueo)
          break;
        case "Jefatura":
          campo = new CampoJefatura(espacio, funcionario,parqueo)
          break;
        case "Oficial":
          campo = new CampoVehiculosOficiales(espacio, funcionario,parqueo)
          break;
        case "Discapacitado":
          campo = new CampoDiscapacitado(espacio, funcionario,parqueo)
          break;
        case "Visitante":
          campo = new CampoVisitantes(espacio, funcionario,parqueo)
          break;
      }
      this.campos.push(campo);
    }
  }

  /**
   * Obtiene las llaves de un objeto
   * @param obj Objeto a obtener las propiedades
   * @returns {string[]} Array con las llaves del objeto
   */
  objectKeys(obj:object):string[] {
    if(obj) {
      return Object.keys(obj);
    }else{
      return [];
    }
  }

  /**
   * Agrega un visitante
   */
  newVisitante() {
    if(this.visitanteForm.valid) {
      this.visitante = this.visitanteForm.value;
      alert("Se ha agregado un visitante");

      this.setCurrentView("Reservar");
    }else{
      alert("Faltan datos");
    }
  }

  /**
   * Agrega un vehículo oficial
   */
  newVehiculoOficial(){
    if(this.vehiculoOficialForm.valid) {
      this.vehiculoOficial = this.vehiculoOficialForm.value;
      alert("Vehiculo agregado");
      this.setCurrentView("Reservar");
    }else{
      alert("Faltan datos");
    }
  }



  
  compareHour(pHora1:string,pHora2:string){   
    let hora1Arr = pHora1.split(/[:]+/)
    let hora2Arr = pHora2.split(/[:]+/)
    let hora1:number = parseInt(hora1Arr[0])
    let hora2:number = parseInt(hora2Arr[0])
    let minutos1:number = parseInt(hora1Arr[1])
    let minutos2:number = parseInt(hora2Arr[1])
    if(hora1 > hora2){
        return true;
    }else if(hora1 == hora2 && minutos1 >= minutos2){
        return true
    }
    return false;
}
  /**
   * Establece la vista actual
   * @param view Nombre de la vista a mostrar
   */
  setCurrentView(view:string) {
    this.currentView = view;
  }

  solicitarReservacion() {
      let reservacion = this.reservacionForm.value; //Reservacion
      let camposFiltrados = this.getCamposPorTipoReserva()
      let camposOcupados:any = [];
      this.facade.getFuncionarioById(this.idFuncionario).subscribe
      (
        {
          next:(funcionario) =>{
            console.log("subscribe de funcionario");
            this.funcionario =funcionario;
            this.facade.getReservas()
            .subscribe(
          {
            next: (response) => {
              console.log("subscribe de reservas");
              this.reservas = response;
              for(let reserva of this.reservas){
                if(this.funcionario.tipoPerfil== "Jefatura" || this.funcionario.tipoPerfil=="Administrativo"){
                  console.log("if de valicadion de jefe o administador");
                  if(reserva.idParqueo == this.idParqueo && reservacion.fechaReservacion==reserva.fecha){
                    if(reserva.tipoCampo!="Oficial"){              
                      camposOcupados.push(reserva.numeroCampo);
                    }
                
                }
              }
                else if(this.funcionario.tipoPerfil=="Funcionario"){

                  console.log("if de funcionario")
                  if(reserva.tipoCampo=="Oficial" || reserva.tipoCampo==='undefine'){
                    console.log("reservaOficial");
                  }
                  else{

                    if(reserva.idParqueo == this.idParqueo && reservacion.fechaReservacion==reserva.fecha){
                      console.log("validacion de parqueo y fecha funcionario");
                      if(this.compareHour(reserva.horaEntrada,reservacion.horaEntrada) && this.compareHour( reserva.horaSalida,reservacion.horaSalida) ){
                        camposOcupados.push(reserva.numeroCampo);
                      }

                      else if(this.compareHour(reserva.horaEntrada, reservacion.horaEntrada) &&  this.compareHour(reservacion.horaSalida, reserva.horaEntrada)){
                        camposOcupados.push(reserva.numeroCampo);
                      }
                       else if(this.compareHour(reserva.horaSalida, reservacion.horaEntrada) && this.compareHour(reservacion.horaSalida, reserva.horaSalida) ){
                          
                         
                       camposOcupados.push(reserva.numeroCampo);
                            
                          }
                      
                        
                       
              
                      
                    }
                  }

                  
                }
                else if(this.funcionario.tipoPerfil=="Operador"){
                  if(reserva.estado){
                    camposOcupados.push(reserva.numeroCampo);
                  }
                }
                
              
            }
            console.log(camposOcupados) 
            let counter=0
            let ocupado=false;
            let encontreCampo=false;

            
              for(let campo of camposFiltrados) {
                if(camposOcupados.length>0){
                  console.log("hay campos ocupados")
                  while(counter<camposOcupados.length){
                    if(campo.data.numeroCampo==camposOcupados[counter]){
                      ocupado= true;
                      break;
                    }
                    counter=counter+1;
                  }
                      if(!ocupado){
                        let response = campo.solicitarReservacion(reservacion);
                      if(response['stop']){
                        alert(response['message']);
                        break ;
                      }
                      if(response['success']){
                        alert(response['message']);
                        this.ticket = response['tiquete']
                        encontreCampo=true;
                        break ;
                      }
                      }
                      else{
                        ocupado= false;
                        counter=0;
                      }
          
                    
                  
                }
                else{
                  console.log("no hay campos ocupados")
                  let response = campo.solicitarReservacion(reservacion);
                  if(response['stop']){
                    alert(response['message']);
                    break;
                  }
                  if(response['success']){
                    alert(response['message']);
                    this.ticket = response['tiquete']
                    encontreCampo=true;
                    break;
                  }
                }
            }
            if(!encontreCampo){
              alert("no se encontro un campo disponible")
            }


            }
            
            
          }
          
        );
          }
      
        })
        
        
      

      

  }

  getCamposPorTipoReserva(){
    if(["Jefatura","Administrativo"].includes(this.funcionario.tipoPerfil)){
      if(this.visitanteForm.invalid){
        return this.filtrarCampoPorTipo(this.campos,"Jefatura")
      }else{
        let camposVisitante = this.filtrarCampoPorTipo(this.campos,"Visitante")
        camposVisitante.forEach((campo:any) => {
          campo.setVisitante(this.visitante)
        });
        return camposVisitante
      }
    }
    else if(this.funcionario.tipoPerfil === "Operador"){
      if(this.visitanteForm.invalid){
        this.campos.forEach(
          (campo:any) => {
            campo.setVehiculo(this.vehiculoOficial)
          });
        return this.campos
      }
    }else{
      return this.campos
    }
  }

  filtrarCampoPorTipo(campos:any,tipo:string){
    return campos.filter((campo:any)=>{
      if(campo.data.tipo == tipo){
        return true
      }
      return false
    })
  }

  newReserva(){
    if(this.reservacionForm.valid){
      this.ticket['idFuncionario'] = this.idFuncionario
      this.ticket['idParqueo'] = this.idParqueo
      this.ticket['estado'] = true

      this.facade
      .newReserva(this.ticket,this.idFuncionario,this.idParqueo)
      .subscribe(
        {
          next:()=>{
            alert('Se ha realizado la reserva');
          }
      });
    }
  }

}
