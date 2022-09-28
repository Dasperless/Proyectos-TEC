import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SolicitarNotificacionesComponent } from './solicitar-notificaciones.component';

describe('SolicitarNotificacionesComponent', () => {
  let component: SolicitarNotificacionesComponent;
  let fixture: ComponentFixture<SolicitarNotificacionesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SolicitarNotificacionesComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SolicitarNotificacionesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
