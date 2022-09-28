import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'historialReservasFilter'
})
export class HistorialReservasFilterPipe implements PipeTransform {

  transform(reservas: any[], nombreFuncionario: string): any[] {
    if(!reservas) return [];
    if(!nombreFuncionario) return reservas;
    if(nombreFuncionario === undefined) return reservas;
    
    return reservas.filter(funcionario => {
      return funcionario.funcionario.includes(nombreFuncionario);
    });
  }

}
