'use strict';

const express = require('express');
const { VoiceResponse } = require('../lib/texml');

const router = new express.Router();

// POST: /menu
router.post('/', function(req, res) {
  const selectedOption = req.body.Digits;
  const optionActions = {
    1: returnInstructions,
    2: planets,
  };

  const action = optionActions[selectedOption] || redirectWelcome;
  res.type('text/xml');
  res.send(action().toString());
});

const returnInstructions = function() {
  const texml = new VoiceResponse();
  texml.say('To get to your extraction point, get on your bike and go down ' +
            'the street. Then Left down an alley. Avoid the police cars.' +
            ' Turn left into an unfinished housing development. Fly over ' +
            'the roadblock. Go passed the moon. Soon after you will see ' +
            'your mother ship.', {voice: 'Polly.Amy-Neural', language: 'en-GB'});
  texml.say('Thank you for calling the ET Phone Home Service - the ' +
            'adventurous alien\'s first choice in intergalactic travel');
  texml.hangup();

  return texml;
};

const planets = function() {
  const texml = new VoiceResponse();
  const gather = texml.gather({
    action: '/extension/connect',
    numDigits: '1',
  });
  gather.say('To call the planet Broh doe As O G, press 2. To call the ' +
             'planet DuhGo bah, press 3. To call an oober asteroid to your ' +
             'location, press 4. To go back to the main menu, press ' +
             'the star key ', {loop: '3'});

  return texml;
};

const redirectWelcome = function() {
  const texml = new VoiceResponse();
  texml.redirect('/ivr/welcome');

  return texml;
};

module.exports = router;
