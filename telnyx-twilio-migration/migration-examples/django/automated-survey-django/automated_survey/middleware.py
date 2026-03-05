class SMSMiddleware:
    """Middleware to detect SMS requests from both Twilio and Telnyx webhooks."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Support both Twilio (MessageSid) and Telnyx (message_id/id in JSON) formats
        args = request.POST or request.GET

        # Twilio form-encoded uses MessageSid
        has_twilio_sms_sid = args and args.get('MessageSid')

        # Telnyx uses nested JSON structure with event_type
        is_telnyx_sms = False
        if request.content_type == 'application/json' and request.body:
            import json
            try:
                body_str = request.body.decode('utf-8') if isinstance(request.body, bytes) else request.body
                data = json.loads(body_str)
                event_type = data.get('data', {}).get('event_type', '')
                is_telnyx_sms = 'message' in event_type
            except (json.JSONDecodeError, AttributeError):
                pass

        request.is_sms = has_twilio_sms_sid or is_telnyx_sms
        response = self.get_response(request)
        return response
