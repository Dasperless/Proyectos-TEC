import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { FacadeService } from 'src/app/services/facade.service';

@Component({
  selector: 'app-perfil-funcionario',
  templateUrl: './perfil-funcionario.component.html',
  styleUrls: ['./perfil-funcionario.component.css']
})
export class PerfilFuncionarioComponent implements OnInit {

  funcionario:any = {};
  headers = {
    esAdmin: 'Administrador',
    nombre: 'Nombre',
    identificacion: 'Identificación',
    tipoFuncionario: 'Tipo Funciónario',
    tipoPerfil: 'Tipo Perfil',
    escuela: 'Escuela',
    parqueo: 'Parqueo',
    telefono: 'Teléfono',
    discapacidad: 'Discapacidad',
    correo: 'Correo',
    correoAlterno: 'Correo Alterno',
  }
  
  id:string = this.route.snapshot.params['id'];

  constructor(
    private facadeService: FacadeService,
    private route: ActivatedRoute,
  ) { }

  ngOnInit(): void {
    this.facadeService
    .getFuncionarioById(this.id)
    .subscribe(
      {
        next: (funcionario: any) => {
          for (let key in funcionario) {
            if(Object.keys(this.headers).includes(key)) {
              this.funcionario[key] = funcionario[key]; 
            }
          }
        }
      });
  }

  getKeys(obj:any):string[] {
    return Object.keys(obj);
  }

  getHeader(key:any):string {
    return this.headers[key as keyof typeof this.headers];
  }
  
//   getEscuela(id:string){
//     if(id !== undefined){
//     this.escuelasService.getEscuela(id)
//       .subscribe(
//         {
//           next: (response: any) => {
//               this.funcionario.escuela =  response.codigo + " - " + response.nombre;
//             },
//           error: (error: any) => {console.log(error);}
//         });
//   } 
// }
}
