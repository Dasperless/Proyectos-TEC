import { Component, OnInit } from '@angular/core';
import { FacadeService } from 'src/app/services/facade.service';
import { FuncionariosService } from 'src/app/services/funcionarios.service';
import { HorarioService } from 'src/app/services/horario.service';
@Component({
  selector: 'app-estadisticas-horarios',
  templateUrl: './estadisticas-horarios.component.html',
  styleUrls: ['./estadisticas-horarios.component.css']
})
export class EstadisticasHorariosComponent implements OnInit {
  funcionarios: any[] = []
  estadisticas: any[] = [];
  dias: any[] = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']
  indexDia:any ={'lunes': 0, 'martes': 1, 'miercoles': 2, 'jueves': 3, 'viernes': 4}
  franjasHorarias:any = {'lunes':[], 'martes':[], 'miercoles':[], 'jueves':[], 'viernes':[]};


  constructor(
    private facade: FacadeService,
  ) { }

  ngOnInit(): void {
    this.getFuncionarios();
  }

  existeFranaja(franjasVerif:any, dia:any){
    let franja = this.franjasHorarias[dia]
    if(franja.length === 0){
      return false;
    }
    if(franja === undefined){
      return false;
    }
    if(franjasVerif.horaInicio == franja.horaInicio && franjasVerif.horaFin == franja.horaFin){
      return true
    }
    return false
  }

  generarEstadistica(){
    for (const funcionario of this.funcionarios) {
      if(funcionario['horario'].length > 0){
        for (const dia of this.dias) {
            let franja = funcionario['horario'][this.indexDia[dia]];
            if(!this.existeFranaja(franja, dia) ){
              if(franja[dia].length > 0){
                this.franjasHorarias[dia].push({...franja[dia],'frecuencia':1});
              }
            }else{
              this.franjasHorarias[this.indexDia[dia]][dia]['frecuencia'] += 1;
            }
        }
      }
    }
    console.debug(this.franjasHorarias);
  }

  getFuncionarios(){
    this.facade.getFuncionarios()
      .subscribe(
        {
          next: (data) => {
            this.funcionarios = data;
            this.generarEstadistica();
          },
          error: (err) => {
            console.log(err);
          }
        }
        
    );
  }


  

}
