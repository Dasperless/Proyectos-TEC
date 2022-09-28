import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EstadisticasHorariosComponent } from './estadisticas-horarios.component';

describe('EstadisticasHorariosComponent', () => {
  let component: EstadisticasHorariosComponent;
  let fixture: ComponentFixture<EstadisticasHorariosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EstadisticasHorariosComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EstadisticasHorariosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
