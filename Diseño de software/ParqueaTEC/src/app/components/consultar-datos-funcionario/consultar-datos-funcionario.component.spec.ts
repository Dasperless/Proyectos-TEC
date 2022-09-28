import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConsultarDatosFuncionarioComponent } from './consultar-datos-funcionario.component';

describe('ConsultarDatosFuncionarioComponent', () => {
  let component: ConsultarDatosFuncionarioComponent;
  let fixture: ComponentFixture<ConsultarDatosFuncionarioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ConsultarDatosFuncionarioComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ConsultarDatosFuncionarioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
