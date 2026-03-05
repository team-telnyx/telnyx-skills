'use strict';

const express = require('express');
const { VoiceResponse } = require('../lib/texml');

const router = new express.Router();

// POST: /ivr/welcome
router.post('/welcome', function(req, res) {
  const texml = new VoiceResponse();
  const gather = texml.gather({
    action: '/menu',
    numDigits: '1',
  });
  gather.play({loop: 3}, 'https://can-tasty-8188.twil.io/assets/et-phone.mp3');

  res.type('text/xml');
  res.send(texml.toString());
});

module.exports = router;
