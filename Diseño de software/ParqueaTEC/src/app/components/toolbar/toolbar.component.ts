import { Component, OnInit } from '@angular/core';
import { FacadeService } from 'src/app/services/facade.service';
@Component({
  selector: 'app-toolbar',
  templateUrl: './toolbar.component.html',
  styleUrls: ['./toolbar.component.css'],
})
export class ToolbarComponent implements OnInit {
  notificaciones: boolean = false;
  isAdmin = this.facade.isAdmin();
  id = localStorage.getItem('token');

  constructor(
    private facade: FacadeService
    ) {}

  ngOnInit(): void {
    this.getNotificaciones();
    console.log(this.id);
  }

  click(event:any){
    this.notificaciones = !this.notificaciones;
    if(this.id !== undefined && this.id !== null){  
      if(this.notificaciones){
        event.preventDefault();
      }
      this.notificaciones = !!this.notificaciones;
      
      this.facade
      .updateFuncionario(this.id, {notificaciones: this.notificaciones})

    }
  }

  getNotificaciones() {
    let id = localStorage.getItem('token');
    if (id === undefined || id === null) {
      this.notificaciones = false;
    } else {
      this.facade.getFuncionarioById(id).subscribe({
        next: (response: any) => {
          this.notificaciones = response.notificaciones;
        },
        error: (error: any) => {
          console.log(error);
        },
      });
    }
  }

}
