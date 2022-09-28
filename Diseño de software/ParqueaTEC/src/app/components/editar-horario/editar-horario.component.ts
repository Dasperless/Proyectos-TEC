import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { FacadeService } from 'src/app/services/facade.service';

@Component({
	selector: 'app-editar-horario',
	templateUrl: './editar-horario.component.html',
	styleUrls: ['./editar-horario.component.css']
})
export class EditarHorarioComponent implements OnInit {
	dias: String[] = ["lunes", "martes", "miercoles", "jueves", "viernes"];
	horas: String[] = ["7:00 am", "8:00 am", "9:00 am", "10:00 am", "11:00 am", "12:00 pm", "1:00 pm", "2:00 pm", "3:00 pm", "4:00 pm", "5:00 pm", "6:00 pm", "7:00 pm", "8:00 pm", "9:00 pm", "10:00 pm"];
	horario: any[] = [];
	horarioTemplate = [
		{ "lunes": [] },
		{ "martes": [] },
		{ "miercoles": [] },
		{ "jueves": [] },
		{ "viernes": [] }
	]
	private idUsuario = localStorage.getItem("token");

	formularioHorario = new FormGroup({
		dia: new FormControl(this.dias[0]),
		horaInicio: new FormControl(''),
		horaFin: new FormControl('')
	});

	constructor(
		private facade: FacadeService
	) { }

	ngOnInit(): void {
		this.getHorario();
	}

	getIdUsuario() {
		return this.idUsuario;
	}

	/**
	 * Convierte la hora a formato 12h
	 * @param time Hora en formato 24h
	 * @returns {string} Hora en formato 12h
	 */
	to12Hour(time: String) {
		let dt = new Date("1970-01-01 " + time)
		var hours = dt.getHours();
		var AmOrPm = hours >= 12 ? 'pm' : 'am';
		hours = (hours % 12) || 12;
		var minutes: any = dt.getMinutes();
		minutes = minutes < 10 && minutes !== 0 ?'0' + minutes  : minutes;
		minutes = minutes == 0 ? minutes + '0' : minutes;
		var finalTime =  hours + ":" + minutes + " " + AmOrPm;
		return finalTime
	}

	// Valida si la franja horaria esta dentro del rango de horas
	validarFranjaHoraria(dia:String, horaInicial: String, horaFinal: String) {
		let horaInicialArr = horaInicial.split(":")
		let horaFinalArr = horaFinal.split(":");

		if(horaInicial === horaFinal){
			alert("La hora inicial y final no pueden ser iguales");
			return false;
		}
		if(horaInicialArr[0] > horaFinalArr[0]){
			alert("La hora final no puede ser mayor a la hora inicial");
			return false;
		}
		return true;
	}

	// Agrega una franja horaria
	agregarFranjaHoraria() {
		let dia = this.formularioHorario.value.dia;
		let horaInicio = this.formularioHorario.value.horaInicio;
		let horaFin = this.formularioHorario.value.horaFin;

		if(this.horario.length === 0){
			this.horario = this.horarioTemplate;
		}

		if(this.validarFranjaHoraria(dia,horaInicio,horaFin)){
			let horaInicion12h = this.to12Hour(this.formularioHorario.value.horaInicio);
			let horaFin12h = this.to12Hour(this.formularioHorario.value.horaFin);
			this.setFranjaHorariaDia(dia, horaInicion12h, horaFin12h);

		}
	}

	// Elimina los divs del horario
	eliminarDivs(id: string): void {
		let elements: any = [];
		do {
			elements = document.getElementsByName(id);
			for (let index = 0; index < elements.length; index++) {
				const element = elements[index];
				element.remove();
			}
		} while (elements.length > 0);

	}

	// Elimina una franja horaria
	eliminarFranjaHoraria(id: string): void {
		// console.log(id);
		let key: any = id.split("-")[0];						// El día
		let dayIndex: any = id.split("-")[1];				// El indice del día
		let scheduleIndex: any = id.split("-")[2];	// El indice del horario

		let array: Array<any> = this.horario[dayIndex][key];	// Obtiene el array de franjas horarias del día
		array.splice(scheduleIndex, 1);												// Elimina el elemento del array
		// console.log("array local",array);
		// console.log("array global",this.horario);
		this.eliminarDivs(id);																// Elimina el div del horario
	}

