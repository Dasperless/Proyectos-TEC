import { Component, OnInit } from '@angular/core';
import { FuncionariosService } from 'src/app/services/funcionarios.service';
import { AuthService } from 'src/app/services/auth.service';
import { Router, ActivatedRoute } from '@angular/router';
import { FacadeService } from 'src/app/services/facade.service';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent implements OnInit {
  usuario:any;

  constructor(
    private facade: FacadeService,
  ) { }

  ngOnInit(): void {
    this.getUser();
  }

  logout(){
    this.facade.logout()
  }

  getUser(){
   let usertoken = localStorage.getItem('token')
   if(usertoken !== null){
      this.facade
      .getFuncionarioById(usertoken)
      .subscribe(
        {
          next: (data) => {
            this.usuario = data;
          },
          error: (err) => {
            console.error(err);
          }
        }
      );
   }
  }

}
