const express = require('express');
const router = express.Router();
const Ticket = require('../models/ticket');

// POST /tickets/new
router.post('/new', function (req, res) {
  var name = req.body.name;
  var description = req.body.description;
  var phoneNumber = req.body.phone_number;
  var createdAt = new Date();

  if (!description || !phoneNumber || !name) {
    return res.status(400).send('name, description and phoneNumber fields are required.')
  }
  Ticket.create({ name: name, phoneNumber: phoneNumber, description: description, createdAt: createdAt })
    .then(function (savedTicket) {
      req.flash('success', 'Your ticket was submitted! An agent will call you soon.');
      return res.status(201)
        .end();
    })
    .catch(function (err) {
      req.flash('errors', 'Failed to create new ticket');
    })
});

module.exports = router;
