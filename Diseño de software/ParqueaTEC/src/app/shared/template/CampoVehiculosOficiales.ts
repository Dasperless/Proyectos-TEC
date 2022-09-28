import {Campo} from './Campo';
export class CampoVehiculosOficiales extends Campo{
	vehiculo: any;
	constructor(campoData:any,funcionario:any,parqueo:any) {
		super(campoData,funcionario,parqueo);
	}
	buscarDisponibilidad(reservacion:any): any {
		let response = {
			success:true, 
			stop:false,
			message:"Se ha encontrado un espacio disponible",
			tiquete:this.generarTiquete(reservacion)
		}
		return response;
	}
	
	setVehiculo(vehiculo:any){
		this.vehiculo=vehiculo;
	}
	
	generarTiquete(reservacion:any): any {
		let tiquete = {
			numeroCampo:this.data.numeroCampo,
			tipoCampo: this.data.tipo,
			funcionario: this.funcionario.nombre,
			parqueo: this.parqueo.NombreParqueo,
			direccion: this.parqueo.Ubicacion,
			indicaciones: this.parqueo.FormaAcceder,
			vehiculo:this.vehiculo
		}
		return tiquete
	}
}