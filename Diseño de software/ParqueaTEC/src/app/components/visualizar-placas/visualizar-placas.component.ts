import { Component, OnInit } from '@angular/core';
import { identity } from 'rxjs';
import { PlacasService } from '../../services/placas.service';
import { Router, ActivatedRoute } from '@angular/router';
import { FacadeService } from 'src/app/services/facade.service';

@Component({
  selector: 'app-visualizar-placas',
  templateUrl: './visualizar-placas.component.html',
  styleUrls: ['./visualizar-placas.component.css']
})
export class VisualizarPlacasComponent implements OnInit {
  placas:any= [];
  id:string = this.route.snapshot.params['id'];

  constructor(
    private facade: FacadeService,
    private route: ActivatedRoute,
  ) { }

  ngOnInit(): void {
    this.getPlacas(this.id);
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

  eliminarPlaca(id:string, idPlaca: string){
    let success = this.facade.deletePlaca(id, idPlaca)
    if(success){
      this.getPlacas(this.id);
    }
  }

}
