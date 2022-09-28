const { Schema, model } = require('mongoose');

const placaSchema = new Schema({
	codigo: String,
})

module.exports = model('placa', placaSchema);