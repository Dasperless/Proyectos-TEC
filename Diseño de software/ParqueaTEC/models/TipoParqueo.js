const { Schema, model } = require('mongoose');

const TipoParqueoSchema = new Schema({
	codigo: String,
	nombre: String,
})

module.exports = model('tipoParqueo', TipoParqueoSchema);
	  