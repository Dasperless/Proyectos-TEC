import {Campo} from './Campo';
export class CampoDiscapacitado extends Campo{
	vehiculo: any;
	constructor(campoData:any,funcionario:any,parqueo:any) {
		super(campoData,funcionario,parqueo);
	}
	
	buscarDisponibilidad(reservacion:any): any {
		if(this.funcionario.tipoPerfil === "Funcionario"){
			return this.buscarDisponibilidadFuncionario(reservacion)
		}else{
			return this.buscarDisponibilidadJefatura(reservacion)
		}
	}
	
	buscarDisponibilidadFuncionario(reservacion:any){
		let response:any = {success: false, message: '', stop: false}; 		//Respuesta de la disponibilidad

		let horario = this.funcionario.horario; 							//Horario funcionario
		let diaReservacion:string = this.getDay(reservacion?.fechaDate); 	//Dia de la reservacion 
		
		let idDia = {'lunes':0,'martes':1,'miercoles':2,'jueves':3,'viernes':4}

		let indexDia:number = idDia[diaReservacion as keyof typeof idDia];

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
			response['stop']= true;
			return response;
		}

		// Verificar la hora
		let boolList:boolean[] =[]
		diahorario[diaReservacion].forEach((franja:any) => {
			let franjaCoincide = this.compararFranjaHoraria(franja, reservacion.horaEntrada, reservacion.horaSalida);
			boolList.push(franjaCoincide);
		});

		if(!boolList.includes(true)){
			response['success']= false;
			response['message']= "El horario no coincide"
			response['stop']= true;
			return response;
		}

		response['success'] = true;
		response['tiquete'] = this.generarTiquete(reservacion);
		response['message'] = 'Se ha encontrado un espacio disponible';
		return response
	}

	buscarDisponibilidadJefatura(reservacion:any){

	}
	
	generarTiquete(reservacion:any) {
		let tiquete;
		if(this.funcionario.tipoPerfil === "Funcionario"){
			tiquete = {
				numeroCampo:this.data.numeroCampo,
				tipoCampo: this.data.tipo,
				funcionario: this.funcionario.nombre,
				parqueo: this.parqueo.NombreParqueo,
				direccion: this.parqueo.Ubicacion,
				indicaciones: this.parqueo.FormaAcceder,
				fecha: reservacion.fechaReservacion,
				horaEntrada: reservacion.horaEntrada,
				horaSalida: reservacion.horaSalida
			}
		}else{
			tiquete = {
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
		}
		return tiquete
	}


	compararFranjaHoraria(franja:any,horaEntrada:any,horaSalida:any){
		franja['horaInicio'] = this.to24Hour(franja['horaInicio'])
		franja['horaFin'] = this.to24Hour(franja['horaFin'])

		if(this.compareHour(horaEntrada,franja.horaInicio) && this.compareHour(franja.horaFin,horaSalida)){
			return true;
		}
		return false;
	}

	compareHour(pHora1:string,pHora2:string){
		let hora1Arr = pHora1.split(/[:]+/)
		let hora2Arr = pHora2.split(/[:]+/)
		let hora1:number = parseInt(hora1Arr[0])
		let hora2:number = parseInt(hora2Arr[0])
		let minutos1:number = parseInt(hora1Arr[1])
		let minutos2:number = parseInt(hora2Arr[1])
		if(hora1 > hora2){
			return true;
		}else if(hora1 == hora2 && minutos1 >= minutos2){
			return true
		}
		return false;
	}
	
	to24Hour(hora: string){
		let horaSplit = hora.split(/[\s:]+/)
		let h:number = parseInt(horaSplit[0]);
		if(horaSplit[2] ==="pm"){
			h = parseInt(horaSplit[0]) + 12
		}
		return h+":"+horaSplit[1]
	}

	
}