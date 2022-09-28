const { SSL_OP_NO_SESSION_RESUMPTION_ON_RENEGOTIATION } = require('constants');
const express = require('express');
const router = express.Router();
const funcionarioSchema = require('../models/funcionario');

// Obtiene los funcionarios
router.get('/funcionarios', function(req, res, next) {
  funcionarioSchema.find({}, function(err, funcionarios) {
	if (err) {
	  res.json({
		success: false,
		message: err
	  });
	} else {
	  res.json(funcionarios);
	}
	});
});

// Obtiene un funcionario
router.get("/funcionarios/:id", function (req, res, next) {
  funcionarioSchema.find({ _id: req.params.id }, function (err, funcionarios) {
	if (err) {
	  res.json({
		success: false,
		message: err,
	  });
	} else {
	  res.json(funcionarios[0]);
	}
  });
});

// Registra un usuario
router.post('/registrarFuncionario', function(req, res, next) {
	const funcionario = funcionarioSchema(req.body);

	//Lo guarda en la base de datos
	funcionario
		.save()
		.then(result => { res.status(201).json({ message: 'Funcionario registrado' }); })
		.catch(err => { res.status(500).json({ message: 'Error al registrar el funcionario' }); });
});

// Edita un funcionario
router.put('/editarFuncionario/:id', function(req, res, next) {
	funcionarioSchema.findByIdAndUpdate(req.params.id, req.body, function(err, funcionario) {
		if (err) {
			res.status(500).json({ message: 'Error al editar el funcionario' });
		} else {
			res.status(200).json({ message: 'Funcionario editado' });
		}
	});
});

// Elimina un funcionario
router.delete('/eliminarFuncionario/:id', function(req, res, next) {
	funcionarioSchema.findByIdAndDelete(req.params.id)
		.then(result => { res.status(200).json({ message: 'Funcionario eliminado' }); })
		.catch(err => { res.status(500).json({ message: 'Error al eliminar el funcionario' }); });
});
module.exports = router;
