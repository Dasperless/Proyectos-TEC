const express = require('express');
const router = express.Router();

const Funcionario = require('../models/funcionario');

/* GET login listing. */
router.get('/login', function(req, res, next) {
  res.send('Login');
});


router.post('/login', async function(req, res, next) {
	const { correo, contraseña } = req.body;
	const funcionario = await Funcionario.findOne({ correo });
	if (!funcionario) return res.status(401).json({ error: 'Usuario no encontrado' });
	if (funcionario.contraseña !== contraseña) return res.status(401).json({ error: 'Contraseña incorrecta' });
	return res.status(200).json(funcionario);
  });

module.exports = router;
