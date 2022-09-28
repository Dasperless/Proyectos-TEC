import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { FacadeService } from 'src/app/services/facade.service';
@Component({
  selector: 'app-informe-funcionarios',
  templateUrl: './informe-funcionarios.component.html',
  styleUrls: ['./informe-funcionarios.component.css']
})
export class InformeFuncionariosComponent implements OnInit {
  funcionarios: any = []; 
  departamentos: any = [];
  idFuncionario:any;
  funcionario:any;

  departamentoForm = this.formBuilder.group({
    departamento: ['']
  });

  constructor(
    private facade: FacadeService,
    private formBuilder: FormBuilder
  ) { }

  ngOnInit(): void {
    this.idFuncionario = localStorage.getItem('token');
    this.getfuncionarios();
    this.getDepartamentos();

    this.facade
    .getFuncionarioById(this.idFuncionario)
    .subscribe(
    {
      next: (data:any) =>{
        this.funcionario = data
        if(this.funcionario.tipoPerfil === "Jefatura"){
          this.facade
          .getEscuelaById(this.funcionario.escuela)
          .subscribe(
            {
              next: (escuela:any) =>{
                this.departamentoForm
                .patchValue(
                  {
                    departamento:escuela.nombre
                  }
                )
              }
            }
          )
        }
      }
    });
  }

  getDepartamentos() {
    this.facade.getEscuelas()
      .subscribe({
        next: (escuelas) => {
          this.departamentos = escuelas;
        },
        error: (err) => {
          console.log(err);
        }
      });
  }

  getfuncionarios() {
    this.facade.getFuncionarios()
      .subscribe
      ({
        next: (funcionarios) => {
          this.funcionarios = funcionarios;
          for(let funcionario of this.funcionarios) {
            this.facade.getEscuelaById(funcionario.escuela)
              .subscribe({
                next: (escuela) => {
                  funcionario.escuela = escuela.nombre;
                }
              });
          }
        },
        error: (err) => {
          console.log(err);
        }
      });
  }

}
