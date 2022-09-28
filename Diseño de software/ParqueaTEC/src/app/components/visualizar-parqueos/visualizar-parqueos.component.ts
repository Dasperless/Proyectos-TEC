import { Component, OnInit } from '@angular/core';
import { FacadeService } from 'src/app/services/facade.service';
import { ParqueoService } from '../../services/parqueo.service';

@Component({
  selector: 'app-visualizar-parqueos',
  templateUrl: './visualizar-parqueos.component.html',
  styleUrls: ['./visualizar-parqueos.component.css']
})
export class VisualizarParqueosComponent implements OnInit {
  parqueos:any= [];

  constructor(
    private facade: FacadeService
  ) { }

  ngOnInit(): void {
    this.getParqueos();
  }

  getParqueos(){
    this.facade.getParqueos()
    .subscribe(
      {
        next: (parqueos) => {
          this.parqueos = parqueos;
        },
        error: (err) => {
          console.log(err);
        }
      });
  }

  eliminarParqueo(id:string){
    let success = this.facade.deleteParqueo(id)
    if(success){
      this.getParqueos();
    }
  }

}
