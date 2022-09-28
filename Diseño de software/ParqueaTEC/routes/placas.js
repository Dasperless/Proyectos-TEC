const { SSL_OP_NO_SESSION_RESUMPTION_ON_RENEGOTIATION } = require('constants');
const express = require('express');
const router = express.Router();
const funcionarioSchema = require('../models/funcionario');

// Obtiene las placas del funcionario
router.get('/placas/:id', function (req, res, next) {
	funcionarioSchema.find({ _id: req.params.id }, function (err, funcionario) {
		if (err) {
			res.json({
				success: false,
				message: err
			});
		} else {
			res.json(
				funcionario[0].placas
			);
		}
	});
});

// Registra una nueva placa
router.post('/registrarplaca/:id', function (req, res, next) {
	funcionarioSchema
      .findOneAndUpdate(
         {_id: req.params.id,},
         {$push: {placas: req.body}}
	   )
      .then(result => { res.status(201).json({ message: 'Placa registrada' }); })
      .catch(err => { res.status(500).json({ message: 'Error al registrar placa' });});

});

// Elimina una placa
router.delete('/eliminarPlaca/:idF/:idP', function(req, res, next) {
		funcionarioSchema
         .findOneAndUpdate(
            {_id: req.params.idF,},
            {$pull:{"placas":{"codigo": req.params.idP} }} 
		)
		.then(result => { res.status(201).json({ message: 'Placa eliminada' }); })
	   .catch(err => { res.status(500).json({ message: 'Error al registrar placa'}); });

});



router.put('/editarPlaca/:idF/:codigoP', function(req, res, next) {
	funcionarioSchema.updateOne(
	{ _id: req.params.idF, "placas.codigo": req.params.codigoP },
	{ $set:   {"placas.$.codigo" : req.body.codigo } }
 ).then(result => { res.status(201).json({ message: 'Placa editada' }); })
 .catch(err => { res.status(500).json({ message: 'Error al editar placa'}); });

	});
module.exports = router;
