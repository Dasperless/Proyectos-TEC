import { Component, OnInit } from '@angular/core';
import { Validators, FormBuilder } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { FacadeService } from 'src/app/services/facade.service';
@Component({
  selector: 'app-registrar-funcionario',
  templateUrl: './registrar-funcionario.component.html',
  styleUrls: ['./registrar-funcionario.component.css']
})
export class RegistrarFuncionarioComponent implements OnInit {
  parqueos: any= [];
  escuelas: any= [];
  id:string = this.route.snapshot.params['id'];
  url:string = this.route.snapshot.url[0].path;
  tipoFuncionario: string[] = ['Docente', 'Administrativo'];
  tipoPerfil: string[] = ['Funcionario','Jefatura', 'Operador', 'Administrativo'];
  selectedEscuela = null;
  selectedTipoFuncionario = undefined;
  selectedTipoPerfil = this.tipoPerfil[0];
  
  registerForm = this.formBuilder.group({
    esAdmin: false,
    nombre: ['', Validators.required],
    identificacion: ['', Validators.required],
    tipoFuncionario: [Validators.required],
    tipoPerfil: [Validators.required],
    escuela: ['', Validators.nullValidator],
    parqueo: ['', Validators.nullValidator],
    telefono: ['', Validators.required],
    discapacidad: [false, Validators.required],
    correo: ['', Validators.required],
    correoAlterno: ['', Validators.required],
    contraseña: ['', Validators.required]
  });

  constructor(
    private facade: FacadeService,
    private formBuilder: FormBuilder,
    private route: ActivatedRoute,
  ) { }

  ngOnInit(): void {
    
    if (this.url === 'editarFuncionario' && this.id !== undefined) {
      this.facade.getFuncionarioById(this.id)
        .subscribe({
          next: (data:any) => {
            this.selectedEscuela = data.escuela;
            this.selectedTipoFuncionario = data.tipoFuncionario;
            this.selectedTipoPerfil = data.tipoPerfil;
            this.registerForm.patchValue(data);            
          },
          error: (err) => {
            console.error(err);
          }
        });
    }
    this.facade
      .getEscuelas()
      .subscribe(
        {
          next: (data:any) => {
            this.escuelas = data;
          }
        }
      );
    this.facade
      .getParqueos()
      .subscribe(
        {
          next: (data:any) => {
            this.parqueos = data;
          }
        }
      );
  }

  // Envia los datos del formulario
  submit(): void {
    if (this.id === undefined){
      this.facade.newFuncionario(this.registerForm.value);
    }
    else {
      let data = this.registerForm.value;
      if(["Administrativo","Operador","Jefatura"].includes(this.selectedTipoPerfil)){
        data.esAdmin = true;
      }
      this.facade.updateFuncionario(this.id, this.registerForm.value);
    }
  }      

  isRegister(): boolean {
    return this.url === 'registrarFuncionario';
  }

}
