import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'parqueoFilter'
})
export class ParqueoFilterPipe implements PipeTransform {

  transform(parqueos: any[], idParqueo: string): any[] {
    if(!parqueos) return [];
    if(!idParqueo) return parqueos;
    return parqueos.filter(parqueo => {
        return parqueo._id.includes(idParqueo);
    });
  }

}
