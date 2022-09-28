import { Component, OnInit } from '@angular/core';
import { FacadeService } from 'src/app/services/facade.service';
@Component({
  selector: 'app-realizar-reservacion',
  templateUrl: './realizar-reservacion.component.html',
  styleUrls: ['./realizar-reservacion.component.css']
})
export class RealizarReservacionComponent implements OnInit {
  parqueos: any = [];
  idFuncionario: any;
  funcionario:any;
  constructor(
    private facade: FacadeService
  ) { }

  ngOnInit(): void {
   
    this.idFuncionario = localStorage?.getItem('token');
    this.getParqueos();
    this.facade.
    getFuncionarioById(this.idFuncionario)
    .subscribe(
      {
        next:(data:any)=>{
          
          this.funcionario=data;
    },
    error:(err)=>{
      console.log(err);
    }
  }
  );
   
  }

  getParqueos(){
    this.facade.getParqueos()
      .subscribe(
        {
          next: (parqueos) => {
            this.parqueos = parqueos;
          },
          error: (err) => {
            console.log(err);
          }
        }
      );
  }
  

}
