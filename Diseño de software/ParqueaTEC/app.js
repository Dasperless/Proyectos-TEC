var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var cors = require('cors');

// Routes
var loginRouter = require('./routes/login');
var funcionarioRouter = require('./routes/funcionarios');
var escuelasRouter = require('./routes/escuelas');
var placasRouter = require('./routes/placas');
var parqueoRouter = require('./routes/parqueo');
var TPRouter = require('./routes/TipoParqueo');
var horarioRouter = require('./routes/horario');
var reservaRouter = require('./routes/reservacion');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(logger('dev'));
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.json());

app.use('/api', escuelasRouter);
app.use('/api', loginRouter);
app.use('/api', funcionarioRouter);
app.use('/api', placasRouter);
app.use('/api', parqueoRouter);
app.use('/api', TPRouter);
app.use('/api', horarioRouter);
app.use('/api', reservaRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;