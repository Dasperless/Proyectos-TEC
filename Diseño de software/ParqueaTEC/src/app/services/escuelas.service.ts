import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class EscuelasService {

  constructor(
      private http: HttpClient
  ) { }

  /**
   * Obtiene todas las escuelas
   * @returns {Observable<any>} Observable con las escuelas en formato json 
   */
  getEscuelas(){
    return this.http.get(`${environment.URL}/escuelas`);
  }

  /**
   * Obtiene una escuela por su id
   * @param id id de la escuela
   * @returns {Observable<any>} Observable con la escuela en formato json
   */
  getEscuela(id:string):Observable<any>{
    return this.http.get(`${environment.URL}/escuela/${id}`);
  }

}

