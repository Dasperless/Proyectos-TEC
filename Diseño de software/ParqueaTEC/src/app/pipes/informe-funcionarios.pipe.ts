import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'informeFuncionarios'
})
export class InformeFuncionariosPipe implements PipeTransform {

  transform(funcionarios: any[], departamento: string): any[] {
    if(!funcionarios) return [];
    if(!departamento) return funcionarios;
    if(departamento === undefined) return funcionarios;
    
    return funcionarios.filter(funcionario => {
      if(funcionario.escuela !== null){
        return funcionario.escuela.includes(departamento);
      }
    });
  }

}
