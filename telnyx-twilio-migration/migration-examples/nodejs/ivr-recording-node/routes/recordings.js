'use strict';

const express = require('express');
const Agent = require('../models/agent');

const router = new express.Router();

// POST: /recordings
// Supports both Telnyx JSON webhook format and TeXML form-encoded callbacks
router.post('/', function(req, res) {
  const agentId = req.query.agentId;
  
  // Determine source (Telnyx JSON vs TeXML form-encoded)
  const isTelnyxWebhook = req.body && req.body.data && req.body.data.payload;
  
  let fromNumber, transcription, recordingUrl;
  
  if (isTelnyxWebhook) {
    // Telnyx callback format (JSON)
    const payload = req.body.data.payload;
    fromNumber = payload.from || req.query.From;
    transcription = payload.transcription || '';
    recordingUrl = payload.recording_urls ? payload.recording_urls.mp3 : '';
  } else {
    // TeXML form-encoded format (similar to Twilio)
    fromNumber = req.body.From;
    transcription = req.body.TranscriptionText || '';
    recordingUrl = req.body.RecordingUrl || '';
  }
  
  Agent.findOne({_id: agentId})
    .then(function(agent) {
      if (!agent) {
        return res.status(404).send('Agent not found');
      }
      agent.recordings.push({
        phoneNumber: fromNumber,
        transcription: transcription,
        url: recordingUrl,
      });
      return agent.save();
    })
    .then(function() {
      res.status(201).send('Recording created');
    })
    .catch(function(err) {
      console.log(err);
      res.status(500).send('Could not create a recording');
    });
});

module.exports = router;
