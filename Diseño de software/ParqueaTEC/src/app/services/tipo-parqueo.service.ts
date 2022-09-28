import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';


@Injectable({
  providedIn: 'root'
})
export class TPService {

  constructor(
      private http: HttpClient,
      private router: Router
  ) { }

  /**
   * Obtiene los tipos de parqueo
   * @returns {Observable<any>} El observable con los tipos de parqueo en formato Json
   */
  getTipoParqueo(){
    return this.http.get(`${environment.URL}/TipoParqueo`);
  }

  /**
   * Obtiene un tipo de parqueo por Id
   * @param id El id del tipo de parqueo
   * @returns {Observable<any>} El observable con el tipo de parqueo en formato Json
   */
  getTipoParqueoById(id: any){
    return this.http.get(`${environment.URL}/TipoParqueo/${id}`);
  }
}

