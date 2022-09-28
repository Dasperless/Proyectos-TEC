import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class HorarioService {

  constructor(
    private http:HttpClient,
  ) { }

  /**
   * Obtiene el horario de un usuario
   * @param idUsuario id del usuario
   * @returns Observable del horario
   */
  getHorario(idUsuario:string): Observable<any> {
    return this.http.get<any>(`${environment.URL}/horario/${idUsuario}`);
  }

  /**
   * Actualiza el horario de un usuario
   * @param horario horario actualizado del usuario
   * @param idUsuario Id del usuario
   * @returns {Observable<any>} Json con la respuesta de la actualizacion
   */
  updateHorario(horario:Array<Object>, idUsuario:any):Observable<any> {
    return this.http.put(`${environment.URL}/editarHorario/${idUsuario}`, horario);
  }

  /**
   * Obtiene la franja horaria del funcionario
   * @param funcionario Json con los datos del funcionario a crear
   * @param dia dia del horario
   * @returns Franja hora del  funcionario
   */
  getFranjasHorarias(funcionario:any, dia:any): Observable<any> {
    let indiceDia:any ={'lunes': 0, 'martes': 1, 'miercoles': 2, 'jueves': 3, 'viernes': 4}
    return funcionario['horario'][indiceDia[dia]][dia];
  }

}
