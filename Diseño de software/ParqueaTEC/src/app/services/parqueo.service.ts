import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ParqueoService {

  /**
   * Obtiene los parqueos de la base de datos
   * @returns {Observable<any>} Array con Json de los parqueos
   */
  getParqueos(){
    return this.http.get(`${environment.URL}/parqueos`);
  }

  /**
   * Obtiene un parqueo de la base de datos por su id
   * @param id Id del parqueo a buscar
   * @returns {Observable<any>} Json del parqueo
   */
  getParqueoById(id: string) {
    return this.http.get(`${environment.URL}/parqueos/${id}`);
  }

  /**
   * Elimina un parqueo por su id 
   * @param id Id del parqueo a eliminar
   * @returns {Observable<any>} Json con la respuesta de la peticion
   */
  eliminarParqueo(id: string) {
    return this.http.delete(`${environment.URL}/eliminarParqueo/${id}`);
  }

  /**
   * Actualiza un parqueo en la base de datos
   * @param id Id del parqueo a actualizar
   * @param Parqueo Json con los datos a actualizar
   * @returns {Observable<any>} Json con la respuesta de la peticion
   */
  updateParqueo(id: string, Parqueo: any) {
    return this.http.put(`${environment.URL}/editarParqueo/${id}`, Parqueo);
  
  }

  /**
   * Registra un nuevo parqueo en la base de datos
   * @param Parqueo Json con los datos del parqueo a crear
   * @returns {OBservable<any>} Json con la respuesta de la peticion
   */
  newParqueo(Parqueo: any) {
    return this.http.post<any>(`${environment.URL}/registrarParqueo`, Parqueo);
  } 

  constructor(private http: HttpClient, private router: Router) { }
}
