const { Schema, model } = require('mongoose');

const escuelaSchema = new Schema({
	codigo: String,
	nombre: String,
})

module.exports = model('escuela', escuelaSchema);
	  