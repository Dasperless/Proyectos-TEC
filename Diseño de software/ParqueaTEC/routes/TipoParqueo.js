const express = require('express');
const router = express.Router();
const TipoParqueoSchema = require('../models/TipoParqueo');


// Obtiene los funcionarios
router.get('/TipoParqueo', function(req, res, next) {
	TipoParqueoSchema
		.find()
		.then((data) => res.json(data))
		.catch((err) => res.status(500).json({ message: 'Error al obtener los tipos de Parqueo' }));
});

router.get('/TipoParqueo/:id', function(req, res, next) {
	TipoParqueoSchema
		.findById(req.params.id)
		.then((data) => res.json(data))
		.catch((err) => res.status(500).json({ message: 'Error al obtener el tipo de Parqueo' }));
});



module.exports = router;
