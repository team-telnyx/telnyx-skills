from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask import url_for
import os

# Import Telnyx SDK instead of Twilio
import telnyx
from telnyx.webhook import WebhookSignature

# Declare and configure application
app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('local_settings.py')


def verify_telnyx_webhook(request) -> bool:
    """Verify Ed25519 webhook signature from Telnyx.
    
    Returns True if the webhook is valid, False otherwise.
    """
    public_key = app.config.get('TELNYX_PUBLIC_KEY')
    if not public_key:
        # Skip verification if public key not configured (dev mode)
        return True
    
    signature = request.headers.get('telnyx-signature-ed25519')
    timestamp = request.headers.get('telnyx-timestamp')
    if not signature or not timestamp:
        return False  # Production requires signature
    
    try:
        # Get raw body for signature verification
        payload = request.get_data(as_text=True)
        WebhookSignature.verify(
            payload=payload,
            signature=signature,
            timestamp=timestamp
        )
        return True
    except Exception:
        return False


# Route for Click to Call demo page.
@app.route('/')
def index():
    return render_template('index.html',
                           configuration_error=None)


# Voice Request URL
@app.route('/call', methods=['POST'])
def call():
    # Get phone number we need to call
    phone_number = request.form.get('phoneNumber', None)

    if not phone_number:
        msg = 'Missing phone number value'
        return jsonify({'error': msg}), 400

    try:
        # Set Telnyx API key
        telnyx.api_key = app.config['TELNYX_API_KEY']
    except Exception as e:
        msg = 'Missing configuration variable: {0}'.format(e)
        return jsonify({'error': msg}), 400

    try:
        # Use Telnyx Call Control API to initiate outbound call
        # connection_id is required for outbound calls with Call Control Apps
        res = telnyx.Call.create(
            to=phone_number,
            from_=app.config['TELNYX_CALLER_ID'],
            connection_id=app.config.get('TELNYX_CONNECTION_ID')
        )
    except Exception as e:
        app.logger.error(e)
        message = e.msg if hasattr(e, 'msg') else str(e)
        return jsonify({'error': message}), 400

    return jsonify({'message': 'Call incoming!'})


@app.route('/outbound', methods=['POST'])
def outbound():
    # Verify webhook signature for production safety
    if not verify_telnyx_webhook(request):
        return 'Forbidden', 403
    
    # Build TeXML (TwiML-compatible XML) response directly
    # Using raw XML string since Telnyx doesn't have a VoiceResponse builder
    response = '''<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say voice="alice">Thank you for contacting our sales department. If this 
        click to call application was in production, we would 
        dial out to your sales team with the Dial verb.</Say>
    <!--
    <Dial>
        <Number>+15558675309</Number>
    </Dial>
    -->
</Response>'''
    return response, 200, {'Content-Type': 'text/xml'}


# Route for Landing Page after deploy.
@app.route('/landing.html')
def landing():
    return render_template('landing.html',
                           configuration_error=None)
