import { Component, OnInit } from '@angular/core';
import { FacadeService } from 'src/app/services/facade.service';
import { FuncionariosService } from 'src/app/services/funcionarios.service';
@Component({
  selector: 'app-visualizar-funcionarios',
  templateUrl: './visualizar-funcionarios.component.html',
  styleUrls: ['./visualizar-funcionarios.component.css']
})
export class VisualizarFuncionariosComponent implements OnInit {

  funcionarios:any = []

  constructor(
    private facade: FacadeService,
  ) { }


  ngOnInit(): void {
    this.getFuncionarios();
  }
  
  eliminarFuncionario(id: string) {
    let success = this.facade.deleteFuncionario(id);

    if(success){
      this.getFuncionarios();
    }
  }

  getFuncionarios() {
    this.facade.getFuncionarios()
      .subscribe(
        {
          next: (response: any) => {
            this.funcionarios = response;
          },
          error: (err) => {
            console.log(err);
          }
        }
      );
  }


}
