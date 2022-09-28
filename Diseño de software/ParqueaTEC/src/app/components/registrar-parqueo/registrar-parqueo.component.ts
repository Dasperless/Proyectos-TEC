
import { Component, OnInit } from '@angular/core';
import { Validators } from '@angular/forms';
import { FormBuilder } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { FacadeService } from 'src/app/services/facade.service';

@Component({
  selector: 'app-registrar-parqueo',
  templateUrl: './registrar-parqueo.component.html',
  styleUrls: ['./registrar-parqueo.component.css']
})
export class RegistrarParqueoComponent implements OnInit {
  registerForm = this.formBuilder.group({
    NombreParqueo: ['', Validators.required],
    TipoParqueo: ['', Validators.required],
    CantidadEspacios: ['', Validators.required],
    EspaciosJefaturas: ['', Validators.required],
    EspaciosOficiales: ['', Validators.required],
    EspaciosDiscapacitados: ['', Validators.required],
    EspaciosVisitantes: ['', Validators.required],
    Ubicacion: ['', Validators.required],
    FormaAcceder: ['', Validators.required],
    Horario: ['', Validators.required],
  });

  id: string = this.route.snapshot.params['id'];
  url: string = this.route.snapshot.url[0].path;
  TipoParqueos: any = [];

  constructor(
    private facade: FacadeService,
    private formBuilder: FormBuilder,
    private route: ActivatedRoute,) { }

  ngOnInit(): void {
    // Cambia los espacios en caso de que se esté editando un parqueo
    if (this.url === 'editarParqueo' && this.id !== undefined) {
      this.facade.getParqueoById(this.id)
        .subscribe(
          {
            next: (parqueo: any) => {
              this.registerForm.patchValue(parqueo);
            },
            error:(error:any)=>{
              console.error(error);
            }
          });
    }
    
    // Obtiene el tipo de parqueo
    this.facade.getTipoParqueo()
      .subscribe(
        {
          next: (response: any) => { 
            this.TipoParqueos = response; 
          }
        }
      )
  }

  /**
   * Registra o actualiza un parqueo
   */
  submit(): void {
    let data = this.registerForm.value;
    let espacios = this.generarEspacios(data);
    data['Espacios'] = espacios;
    if (this.id === undefined) {
      this.facade.newParqueo(this.registerForm.value);
    }
    else {
      this.facade.updateParqueo(this.id, this.registerForm.value);
    }
  }
  
  /**
   * Verifica si actualmente se está registrando o actualizando
   * @returns {boolean} true si se esta registrando un parqueo false si se está actualizando 
   */
  isRegister(): boolean {
    return this.url === 'registrarParqueo';
  }

  /**
   * 
   * @param parqueo Datos del parqueo
   */
  generarEspacios(parqueo:any): any[] {
    let espaciosArr:any = [];

    let CantidadEspaciosParqueo = [ 
      "CantidadEspacios", 
      "EspaciosJefaturas", 
      "EspaciosOficiales", 
      "EspaciosDiscapacitados", 
      "EspaciosVisitantes" ];

    let tipo = {
      "CantidadEspacios": 'Estandar',
      "EspaciosJefaturas": 'Jefatura',
      "EspaciosOficiales": 'Oficial',
      "EspaciosDiscapacitados": 'Discapacitado',
      "EspaciosVisitantes": 'Visitante'
    
    }

    let tipoKey;
    let espacios:any = [];
    for (let cantidad of CantidadEspaciosParqueo) {
      if (parqueo[cantidad] > 0) {
        tipoKey = cantidad as keyof typeof tipo;
        espacios = this.newEspacios(tipo[tipoKey], parqueo[cantidad]);
        espaciosArr = espaciosArr.concat(espacios);
      }
    }
    return espaciosArr
  }

  /**
   * Crea un arreglo de objetos con los espacios segun el tipo de espacio
   * @param tipo Tipo de espacio
   * @param cantidad Cantidad de espacios
   * @returns {any[]} Espacios
   */
  newEspacios(tipo:string,cantidad:number): any[] {
    let espacios=[];
    let prefijo = {
      'Estandar':'F',
      'Oficial':'O',
      'Discapacitado':'D',
      'Visitante':'V',
      'Jefatura':'J'
    };
    for (let i = 0; i < cantidad; i++) {
      let espacio ={
        numeroCampo: prefijo[tipo as keyof typeof prefijo]+i.toString(),
        tipo: tipo
      }
      espacios.push(espacio);
    }   
    return espacios 
  }


}