	// Verifica cuando marcar en el horario
	marcarFranjaHoraria(dia: String, hora: String) {
		if (this.horario.length === 0) {
			return false;
		}
		let diaActual = this.getHorarioPorDia(dia);
		if (diaActual.length === 0) {
			return false;
		}
		for (let index = 0; index < diaActual.length; index++) {
			let franjaHoraria = diaActual[index]
			if (this.compararHoraFranja(hora, franjaHoraria.horaInicio, franjaHoraria.horaFin)) {
				return true;
			}
		}
		return false;
	}

	// Obtiene el detalle de la franja horaria
	getInfoFranjaHoraria(dia: String, hora: String) {
		let diaActual = this.getHorarioPorDia(dia);
		if (diaActual.length === 0) {
			return "";
		}
		for (let index = 0; index < diaActual.length; index++) {
			let franjaHoraria = diaActual[index]
			if (this.compararHoraFranja(hora, franjaHoraria.horaInicio, franjaHoraria.horaFin)) {
				let detalle = "De " + franjaHoraria.horaInicio + " a " + franjaHoraria.horaFin;
				return detalle;
			}
		}
		return "";
	}

	// Obtiene el detalle de la franja horaria
	getIndiceFranjaHoraria(dia: String, hora: String) {
		let diaActual = this.getHorarioPorDia(dia);
		if (diaActual.length === 0) {
			return -1;
		}
		for (let index = 0; index < diaActual.length; index++) {
			let franjaHoraria = diaActual[index]
			if (this.compararHoraFranja(hora, franjaHoraria.horaInicio, franjaHoraria.horaFin)) {
				return index;
			}
		}
		return -1;
	}

	// Compara la hora de inicio y fin con la franja horaria
	compararHoraFranja(hora: String, horaInicio: String, horaFin: String) {
		let horaArray = hora.split(/[\s:]+/);
		let horaInicioArr = horaInicio.split(/[\s:]+/);
		let horaFinArr = horaFin.split(/[\s:]+/);

		if (horaArray[2] !== horaInicioArr[2]) {
			return false
		}
		else if (parseInt(horaArray[0]) >= parseInt(horaInicioArr[0]) && parseInt(horaArray[0]) <= parseInt(horaFinArr[0])) {
			return true;
		}
		return false;
	}

	// Verifica sie el objeto está vacio	
	isEmpty(obj: Object) {
		for (var prop in obj) {
			if (Object.prototype.hasOwnProperty.call(obj, prop)) {
				return false;
			}
		}

		return JSON.stringify(obj) === JSON.stringify({});
	}

	// Establece la franja horaria del día
	setFranjaHorariaDia(dia:any, horaInicio:any, horaFin:any){
		let diaHash:any = {"lunes": 0,"martes": 1,"miercoles":2,"jueves":3,"viernes":4};
		let diaIndex = diaHash[dia];

		if(this.horario[diaIndex][dia].length === 1 && this.isEmpty(this.horario[diaIndex][dia][0])){
			this.horario[diaIndex][dia] = [{horaInicio:horaInicio,horaFin:horaFin}];
		}else{
			this.horario[diaIndex][dia].push({horaInicio:horaInicio,horaFin:horaFin});
		}
	}

	// obtiene el horario por dia
	getHorarioPorDia(dia: String) {
		switch (dia) {
			case "lunes":
				if (this.isEmpty(this.horario[0].lunes[0])) {
					return [];
				}
				return this.horario[0].lunes;
				break;
			case "martes":
				if (this.isEmpty(this.horario[1].martes[0])) {
					return [];
				}
				return this.horario[1].martes;
				break;
			case "miercoles":
				if (this.isEmpty(this.horario[2].miercoles[0])) {
					return [];
				}
				return this.horario[2].miercoles;
				break;
			case "jueves":
				if (this.isEmpty(this.horario[3].jueves[0])) {
					return []
				}
				return this.horario[3].jueves;
				break;
			case "viernes":
				if (this.isEmpty(this.horario[4].viernes[0])) {
					return [];
				}
				return this.horario[4].viernes;
				break;
			default:
				break;
		}
	}

	// Guarda el horario
	getHorario() {
		let idFuncionario: any = "";
		if (localStorage.getItem('token') !== null && localStorage.getItem('token') !== undefined) {
			idFuncionario = localStorage.getItem('token');
			this.facade.getHorario(idFuncionario)
				.subscribe(
					{
						next: (data) => {
							if (data != null || data != undefined) {
								this.horario = data;
							}
						},
						error: (err) => {
							console.error(err);
						}
				});
		}

	}

	saveHorario() {
		this.facade.updateHorario(this.horario,this.idUsuario)
	}
}