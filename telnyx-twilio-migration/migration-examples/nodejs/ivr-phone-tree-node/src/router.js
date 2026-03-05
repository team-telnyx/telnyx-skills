const Telnyx = require('telnyx');
const Router = require('express').Router;
const ivrRouter = require('./ivr/router');

const router = new Router();

// Initialize Telnyx client
const client = new Telnyx({
  apiKey: process.env.TELNYX_API_KEY,
});

// GET: / - home page
router.get('/', (req, res) => {
  res.render('index');
});

/**
 * Telnyx webhook signature validation middleware
 * @param {Object} req - Express request object
 * @param {Object} res - Express response object
 * @param {Function} next - Express next function
 * @return {void}
 */
function telnyxWebhookValidator(req, res, next) {
  // Skip validation if no public key is configured (development mode)
  if (!process.env.TELNYX_PUBLIC_KEY) {
    console.warn(
      'TELNYX_PUBLIC_KEY not set - skipping webhook signature validation'
    );
    return next();
  }

  try {
    // Use raw body captured by express.json verify callback
    const rawBody = req.rawBody || JSON.stringify(req.body);
    client.webhooks.signature.verifySignature(
      rawBody,
      req.headers['telnyx-signature-ed25519'],
      req.headers['telnyx-timestamp'],
      process.env.TELNYX_PUBLIC_KEY
    );
    next();
  } catch (e) {
    console.error('Webhook signature verification failed:', e.message);
    res.status(403).send('Forbidden');
  }
}

router.use('/ivr', telnyxWebhookValidator, ivrRouter);

module.exports = router;
