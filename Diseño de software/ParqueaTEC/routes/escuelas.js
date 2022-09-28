const express = require('express');
const router = express.Router();
const escuelaSchema = require('../models/escuela');


// Obtiene los funcionarios
router.get('/escuelas', function(req, res, next) {
	escuelaSchema
		.find()
		.then((data) => res.json(data))
		.catch((err) => res.status(500).json({ message: 'Error al obtener las escuelas' }));
});

// Obtiene una escuela por su id
router.get('/escuela/:id', function(req, res, next) {
	escuelaSchema
		.findById(req.params.id)
		.then((data) => res.json(data))
		.catch((err) => res.status(500).json({ message: 'Error al obtener la escuela' }));
});


module.exports = router;
