const { Schema, model } = require('mongoose');

const funcionarioSchema = new Schema({
	esAdmin: Boolean,
	nombre: String,
	identificacion: Number,
	tipoFuncionario: String,
	tipoPerfil: String,
	escuela: String,
	parqueo: String,
	telefono: Number,
	discapacidad: Boolean,
	correo: String,
	correoAlterno: String,
	contraseña: String,
	placas: Array,
	horario: Array,
	notificaciones: Boolean,
})

module.exports = model('funcionario', funcionarioSchema);
	  