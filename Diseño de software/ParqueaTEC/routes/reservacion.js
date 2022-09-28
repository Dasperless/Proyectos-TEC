
const express = require('express');
const router = express.Router();
const reserva = require('../models/reservacion');

// Obtiene las reserva
router.get('/reserva', function(req, res, next) {
 return reserva.find({}, function(err, reservas) {
	if (err) {
	  res.json({
		success: false,
		message: err
	  });
	} else {
	  res.json(reservas);
	  
	}
	});
});

// Obtiene las reservas por id del parqueo
router.get('/reservas/:idParqueo', function(req, res, next) {
	reserva.find({idParqueo:req.params.idParqueo}, function(err, reservas) {
	   if (err) {
		 res.json({
		   success: false,
		   message: err
		 });
	   } else {
		 res.json(reservas);
	   }
	   });
   });
   

// Obtiene un reserva
router.get("/reserva/:id", function (req, res, next) {
  reserva.find({ _id: req.params.id }, function (err, reservas) {
	if (err) {
	  res.json({
		success: false,
		message: err,
	  });
	} else {
	  res.json(reservas[0]);
	}
  });
});



// Registra un reserva
router.post('/reservar/:idFuncionario/:idParqueo', function(req, res, next) {
	const reserva1 = reserva(req.body);

	//Lo guarda en la base de datos
	reserva1
		.save()
		.then(result => { res.status(201).json({ message: 'Reserva registrado' }); })
		.catch(err => { res.status(500).json({ message: 'Error al registrar la reserva' }); });
});

// Edita un reserva
router.put('/editarReserva/:idReserva', function(req, res, next) {
	reserva.findByIdAndUpdate(req.params.id, req.body, function(err, reserva) {
		if (err) {
			res.status(500).json({ message: 'Error al editar la reserva' });
		} else {
			res.status(200).json({ message: 'Reserva editada' });
		}
	});
});

// Elimina un reserva
router.delete('/eliminarReserva/:idReserva', function(req, res, next) {
	reserva.findByIdAndDelete(req.params.idReserva)
		.then(result => { res.status(200).json({ message: 'Reserva eliminada' }); })
		.catch(err => { res.status(500).json({ message: 'Error al eliminar la reserva' }); });
});


module.exports = router;
