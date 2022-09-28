import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VisualizarFuncionariosComponent } from './visualizar-funcionarios.component';

describe('VisualizarFuncionariosComponent', () => {
  let component: VisualizarFuncionariosComponent;
  let fixture: ComponentFixture<VisualizarFuncionariosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ VisualizarFuncionariosComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(VisualizarFuncionariosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
