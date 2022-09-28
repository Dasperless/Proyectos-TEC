import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class PlacasService {

  /**
   * Retorna un array con las placas de un funcionario
   * @param idFuncionario id del usuario
   * @returns {Observable<any>} Json con los datos de las placas
   */
  getPlacas(idFuncionario: string){
    return this.http.get(`${environment.URL}/placas/${idFuncionario}`);
  }

  /**
   * Elimina una placa de la base de datos
   * @param idFuncionario id del funcionario
   * @param idPlaca id de la placa
   * @returns {Observable<any>} Json con la respuesta de la peticion
   */
  eliminarPlaca(idFuncionario: string, idPlaca: string) {
    return this.http.delete(`${environment.URL}/eliminarPlaca/${idFuncionario}/${idPlaca}`);
  }

  /**
   * Actualiza una placa de la base de datos
   * @param idFuncionario id del funcionario
   * @param idPlaca id de la placa
   * @param placaActualizada Json con los datos de la placa actualizada
   * @returns {Observable<any>} Json con la respuesta de la peticion
   */
  updatePlaca(idFuncionario: string, idPlaca: any, placaActualizada: any) {
    return this.http.put(`${environment.URL}/editarPlaca/${idFuncionario}/${idPlaca}`, placaActualizada);
  }

  /**
   * Registra una nueva placa en la base de datos.
   * @param idFuncionario id del funcionario
   * @param placa Json con la placa a registrar
   * @returns {Observable<any>} Json con la respuesta de la peticion
   */
  newPlaca(idFuncionario: String, placa: any) {
    return this.http.post<any>(`${environment.URL}/registrarplaca/${idFuncionario}`, placa);
  } 

  constructor( private http: HttpClient, private router: Router) { }
}
