import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class FuncionariosService {

  constructor(private http: HttpClient) { }

  /**
   * Obtiene un funcionario por su id
   * @param id id del funcionario a buscar
   * @returns un objeto observable de tipo funcionario
   */
  getFuncionarioById(id: string): Observable<any> {
    return this.http.get(`${environment.URL}/funcionarios/${id}`);
  }

  /**
   * Retorna un arreglo con los funcionarios
   * @returns Un arreglo observable de los funcionarios
   */
  getFuncionarios(): Observable<any>{
    return this.http.get(`${environment.URL}/funcionarios`);
  }

  /**
   * Elimina un funcionario por su id
   * @param id id del funcionario a eliminar
   * @returns 
   */
  eliminarFuncionario(id: string): Observable<any> {
    return this.http.delete(`${environment.URL}/eliminarFuncionario/${id}`);
  }

  /**
   * Actualiza un funcionario por su id
   * @param id id del funcionario a actualizar
   * @param funcionario objeto con los datos a actualizar
   * @returns Una respuesta de que se actualizo o no
   */
  updateFuncionario(id: string, funcionario: any): Observable<any> {
    return this.http.put(`${environment.URL}/editarFuncionario/${id}`, funcionario);
  }

  /**
   * Crea un nuevo funcionario
   * @param funcionario Json con los datos del funcionario a crear
   * @returns Una respuesta si se creó o no
   */
  newFuncionario(funcionario: any) {
    return this.http.post<any>(`${environment.URL}/registrarFuncionario`, funcionario);
  } 
}
