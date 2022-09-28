const { Schema, model } = require('mongoose');

const reserva = new Schema({
	estado:Boolean,
	parqueo: String,
	idParqueo:String,
	numeroCampo: String,
	tipoCampo: String,
	fecha: String,
	horaEntrada: String,
	horaSalida: String,
	funcionario: String,
	invitado:Object,
	vehiculo:Object
})

module.exports = model('reserva', reserva);