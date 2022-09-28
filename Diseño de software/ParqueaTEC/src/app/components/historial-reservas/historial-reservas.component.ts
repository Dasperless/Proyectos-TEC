import { Component, OnInit } from '@angular/core';
import { FacadeService } from 'src/app/services/facade.service';

@Component({
  selector: 'app-historial-reservas',
  templateUrl: './historial-reservas.component.html',
  styleUrls: ['./historial-reservas.component.css']
})
export class HistorialReservasComponent implements OnInit {
  reservaciones:any
  funcionario:any;
  constructor(
    private facade : FacadeService
  ) { }

  ngOnInit(): void {
    let idFuncionario:any = localStorage?.getItem('token');
    this.facade
    .getFuncionarioById(idFuncionario)
    .subscribe(
      {
        next:(funcionario:any)=>{
          this.funcionario = funcionario;
          this.facade
          .getReservas()
          .subscribe(
            {
              next: (reservas:any) => {
                this.reservaciones =  reservas
              }
          })
        } 
      }
    )

  }

}
