const { Schema, model } = require('mongoose');

const parqueoSchema = new Schema({
	TipoParqueo: String,
	NombreParqueo: String	,
      CantidadEspacios: Number,
      EspaciosJefaturas: Number,
      EspaciosOficiales: Number,
      EspaciosDiscapacitados: Number,
      EspaciosVisitantes: Number,
      Ubicacion: String,
      FormaAcceder: String,
      Horario: String,
      Espacios:Array,
})

module.exports = model('parqueos', parqueoSchema);
	  