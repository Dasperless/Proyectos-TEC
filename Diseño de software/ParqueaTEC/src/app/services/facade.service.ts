import { Injectable, Injector } from '@angular/core';
import { FuncionariosService } from './funcionarios.service';
import { Observable } from 'rxjs';
import { EscuelasService } from './escuelas.service';
import { HorarioService } from './horario.service';
import { ParqueoService } from './parqueo.service';
import { PlacasService } from './placas.service';
import { ReservaService } from './reserva.service';
import { TPService } from './tipo-parqueo.service';
import { AuthService } from './auth.service';
import { Router } from '@angular/router';
import { LoginComponent } from '../components/login/login.component';
import { ReservacionService } from './reservacion.service';

@Injectable()
export class FacadeService {

  private _funcionariosService!: FuncionariosService;
  Router: any;

  public get funcionarioService(): FuncionariosService {
    if(!this._funcionariosService) {
      this._funcionariosService = this.injector.get(FuncionariosService);
    }
      return this._funcionariosService;
  }

  private _escuelasService!: EscuelasService;
  public get escuelasService(): EscuelasService {
    if(!this._escuelasService) {
      this._escuelasService = this.injector.get(EscuelasService);
    }
      return this._escuelasService;
  }

  private _horarioService!: HorarioService;
  public get horarioService(): HorarioService{
    if(!this._horarioService) {
      this._horarioService = this.injector.get(HorarioService);
    }
      return this._horarioService;
  }

  private _parqueoService!: ParqueoService;
  public get parqueoService(): ParqueoService {
    if(!this._parqueoService) {
      this._parqueoService = this.injector.get(ParqueoService);
    }
      return this._parqueoService;
  }

  private _placasService!: PlacasService;
  public get placasService(): PlacasService {
    if(!this._placasService) {
      this._placasService = this.injector.get(PlacasService);
    }
      return this._placasService;
  }

  private _TPService!: TPService;
  public get tipoParqueoService(): TPService{
    if(!this._TPService) {
      this._TPService = this.injector.get(TPService);
    }
      return this._TPService;
  }

  private _authService!: AuthService;
  public get authService(): AuthService {
    if(!this._authService) {
      this._authService = this.injector.get(AuthService);
    }
      return this._authService;
  }  

  private _reservacionService!: ReservacionService;
  public get reservacionService(): ReservacionService {
    if(!this._reservacionService) {
      this._reservacionService = this.injector.get(ReservacionService);
    }
      return this._reservacionService;
  }


  private _ReservaService!: ReservaService;
  public get ReservaService(): ReservaService {
    if(!this._ReservaService) {
      this._ReservaService = this.injector.get(ReservaService);
    }
      return this._ReservaService;
  }

  constructor(private injector:Injector) { }

  // Servicio de Funcionarios 

  getFuncionarios(): Observable<any> {
    return this.funcionarioService.getFuncionarios();
  }

  getFuncionarioById(id: string): Observable<any> {
    return this.funcionarioService.getFuncionarioById(id);
  }

  deleteFuncionario(id: string): boolean {
    let success = true
    this.funcionarioService
    .eliminarFuncionario(id)
    .subscribe(
      {
        error: (error: any) => {
          console.error(error);
          alert('Error al eliminar funcionario');
          success = false
        }
      }
    )
    return success;
  }
  
  updateFuncionario(id: string, funcionario: any): void{
    this.funcionarioService
      .updateFuncionario(id, funcionario)
      .subscribe(
        {
          next: () => {
            alert('Funcionario actualizado');
            this.injector.get(Router).navigate(['/visualizarFuncionarios']);
          },
          error: (error: any) => {
            alert('Error al actualizar el funcionario');
            console.error(error);            
          }
        }
      )
  }

  newFuncionario(funcionario: any): void {
    this.funcionarioService
      .newFuncionario(funcionario)
      .subscribe(
        {
          next: () => {
            alert('Funcionario registrado');
            this.injector.get(Router).navigate(['/visualizarFuncionarios']);
          },
          error: (error: any) => {
            console.error(error);
            alert('Error al registrar funcionario');
          }
        }
      )
  }

  // Servicio de autenticacion

  login(user: any):void {
    this.authService.login(user)
    .subscribe({
      next: (response: any) => 
        {
          let id = response.id;
          let esAdmin = response.esAdmin;
          if(id != null || id != undefined && esAdmin != null || esAdmin != undefined) {
            localStorage.setItem('token', response._id);
            localStorage.setItem('isAdmin', response.esAdmin);
          }else{
            alert('Error de login, contacte con el administrador');
            this.injector.get(LoginComponent).succesLogin = false;
          }
          if(response.esAdmin) {
            this.injector.get(Router).navigate(['/realizarReservacion']);
          }else{
            this.injector.get(Router).navigate(['/inicio']);
          }          
        },
      error: (error: any) => {
        console.log(error);
        alert('Error de login, contacte con el administrador');
      }
    }
    );
  }

