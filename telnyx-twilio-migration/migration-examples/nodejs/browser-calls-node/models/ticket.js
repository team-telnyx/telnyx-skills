var mongoose = require('mongoose');

var Ticket = new mongoose.Schema({
  name:String,
  phoneNumber: String,
  description: String,
  createdAt : Date
});

// Delete model definition in case it is already defined
delete mongoose.models.ticket;

var ticket = mongoose.model('ticket', Ticket);
module.exports = ticket;
