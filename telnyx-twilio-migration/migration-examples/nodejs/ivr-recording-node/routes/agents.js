'use strict';

const express = require('express');
const { VoiceResponse } = require('../lib/texml');
const Agent = require('../models/agent');

const router = new express.Router();

// GET: /agents
router.get('/', function(req, res) {
  Agent.find({})
    .then(function(agents) {
      res.render('agents/index', {agents: agents});
    });
});

// POST: /agents/call
router.post('/call', function(req, res) {
  if (req.body.CallStatus === 'completed') {
    return res.send('');
  }

  const texml = new VoiceResponse();
  texml.say('It appears that no agent is available. ' +
    'Please leave a message after the beep',
    {voice: 'Polly.Amy-Neural', language: 'en-GB'});
  texml.record({
    maxLength: 20,
    action: '/agents/hangup',
    transcribeCallback: '/recordings?agentId=' + req.query.agentId,
    channels: 'single',
  });
  texml.say('No record received. Goodbye',
    {voice: 'Polly.Amy-Neural', language: 'en-GB'});
  texml.hangup();

  res.type('text/xml');
  res.send(texml.toString());
});

// POST: /agents/hangup
router.post('/hangup', function(req, res) {
  const texml = new VoiceResponse();
  texml.say('Thanks for your message. Goodbye',
    {voice: 'Polly.Amy-Neural', language: 'en-GB'});
  texml.hangup();

  res.type('text/xml');
  res.send(texml.toString());
});

// POST: /agents/screencall
router.post('/screencall', function(req, res) {
  const texml = new VoiceResponse();
  const gather = texml.gather({
    action: '/agents/connectmessage',
    numDigits: '1',
  });
  gather.say(spellPhoneNumber(req.body.From));
  gather.say('Press any key to accept');

  texml.say('Sorry. Did not get your response');
  texml.hangup();

  res.type('text/xml');
  res.send(texml.toString());
});

// POST: /agents/connectmessage
router.post('/connectmessage', function(req, res) {
  const texml = new VoiceResponse();
  texml.say('Connecting you to the extraterrestrial in distress');

  res.type('text/xml');
  res.send(texml.toString());
});

const spellPhoneNumber = function(phoneNumber) {
  return phoneNumber.split('').join(',');
};

module.exports = router;
