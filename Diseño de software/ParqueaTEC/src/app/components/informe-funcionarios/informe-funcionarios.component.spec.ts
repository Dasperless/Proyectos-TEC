import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InformeFuncionariosComponent } from './informe-funcionarios.component';

describe('InformeFuncionariosComponent', () => {
  let component: InformeFuncionariosComponent;
  let fixture: ComponentFixture<InformeFuncionariosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ InformeFuncionariosComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(InformeFuncionariosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
