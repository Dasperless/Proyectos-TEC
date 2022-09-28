import {Campo} from './Campo';
export class CampoJefatura extends Campo{
	vehiculo: any;
	
	constructor(campoData:any, funcionario:any, parqueo:any) {
		super(campoData,funcionario,parqueo);
	}
	
	buscarDisponibilidad(reservacion:any): any {
		let response:any = {success: false, message: '', stop: false};
		let horario = this.funcionario.horario;
		let diaReservacion = this.getDay(reservacion?.fechaDate);
		
		let idDia = {
			'lunes':0,
			'martes':1,
			'miercoles':2,
			'jueves':3,
			'viernes':4,			
		}
		let indexDia = idDia[diaReservacion as keyof typeof idDia];
		let diahorario = horario[indexDia]
		if(diahorario == undefined){
			response['success']= false;
			response['message']= 'No se ha creado un horario para el funcionario';
			response['stop']= true;
			return response;
		}
		
		if(diahorario[diaReservacion].length === 0){
			response['success']= false;
			response['message']= 'El funcionario no trabaja en ese dia';
			response['stop'] = true;
			return response;
		}
		response['tiquete'] = this.generarTiquete(reservacion);
		response['success']= true;
		response['message']= 'Se ha encontrado un campo disponible';
		return response
	}

	generarTiquete(reservacion:any): any {
		let tiquete = {
			numeroCampo:this.data.numeroCampo,
			tipoCampo: this.data.tipo,
			funcionario: this.funcionario.nombre,
			parqueo: this.parqueo.NombreParqueo,
			direccion: this.parqueo.Ubicacion,
			indicaciones: this.parqueo.FormaAcceder,
			fecha: reservacion.fechaReservacion,
			horaEntrada: '00:00',
			horaSalida: '24:00'
		}
		return tiquete
	}	
}