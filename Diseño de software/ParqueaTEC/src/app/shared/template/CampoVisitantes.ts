import {Campo} from './Campo';
export class CampoVisitantes extends Campo {
	visitante: any;
	
	constructor(campoData:any, funcionario:any,parqueo:any) {
		super(campoData, funcionario,parqueo);
	}

	buscarDisponibilidad(reservacion:any): any {
		let response= {
			success:true,
			message: 'Se ha encontrado un campo',
			tiquete: this.generarTiquete(reservacion),
			stop:false
		}
		return response;
	}
	
	setVisitante(visitantes:any) {
		this.visitante = visitantes;
	}
	
	/**
	 * Genera un json con la información del tiquete
	 * @param reservacion Datos de la reservacion
	 * @returns 
	 */
	generarTiquete(reservacion:any) {
		let tiquete = {
			numeroCampo:this.data.numeroCampo,
			tipoCampo: this.data.tipo,
			funcionario: this.funcionario.nombre,
			parqueo: this.parqueo.NombreParqueo,
			direccion: this.parqueo.Ubicacion,
			indicaciones: this.parqueo.FormaAcceder,
			invitado: this.visitante,
			fecha: reservacion.fechaReservacion,
			horaEntrada: '00:00',
			horaSalida: '24:00'
		}
		return tiquete;
    }
}
	