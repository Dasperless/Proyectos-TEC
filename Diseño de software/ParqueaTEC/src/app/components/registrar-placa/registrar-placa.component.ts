import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormControl } from '@angular/forms';
import { Validators } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';



import { FormsModule } from '@angular/forms';
import { FacadeService } from 'src/app/services/facade.service';

@Component({
  selector: 'app-registrar-placa',
  templateUrl: './registrar-placa.component.html',
  styleUrls: ['./registrar-placa.component.css']
})
export class RegistrarPlacaComponent implements OnInit {
    id:string = this.route.snapshot.params['id'];
    oldCodigo:string =this.route.snapshot.params['codigoPlaca'];
    Codigo: string="";
    placas:any= [];

  constructor( 
    private facade: FacadeService, 
    private route: ActivatedRoute
  ) { }

  ngOnInit(): void {
    if(this.oldCodigo!=="" || this.oldCodigo!== null){
      this.Codigo = this.oldCodigo;
    }
  }
 
  submit(idUsuario: string, placaAntigua: string, placaActualizada: any): void {
    if(this.oldCodigo == ""  || this.oldCodigo==null){
      this.facade.newPlaca(idUsuario, placaAntigua)
    }else{
      this.facade.updatePlaca(idUsuario, placaAntigua, placaActualizada)
    }
  } 

  getPlacas(id:string){
    this.facade.getPlacas(id)
      .subscribe(
        {
          next: (response: any) => {
            this.placas = response;
            console.log(this.placas);
          },
          error: (err) => {
            console.log(err);
          }
        }
      );
  }
  
}
