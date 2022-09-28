export abstract class Campo {
	funcionario: any;
	parqueo:any;
	data:any;

	constructor(campoData:any,funcionario:any,parqueo:any) {
		this.setParqueo(parqueo);
		this.setData(campoData);
		this.setFuncionario(funcionario);
	}


	solicitarReservacion(reservacion:any):any {
		reservacion['fechaDate'] = this.stringToDate(reservacion.fechaReservacion);
		return this.buscarDisponibilidad(reservacion)
	}

	stringToDate(fecha:any):Date {
		return new Date(fecha.replaceAll("-","/"));
	}

	getDay(fecha:Date) {
		return fecha.toLocaleDateString('es-MX', { weekday: 'long' }).normalize('NFD').replace(/([aeio])\u0301|(u)[\u0301\u0308]/gi,"$1$2");
	}

	abstract buscarDisponibilidad(reservacion:any):any;

	abstract generarTiquete(reservacion:any):any

	setFuncionario(funcionario:any){
		this.funcionario = funcionario;
	}

	setParqueo(parqueo:any){
		this.parqueo = parqueo;
	}

	setData(data:any){
		this.data = data;
	}

}