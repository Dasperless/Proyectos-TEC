import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { environment } from '../../environments/environment';
@Injectable({
  providedIn: 'root'
})

export class AuthService {

  constructor(private http: HttpClient, private router: Router) { }

  login(user: any) {
    return this.http.post<any>(`${environment.URL}/login`, user);
  }

  register(user: any) {
    return this.http.post<any>(`${environment.URL}/registrarFuncionario`, user);
  } 

  isLoggedIn():Boolean {
    return !!localStorage.getItem('token');
  }

  isAdmin():Boolean {
    let isAdmin = localStorage.getItem('isAdmin');
    if(isAdmin !== null && isAdmin !== undefined) {
      return JSON.parse(isAdmin);
    }
    return false;
  }

  logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('isAdmin');
    this.router.navigate(['/login']);
  }
}
