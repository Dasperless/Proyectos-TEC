import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VisualizarParqueoComponent } from './visualizar-parqueo.component';

describe('VisualizarParqueoComponent', () => {
  let component: VisualizarParqueoComponent;
  let fixture: ComponentFixture<VisualizarParqueoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ VisualizarParqueoComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(VisualizarParqueoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
