import { Component, OnInit } from '@angular/core';
@Component({
  selector: 'app-funcionario',
  templateUrl: './funcionario.component.html',
  styleUrls: ['./funcionario.component.css']
})
export class FuncionarioComponent implements OnInit {
  id: any = ""
  constructor( ) { }

  ngOnInit(): void {
      this.id = localStorage.getItem('token');

  }

}
