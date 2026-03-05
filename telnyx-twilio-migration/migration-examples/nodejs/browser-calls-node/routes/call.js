const express = require('express');
const router = express.Router();

const config = require('../config');

// POST /calls/connect
// NOTE: With Telnyx WebRTC, this endpoint is OPTIONAL
// The browser client can dial directly using client.newCall()
// This endpoint is kept for backward compatibility if needed
// but is no longer required for basic browser-to-phone calls.
router.post('/connect', function(req, res, next) {
  // With Telnyx WebRTC, the browser client dials directly.
  // No server-side TwiML/TeXML required for simple dial cases.
  // This endpoint can be used for complex routing if needed.
  
  res.status(200).json({
    message: 'Telnyx WebRTC uses direct browser dialing. No server-side call routing required.',
    note: 'For complex routing, implement Call Control API or TeXML endpoints.'
  });
});

module.exports = router;
