import { TestBed } from '@angular/core/testing';

import { TPService } from './tipo-parqueo.service';

describe('TipoParqueoService', () => {
  let service: TPService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(TPService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
