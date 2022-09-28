import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ReservacionService {


  constructor(private http: HttpClient, private router: Router) { }

  public filtrarCampos(array:any[],filtros: any[]): any {
    if(array === undefined ||array.length < 0 ) return [];
    if(filtros === undefined || filtros.length < 0 ) return array;
    return array.filter((item) => {
      let tipo = item.tipo;
      if(filtros.includes(tipo)) {
        return item;
      }
    })
  }

  /**
   * Obtiene las reservas de la base de datos
   * @returns {Observable<any>} Array con Json de los parqueos
   */
   getReserva(){
    return this.http.get(`${environment.URL}/reserva`);
  }

  /**
   * Obtiene un parqueo de la base de datos por su id
   * @param id Id del parqueo a buscar
   * @returns {Observable<any>} Json del parqueo
   */
  getReservaById(id: string) {
    return this.http.get(`${environment.URL}/reserva/${id}`);
  }

  /**
   * Elimina un parqueo por su id 
   * @param id Id del parqueo a eliminar
   * @returns {Observable<any>} Json con la respuesta de la peticion
   */
  eliminarReserva(id: string) {
    return this.http.delete(`${environment.URL}/eliminarReserva/${id}`);
  }

  /**
   * Actualiza un parqueo en la base de datos
   * @param id Id del parqueo a actualizar
   * @param Reserva Json con los datos a actualizar
   * @returns {Observable<any>} Json con la respuesta de la peticion
   */
  editarReserva(id: string, Reserva: any) {
    return this.http.put(`${environment.URL}/editarReserva/${id}`, Reserva);
  
  }

  /**
   * Registra un nuevo parqueo en la base de datos
   * @param Reserva Json con los datos del parqueo a crear
   * @returns {OBservable<any>} Json con la respuesta de la peticion
   */
  newReserva(Reserva: any,idFuncionario: string, idParqueo: string,) {
    return this.http.post<any>(`${environment.URL}/reservar/${idFuncionario}/${idParqueo}`, Reserva);
  }   
  
  getReservasByIdParqueo(idParqueo:string){
    return this.http.get(`${environment.URL}/reservas/${idParqueo}`);

  }
  

}
