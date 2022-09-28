import { Component, OnInit } from '@angular/core';
import { FacadeService } from 'src/app/services/facade.service';
@Component({
  selector: 'app-consultar-datos-funcionario',
  templateUrl: './consultar-datos-funcionario.component.html',
  styleUrls: ['./consultar-datos-funcionario.component.css']
})
export class ConsultarDatosFuncionarioComponent implements OnInit {
  funcionarios:any = []
  searchId:string = "";

  constructor(
    private facade: FacadeService
  ) { }

  ngOnInit(): void {
    this.getFuncionarios(); 
  }

  getFuncionarios(){
    this.facade
      .getFuncionarios()
      .subscribe(
        {
          next: (data) => {
            this.funcionarios = data
          },
          error: (err) => {
            console.log(err)
          }
            
      });
  }
}
