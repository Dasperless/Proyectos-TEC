import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'funcionarioFilter'
})
export class FuncionarioFilterPipe implements PipeTransform {
  /**
   * @param funcionarios - Array de funcionarios
   * @param identificacion - Identificacion del funcionario
   * @returns array de funcionarios filtrados
   */
  transform(funcionarios: any[], identificacion: string): any[] {
    if(!funcionarios) return [];
    if(!identificacion) return funcionarios;
    return funcionarios.filter(funcionario => {
        return funcionario.identificacion.toString(10).includes(identificacion);
    });
  }

}
