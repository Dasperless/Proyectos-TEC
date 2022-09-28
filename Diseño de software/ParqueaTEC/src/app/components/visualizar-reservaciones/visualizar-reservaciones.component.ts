import { Component, OnInit } from '@angular/core';
import { FacadeService } from 'src/app/services/facade.service';

@Component({
  selector: 'app-visualizar-reservaciones',
  templateUrl: './visualizar-reservaciones.component.html',
  styleUrls: ['./visualizar-reservaciones.component.css']
})
export class VisualizarReservacionesComponent implements OnInit {
  idFuncionario :any
  reservas:any = []

  constructor(
    private facade: FacadeService
  ) { }

  ngOnInit(): void {
    this.idFuncionario= localStorage.getItem('token');
    this.facade
    .getFuncionarioById(this.idFuncionario)
    .subscribe(
        {
        next:(data:any)=>{
          this.facade
          .getReservasByIdParqueo(data.parqueo)
          .subscribe(
            {
              next: (res:any)=>{
                this.reservas = res;
              }
            }
        )
         }
       }
     )
  }
  eliminarReserva(id: string) {
      this.facade.eliminarReserva(id).subscribe({next:()=>{
      this.ngOnInit();
    }})

    
  }

}
