const { SSL_OP_NO_SESSION_RESUMPTION_ON_RENEGOTIATION } = require('constants');
const express = require('express');
const router = express.Router();
const parqueoSchema = require('../models/parqueo');

router.get('/parqueos', function(req, res, next) {
    parqueoSchema.find({}, function(err, parqueos) {
        if (err) {
          res.json({
            success: false,
            message: err
          });
        } else {
          res.json(parqueos);
        }
        });
  });


router.post('/registrarParqueo', function(req, res, next) {
const parqueo = parqueoSchema(req.body);

//Lo guarda en la base de datos
parqueo
    .save()
    .then(result => { res.status(201).json({ message: 'Parqueo registrado' }); })
    .catch(err => { res.status(500).json({ message: 'Error al registrar el Parqueo' }); });
});


//editar
router.put('/editarParqueo/:id', function(req, res, next) {
	parqueoSchema.findByIdAndUpdate(req.params.id, req.body, function(err, parqueo) {
		if (err) {
			res.status(500).json({ message: 'Error al editar el parqueo' });
		} else {
			res.status(200).json({ message: 'parqueo editado' });
		}
	});
});


// Elimina 
router.delete('/eliminarParqueo/:id', function(req, res, next) {
	parqueoSchema.findByIdAndDelete(req.params.id)
		.then(result => { res.status(200).json({ message: 'parqueo eliminado' }); })
		.catch(err => { res.status(500).json({ message: 'Error al eliminar el parqueo' }); });
});


// Obtiene un Parqueo
router.get("/parqueos/:id", function (req, res, next) {
  parqueoSchema.find({ _id: req.params.id }, function (err, parqueos) {
	if (err) {
	  res.json({
		success: false,
		message: err,
	  });
	} else {
	  res.json(parqueos[0]);
	}
  });
});



module.exports = router;