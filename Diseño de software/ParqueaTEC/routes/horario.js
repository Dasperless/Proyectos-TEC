const express = require('express');
const router = express.Router();
const funcionarioSchema = require('../models/funcionario');


// Obtiene el horario del funcionario
router.get('/horario/:id', function (req, res, next) {
	funcionarioSchema.find({ _id: req.params.id }, function (err, funcionario) {
		if (err) {
			res.json({
				success: false,
				message: err
			});
		} else {
			res.json(
				funcionario[0].horario
			);
		}
	});
});

// Registra un horario
router.put('/editarHorario/:id', function (req, res, next) {
	funcionarioSchema
      .findOneAndUpdate(
         {_id: req.params.id,},
         {$set: {horario: req.body}}
	   )
      .then(result => { res.status(201).json({ message: 'Horario registrado' }); })
      .catch(err => { res.status(500).json({ message: 'Error al registrar horario' });});

});

module.exports = router;