  isLoggedIn(): Boolean {
    return this.authService.isLoggedIn();
  }

  isAdmin(): Boolean {
    return this.authService.isAdmin();
  }

  logout(): void {
    this.authService.logout();
  }

  // servicios de parqueo
  
  getParqueos(): Observable<any> {
    return this.parqueoService.getParqueos();
  }

  getParqueoById(id: string): Observable<any> {
    return this.parqueoService.getParqueoById(id);
  }

  deleteParqueo(id: string): boolean {
    let success = true
    this.parqueoService
    .eliminarParqueo(id)
    .subscribe(
      {
        error: (error: any) => {
          console.error(error);
          alert('Error al eliminar parqueo');
          success = false
          return success;
        }
      });
    return success;
  }

  updateParqueo(id: string, parqueo: any): void {
    this.parqueoService
      .updateParqueo(id, parqueo)
      .subscribe(
        {
          next: () => {
            alert('Parqueo actualizado');
            this.injector.get(Router).navigate(['/parqueos']);
          }
        }
      )
  }

  newParqueo(parqueo: any): void {
    this.parqueoService
      .newParqueo(parqueo)
      .subscribe(
        {
          next: () => {
            alert('Parqueo registrado');
            this.injector.get(Router).navigate(['/parqueos']);            
          },
          error: (error: any) => {
            console.error(error);
            alert('Error al registrar parqueo');
         }
      });
  }

  // servicios de placas

  getPlacas(idFuncionario: string): Observable<any> {
    return this.placasService.getPlacas(idFuncionario);
  }

  deletePlaca(idFuncionario: string, idPlaca:string): boolean{
    let success = true
    this.placasService
    .eliminarPlaca(idFuncionario, idPlaca)
    .subscribe(
      {
        error: (error: any) => {
          console.error(error);
          alert('Error al eliminar placa');
          success = false
          return success
        }
      }
    )
    return success;
  }

  updatePlaca(idFuncionario: string, idPlaca: string, placa: any):void{
    this.placasService
    .updatePlaca(idFuncionario, idPlaca, placa)
    .subscribe(
      {
        next: () => {
          alert('Placa actualizado');
          this.injector.get(Router).navigate(['/placas/'+idFuncionario]);
        },
        error: (error: any) => {
          alert('Error al actualizarplaca');
          console.log(error);
        }
      });
  }

  newPlaca(id: string, codigo: any): void {
    this.placasService
    .newPlaca(id,{codigo: codigo})
    .subscribe(
      {
        next: () => {
          alert('Placa registrado');
          this.injector.get(Router).navigate(['/placas/'+id]);
        },
        error: (error: any) => {
          console.error(error);
          alert('Error al registrar el funcionario');
        },
      });
  }

 // servicios de tipo de parqueo
  getTipoParqueo(){
    return this.tipoParqueoService.getTipoParqueo();
  }

  getTipoParqueoById(id: string){
    return this.tipoParqueoService.getTipoParqueoById(id);
  }

  // servicios de escuela
  getEscuelas(){
    return this.escuelasService.getEscuelas();
  }

  getEscuelaById(id: string){
    return this.escuelasService.getEscuela(id);
  }

  // servicios de horario

  getHorario(idUsuario: string){
    return this.horarioService.getHorario(idUsuario);
  }

  updateHorario(horario: Array<Object>, idUsuario: any):void{
    this.horarioService.updateHorario(horario,idUsuario)
    .subscribe(
      {
        next: () => {
          alert("Horario guardado correctamente");
        },
        error: (err) => {
          console.error(err);
          alert("Error al guardar el horario");
        }
      });
  }

  getFranjasHorarias(funcionario:any, dia:any){
    return this.horarioService.getFranjasHorarias(funcionario, dia);
  }


   // servicios de horario
   getReservas(){
    return this.ReservaService.getReserva();
  }

  getReserva(idReserva: any){
    return this.ReservaService.getReservaById(idReserva);
  }
  // servicios de reservacion

  filtrarCampos(array:any[],filtro: any):any {
    return this.reservacionService.filtrarCampos(array,filtro);
  }   
  
 newReserva(reservacion:any, idFuncionario:string, idParqueo:any){
  return this.reservacionService.newReserva(reservacion,idFuncionario,idParqueo);
 }

 getReservasByIdParqueo(idParqueo:string){
  return this.reservacionService.getReservasByIdParqueo(idParqueo);
 }
 eliminarReserva(idReserva:string){
  return this.reservacionService.eliminarReserva(idReserva);
 }
 
}
