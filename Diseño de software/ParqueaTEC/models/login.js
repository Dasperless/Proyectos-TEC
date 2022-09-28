const { Schema, model } = require('mongoose');

const loginSchema = new Schema({
	  correo: String,
	  contraseña: String	
})

module.exports = model('login', loginSchema);
	  