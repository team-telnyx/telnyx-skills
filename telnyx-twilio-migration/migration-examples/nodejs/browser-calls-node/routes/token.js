const express = require('express');
const router = express.Router();

const Telnyx = require('telnyx');
const config = require('../config');

// Initialize Telnyx client
const telnyx = new Telnyx({ apiKey: config.telnyxApiKey });

// POST /token/generate
// Returns a JWT login token for Telnyx WebRTC client
router.post('/generate', async function (req, res) {
  try {
    const page = req.body.page;
    const clientName = (page == "/dashboard" ? "support_agent" : "customer");

    // 1. Create a telephony credential for this session
    const credentialResponse = await telnyx.telephonyCredentials.create({
      connection_id: config.telnyxConnectionId,
      name: clientName,
    });

    const credentialId = credentialResponse.data.id;

    // 2. Generate a JWT login token for the credential
    // The createToken endpoint returns the JWT directly as a string
    const tokenResponse = await telnyx.telephonyCredentials.createToken(credentialId);
    
    // Handle different response formats from the SDK
    let token;
    if (typeof tokenResponse === 'string') {
      token = tokenResponse;
    } else if (tokenResponse && tokenResponse.data && tokenResponse.data.token) {
      token = tokenResponse.data.token;
    } else if (tokenResponse && tokenResponse.token) {
      token = tokenResponse.token;
    } else {
      // If we can't extract token from response, fall back to REST API call
      const fetch = require('node-fetch');
      const apiKey = config.telnyxApiKey;
      const restResponse = await fetch(
        `https://api.telnyx.com/v2/telephony_credentials/${credentialId}/token`,
        {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${apiKey}`,
            'Content-Type': 'application/json'
          }
        }
      );
      token = await restResponse.text();
    }

    res.setHeader('Content-Type', 'application/json');
    res.send(JSON.stringify({ 
      token: token,
      credential_id: credentialId,
      sip_username: credentialResponse.data.sip_username,
      sip_password: credentialResponse.data.sip_password
    }));
  } catch (error) {
    console.error('Error generating Telnyx credential:', error);
    res.status(500).json({ 
      error: 'Failed to generate credentials',
      details: error.message 
    });
  }
});

module.exports = router;
