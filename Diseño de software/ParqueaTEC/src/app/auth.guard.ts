import { Injectable } from '@angular/core';
import { CanActivate } from '@angular/router';
import { Router } from '@angular/router';
import { FacadeService } from './services/facade.service';
@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {
  constructor (
    private facade: FacadeService,
    private router: Router
  ) {}

  canActivate( ):boolean{
    if (this.facade.isLoggedIn() && this.facade.isAdmin()) {
      return true;
    }
    this.router.navigate(['/login']);
    return false;
  }
  
}
