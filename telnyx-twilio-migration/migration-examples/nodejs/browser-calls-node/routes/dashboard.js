const express = require('express');
const router = express.Router();
const Ticket = require('../models/ticket');


// GET /dahsboard
router.get('/', function (req, res) {
  Ticket.find()
    .then(function (tickets) {
      res.render('dashboard/index', { tickets: tickets });
    });
});

module.exports = router;
