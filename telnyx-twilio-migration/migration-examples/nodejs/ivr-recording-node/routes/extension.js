'use strict';

const express = require('express');
const { VoiceResponse } = require('../lib/texml');
const Agent = require('../models/agent');

const router = new express.Router();

// POST: /extension/connect
router.post('/connect', function(req, res) {
  const selectedOption = req.body.Digits;
  const extensions = {
    2: 'Brodo',
    3: 'Dagobah',
    4: 'Oober',
  };

  Agent.findOne({extension: extensions[selectedOption]})
    .then(function(agent) {
      if (agent === null) {
        return res.type('text/xml').send(redirectToWelcome());
      }

      const texml = new VoiceResponse();
      texml.say('You\'ll be connected shortly to your planet.',
        {voice: 'Polly.Amy-Neural', language: 'en-GB'});
      const dial = texml.dial({
        action: `/agents/call?agentId=${agent.id}`,
        callerId: agent.phoneNumber,
      });
      dial.number(agent.phoneNumber, {url: '/agents/screencall'});

      res.type('text/xml');
      res.send(texml.toString());
    })
    .catch(function(err) {
      console.log(err);
      res.status(500).send('An error has ocurred');
    });
});

const redirectToWelcome = function() {
  const texml = new VoiceResponse();
  texml.redirect('/ivr/welcome');

  return texml.toString();
};

module.exports = router;
