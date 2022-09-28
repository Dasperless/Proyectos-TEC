import { Component, OnInit } from '@angular/core';
import { FacadeService } from 'src/app/services/facade.service';

@Component({
	selector: 'app-registrar-horario',
	templateUrl: './registrar-horario.component.html',
	styleUrls: ['./registrar-horario.component.css']
})
export class RegistrarHorarioComponent implements OnInit {
	dias:String[] = ["lunes","martes","miercoles","jueves","viernes"];
	horas:String[] = ["7:00 am","8:00 am","9:00 am","10:00 am","11:00 am","12:00 pm","1:00 pm","2:00 pm","3:00 pm","4:00 pm","5:00 pm","6:00 pm","7:00 pm","8:00 pm","9:00 pm","10:00 pm"];	
	horario:any[] = [];
	private idUsuario = localStorage.getItem("token");

	constructor(
		private facade:FacadeService
	) { }

	ngOnInit(): void {
		this.getHorario();
	}

	getIdUsuario(){
		return this.idUsuario;
	}

	// Verifica cuando marcar en el horario
	marcarFranjaHoraria(dia:String, hora:String){
		if(this.horario.length === 0){
			return false;
		}
		let diaActual = this.getHorarioPorDia(dia);
		if(diaActual.length === 0){
			return false;
		}
		for (let index = 0; index < diaActual.length; index++) {
			let franjaHoraria = diaActual[index]
			if(this.compararHoraFranja(hora, franjaHoraria.horaInicio, franjaHoraria.horaFin)){
				return true;
			}
		}
		return false;
	}

	// Obtiene el detalle de la franja horaria
	getInfoFranjaHoraria(dia:String, hora:String){
		let diaActual = this.getHorarioPorDia(dia);
		if(diaActual.length === 0){
			return "";
		}
		for (let index = 0; index < diaActual.length; index++) {
			let franjaHoraria = diaActual[index]
			if(this.compararHoraFranja(hora, franjaHoraria.horaInicio, franjaHoraria.horaFin)){
				let detalle = "De "+franjaHoraria.horaInicio + " a " + franjaHoraria.horaFin;
				return detalle;
			}
		}
		return "";
	}

	// Obtiene el detalle de la franja horaria
	getIndiceFranjaHoraria(dia:String, hora:String){
		let diaActual = this.getHorarioPorDia(dia);
		if(diaActual.length === 0){
			return -1;
		}
		for (let index = 0; index < diaActual.length; index++) {
			// console.log("tamaño array: ", index);
			let franjaHoraria = diaActual[index]
			if(this.compararHoraFranja(hora, franjaHoraria.horaInicio, franjaHoraria.horaFin)){
				return index;
			}
		}
		return -1;
	}

	// Compara la hora de inicio y fin con la franja horaria
	compararHoraFranja(hora:String, horaInicio:String, horaFin:String){
		let horaArray = hora.split(/[\s:]+/);
		let horaInicioArr = horaInicio.split(/[\s:]+/);
		let horaFinArr = horaFin.split(/[\s:]+/);

		if(horaArray[2] !== horaInicioArr[2]){
			return false
		}
		else if(parseInt(horaArray[0]) >= parseInt(horaInicioArr[0]) && parseInt(horaArray[0]) <=  parseInt(horaFinArr[0])){
			return true;
		}
		return false;
	}
	
	// Verifica sie el objeto está vacio	
	isEmpty(obj:Object) {
		for(var prop in obj) {
			if(Object.prototype.hasOwnProperty.call(obj, prop)) {
				return false;
			}
		}
	
		return JSON.stringify(obj) === JSON.stringify({});
	}

	// obtiene el horario por dia
	getHorarioPorDia(dia:String){
		switch (dia) {
			case "lunes":
				if(this.isEmpty(this.horario[0].lunes[0])){
					return [];
				}
				return this.horario[0].lunes;
				break;
			case "martes":
				if(this.isEmpty(this.horario[1].martes[0])){
					return [];
				}
				return this.horario[1].martes;
				break;
			case "miercoles":
				if(this.isEmpty(this.horario[2].miercoles[0])){
					return [];
				}
				return this.horario[2].miercoles;
				break;
			case "jueves":
				if(this.isEmpty(this.horario[3].jueves[0])){
					return []
				}
				return this.horario[3].jueves;
				break;
			case "viernes":
				if(this.isEmpty(this.horario[4].viernes[0])){
					return [];
				}
				return this.horario[4].viernes;
				break;
			default:
				break;
		}
	}

	// Guarda el horario
	getHorario(){
		let idFuncionario:any = "";
		if(localStorage.getItem('token') !== null && localStorage.getItem('token') !== undefined) {
			idFuncionario = localStorage.getItem('token');
			this.facade.getHorario(idFuncionario)
			.subscribe(
				{
					next: (data) => {
						if(data != null || data != undefined){
							this.horario = data;
							console.log(this.horario);
						}
					},
					error: (err) => {
						console.log(err);
					}
				});
		}

	}

}
