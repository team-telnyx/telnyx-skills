require('dotenv').config();

var express = require('express');
session = require('express-session');
var path = require('path');
var favicon = require('serve-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var flash = require('connect-flash');
var bodyParser = require('body-parser');

var home = require('./routes/home');
var call = require('./routes/call');
var dashboard = require('./routes/dashboard');
var tickets = require('./routes/tickets');
var token = require('./routes/token');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

// uncomment after placing your favicon in /public
//app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(session({
    secret: 'secret',
    name: 'browser-calls',
    cookie: { maxAge: 60000 },
    resave: true,
    saveUninitialized: true
}));
app.use(express.static(path.join(__dirname, 'public')));
app.use(flash());

// middleware for flash message handling
app.use(function(req, res, next){
    res.locals.success = req.flash('success');
    res.locals.errors = req.flash('errors');
    next();
});

app.use('/', home);
app.use('/home', home);
app.use('/call', call);
app.use('/dashboard', dashboard);
app.use('/tickets', tickets);
app.use('/token', token);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  next(err);
});

// error handlers

// development error handler
// will print stacktrace
if (app.get('env') === 'development') {
  app.use(function(err, req, res, next) {
    res.status(err.status || 500);
    res.render('error', {
      message: err.message,
      error: err
    });
  });
}

// production error handler
// no stacktraces leaked to user
app.use(function(err, req, res, next) {
  res.status(err.status || 500);
  res.render('error', {
    message: err.message,
    error: {}
  });
});


module.exports = app;
