import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VisualizarPlacasComponent } from './visualizar-placas.component';

describe('VisualizarPlacasComponent', () => {
  let component: VisualizarPlacasComponent;
  let fixture: ComponentFixture<VisualizarPlacasComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ VisualizarPlacasComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(VisualizarPlacasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
