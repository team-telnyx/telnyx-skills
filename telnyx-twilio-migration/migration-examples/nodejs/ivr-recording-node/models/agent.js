'use strict';
const mongoose = require('mongoose');

const Recording = new mongoose.Schema({
  url: String,
  transcription: String,
  phoneNumber: String,
});

const Agent = new mongoose.Schema({
  extension: String,
  phoneNumber: String,
  recordings: [Recording],
});

const agent = mongoose.model('agent', Agent);
module.exports = agent;
