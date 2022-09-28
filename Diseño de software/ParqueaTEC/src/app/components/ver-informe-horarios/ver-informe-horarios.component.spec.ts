import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VerInformeHorariosComponent } from './ver-informe-horarios.component';

describe('VerInformeHorariosComponent', () => {
  let component: VerInformeHorariosComponent;
  let fixture: ComponentFixture<VerInformeHorariosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ VerInformeHorariosComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(VerInformeHorariosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
