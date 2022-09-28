import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VisualizarParqueosComponent } from './visualizar-parqueos.component';

describe('VisualizarParqueosComponent', () => {
  let component: VisualizarParqueosComponent;
  let fixture: ComponentFixture<VisualizarParqueosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ VisualizarParqueosComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(VisualizarParqueosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
