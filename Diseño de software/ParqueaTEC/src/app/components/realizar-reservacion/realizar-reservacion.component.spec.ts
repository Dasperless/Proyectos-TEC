import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RealizarReservacionComponent } from './realizar-reservacion.component';

describe('RealizarReservacionComponent', () => {
  let component: RealizarReservacionComponent;
  let fixture: ComponentFixture<RealizarReservacionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RealizarReservacionComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RealizarReservacionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
