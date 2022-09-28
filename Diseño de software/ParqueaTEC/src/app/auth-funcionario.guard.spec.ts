import { TestBed } from '@angular/core/testing';

import { AuthFuncionarioGuard } from './auth-funcionario.guard';

describe('AuthFuncionarioGuard', () => {
  let guard: AuthFuncionarioGuard;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    guard = TestBed.inject(AuthFuncionarioGuard);
  });

  it('should be created', () => {
    expect(guard).toBeTruthy();
  });
});
