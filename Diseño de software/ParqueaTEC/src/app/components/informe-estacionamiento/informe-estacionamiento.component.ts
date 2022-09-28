import { Component, OnInit } from '@angular/core';
import { FacadeService } from 'src/app/services/facade.service';
import { ParqueoService } from 'src/app/services/parqueo.service';
import { TPService } from 'src/app/services/tipo-parqueo.service';

@Component({
  selector: 'app-informe-estacionamiento',
  templateUrl: './informe-estacionamiento.component.html',
  styleUrls: ['./informe-estacionamiento.component.css']
})
export class InformeEstacionamientoComponent implements OnInit {
  parqueos: any = [];

  constructor(
    private facade: FacadeService
  ) {  }

  ngOnInit(): void {
    this.getParqueos();
  }

  getParqueos(){
    this.facade.getParqueos()
      .subscribe(
        {
          next: (parqueos:any) => {
            for (const parqueo of parqueos) {
              this.facade.getTipoParqueoById(parqueo.TipoParqueo).subscribe(
                {
                  next: (tipoParqueo:any) => {
                    parqueo.TipoParqueo = tipoParqueo.nombre;
                  },
                  error: err => console.error(err)
                });
            }
            this.parqueos = parqueos;
            console.log(this.parqueos);
          },
          error: (err) => {
            console.log(err);
          }

        }
    );
  }
}
