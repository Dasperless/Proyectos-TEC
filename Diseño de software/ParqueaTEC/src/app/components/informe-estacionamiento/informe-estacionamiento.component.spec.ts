import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InformeEstacionamientoComponent } from './informe-estacionamiento.component';

describe('InformeEstacionamientoComponent', () => {
  let component: InformeEstacionamientoComponent;
  let fixture: ComponentFixture<InformeEstacionamientoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ InformeEstacionamientoComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(InformeEstacionamientoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
