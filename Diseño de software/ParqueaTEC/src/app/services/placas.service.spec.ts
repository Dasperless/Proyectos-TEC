import { TestBed } from '@angular/core/testing';

import { PlacasService } from './placas.service';

describe('PlacasService', () => {
  let service: PlacasService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PlacasService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
