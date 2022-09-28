import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RegistrarPlacaComponent } from './registrar-placa.component';

describe('RegistrarPlacaComponent', () => {
  let component: RegistrarPlacaComponent;
  let fixture: ComponentFixture<RegistrarPlacaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RegistrarPlacaComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RegistrarPlacaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
